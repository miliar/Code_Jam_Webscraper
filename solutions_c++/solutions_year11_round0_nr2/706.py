// codejam.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int testnum ;
int C;
int D;
int N;

char cstr[3];
char dstr[2];
char nstr[110];

char r[110];
int len;

int com[26][26];
int opp[26][26];
int count[26];

void myinit(){
	int i,j;
	for(i=0;i<26;i++){
		for(j=0;j<26;j++){
			com[i][j] = -1;
			opp[i][j] = 0;
		}
		count[i] = 0;
	}
	for(i=0;i<110;i++)
		r[i] = 0;
	len = 0;
}

inline int  char2int(char c){
	return c-'A';
}

inline char int2char(int i){
	return i+'A';
}

void fun(int i){
	int t1,t2,t3;

	//insert i
	r[len++] = nstr[i];
	t1 = char2int(r[len-1]);
	count[t1] ++;

	if(len == 1)
		return ;

	
	//step 1: check com
	bool iscom = false;
	do{
		t1 = char2int(r[len-1]);
		t2 = char2int(r[len-2]);
		t3 = com[t1][t2];
		if( t3 != -1){
			len = len -2;
			r[len++] = int2char(t3);
			count[t1] --;
			count[t2] --;
			count[t3] ++;
			iscom = true;
		}
		else
			iscom =false;
	}while(iscom && len >= 2);

	//step 2: chek opp
	int temp = char2int(r[len-1]);
	for(int i=0;i<len-1;i++){
		t1 = char2int(r[i]);
		if(opp[t1][temp] == 1){
			len = 0;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\B.txt");
	ofstream out("D:\Br.txt");

	in >> testnum;
	cout << testnum << endl;
	
	int i,t1,t2,t3;
	int num = 1;
	while(testnum-- > 0){
		cout << testnum+1<<" case *************************************\n";

		myinit();

		in >> C;
		for( i =0;i<C;i++){
			in >> cstr;
			//cout << cstr << endl;
			t1 = char2int(cstr[0]);
			t2 = char2int(cstr[1]);
			t3 = char2int(cstr[2]);
			com[t1][t2] = com[t2][t1] = t3;
		}

		in >> D;
		for( i =0;i<D;i++){
			in >> dstr;
			//cout << dstr << endl;
			t1 = char2int(dstr[0]);
			t2 = char2int(dstr[1]);
			opp[t2][t1] = opp[t1][t2] = 1;
		}

		in >> N;
		in >> nstr;
		//cout << nstr << endl;
		for(i=0;i<N;i++)
			fun(i);

		out<<"Case #"<<num++<<": [";
		for(i=0;i<len-1;i++)
			out<<r[i]<<", ";
		if(len-1>=0)
			out<<r[len-1];
		out<<"]"<<endl;
	}

	in.close();
	out.close();
	return 0;
}








