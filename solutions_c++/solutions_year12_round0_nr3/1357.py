/*
 * C.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Chan
 */
#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <sstream>
#include <map>
#include <fstream>
using namespace std;

int pow(int a, int b){
	int rt = 1;
	while(b-->0) rt*=a;
	return rt;
}

int merge1(vector<int> A,vector<int> B, int ten2da, int ten2db);
int merge2(int inf,int sup,vector<int> A,vector<int> B, int ten2da, int ten2db);

vector<int>& vectorA(vector<int>& A, int lowest, int highest){
	A.clear();
	for(int i=lowest; i<= highest; ++i) A.push_back(i);
	return A;
}

vector<int>& vectorB(vector<int>& B, int lowest, int highest){
	B.clear();
	for(int i=lowest; i<= highest; ++i) B.push_back(i);
	return B;
}

map<string,int> chk;

int main(){
	vector<int> a;
	vector<int> b;
	ifstream fin;
	ofstream fout;
	fin.open("inout/C-large.in");
	fout.open("inout/C-large.out");
	int T,t;
	fin >> T;
	t=0;

	while(t++!=T)
	{
		int inf, sup;
		fin >> inf >> sup;

		stringstream ss;
		ss << inf ;
		string sss = ss.str();

		int digits =sss.size();
		int ten2d = pow(10,digits);
		chk.clear();
		for(int d=1;d<digits;++d){
			int ten2da = pow(10,d), ten2db = ten2d/ten2da;
			vectorA(a,inf/ten2db, ten2da-1);
			vectorB(b,ten2db/10,sup/ten2da);
			merge2(inf,sup,a,b,ten2da,ten2db);
		}

		fout << "Case #" << t << ": " << chk.size() << endl;
	}
    return 0;
}

int bfirst(int a, int b, int ten2da, int ten2db){
	return b*ten2da+a;
}

int afirst(int a, int b, int ten2da, int ten2db){
	return a*ten2db+b;
}

// Ascending order assumed
int merge1(vector<int> A,vector<int> B, int ten2da, int ten2db){
	int count(0);//vector<int> rt;

	typedef vector<int>::reverse_iterator viter;
	viter itrb = B.rbegin();
	viter itra = A.rbegin();
	while(itrb!=B.rend()&&itra!=A.rend())
	{
		while(itra!=A.rend() && afirst(*itra,*itrb,ten2da,ten2db)
				>= bfirst(*itra,*itrb,ten2da,ten2db))
		{
			++itra;
		}
		if(itra!=A.rend()){
//			viter tmp = itra;
//			while(tmp!=A.rend()){
//				rt.push_back(bfirst(*tmp,*itrb,ten2da,ten2db));
//				++tmp;
//			}
			count+=A.rend()-itra;
		}
		++itrb;
	}

	return count;
}

int merge2(int inf, int sup , vector<int> A, vector<int> B, int ten2da, int ten2db){
	int rt(0);

	typedef vector<int>::reverse_iterator viter;

	for(viter itrb=B.rbegin(); itrb != B.rend();++itrb){
		for(viter itra=A.rbegin(); itra != A.rend();++itra){
			int ab=afirst(*itra,*itrb,ten2da,ten2db);
			int ba=bfirst(*itra,*itrb,ten2da,ten2db);

			if( inf <= ab && ab < ba && ba <= sup )
			{
				++rt;
				stringstream ss;
				ss << ab << ba ;
				chk[ss.str()]++;
			}
		}
	}

	return rt;
}
