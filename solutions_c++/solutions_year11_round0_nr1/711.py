// codejam-A.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>

using namespace std;

int testnum ;
int curnum;

int N;
int a[110][2];

int Rd;
int Bd;
int Rtask ;
int Btask ;
int Rpos;
int Bpos;

int curtask;
int time;

int choice(){
	int i;
	if(Rtask == -1){
		for(i=curtask;i<N;i++)
			if(a[i][0] == 0){
				Rtask = i;
				break;
			}
		if(i==N)
			Rtask = i;
	}
	if(Btask == -1){
		for(i=curtask;i<N;i++)
			if(a[i][0] == 1){
				Btask = i;
				break;
			}
		if(i==N)
			Btask = i;
	}


	int temp = a[Rtask][1] - Rpos;
	if(temp >0)
		Rd = 1;
	else if(temp==0)
		Rd = 0;
	else{
		Rd = -1;
		temp = -temp;
	}

	int temp2 = a[Btask][1] - Bpos;
	if(temp2 >0)
		Bd = 1;
	else if(temp2 == 0)
		Bd = 0;
	else{
		Bd = -1;
		temp2 = -temp2;
	}

	int min = temp;
	if(temp > temp2) min = temp2;

	return min;
}

void done( int step ){
	int temp;
	if(step == 0){
		if(Btask < Rtask  ){
			if(Bd == 0 ){	
				time ++;
				Rpos += Rd * 1;
			}
			else{
				 temp = Bpos - a[Btask][1];
				if(temp <0)temp = -temp;
				
				time += temp+1;
				Bpos += Bd*temp;
			}
			curtask ++;
			Btask = -1;
		}
		else{
			if(Rd == 0 ){	
				time ++;
				Bpos += Bd * 1;
			}
			else{
				 temp = Rpos - a[Rtask][1];
				if(temp <0)temp = -temp;
				Rpos += Rd*temp;
				time += temp+1;
			}
			curtask ++;
			Rtask = -1;
		}
	}
	else{
		Rpos += Rd*step;
		Bpos += Bd*step;
		time += step;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\A-small.txt");
	ofstream out("D:\Ar-small.txt");
	
	in>>testnum;
	curnum = 1;
	int i;
	while( testnum-- > 0){
		in >> N;
		for(int i=0;i<N;i++){
			char c;
			in >> c;
			if(c == 'B') a[i][0] = 1;
			else a[i][0] = 0;
			in >> a[i][1];
		}
		a[N][1] = 10000;

		//init
		time = 0;
		Rtask = Btask = -1;
		Rpos = Bpos = 1;
		curtask = 0;

		//do
		while(curtask < N ){
			int k = choice();
			done(k);
		}

		cout << time << endl;
		
		out <<"Case #"<<curnum++<<": ";
		out << time << endl;
	}

	in.close();
	out.close();

	return 0;
}




