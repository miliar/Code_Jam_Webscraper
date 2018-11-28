#include"stdafx.h"


#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
//#include <windows.h>
using namespace std;
using std::vector;

typedef unsigned long long int64;
//typedef vector<int,int,int> v3i;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

int64 ans=0;



//#define fout cout
int L,D,N;

bool satisfy(char chk[],char str[])
{
	for(int i=0,j=0;str[i]!=0;i++)
	{
		int c;		//c=0 variable c=1 fixed
		if(chk[j]=='(')
			c=0;
		else
			c=1;
		if(c==1)
			if(chk[j]!=str[i])
				return false;
			else
				j++;
		else
		{
			j++;
			while(chk[j]!=str[i] && chk[j]!=')')j++;
			
			if(chk[j]==')')
				return false;
			while(chk[j]!=')')j++;
				j++;
		}
	}
	return true;
}





int main()
{
	ifstream fin("ReadMe.txt");
	fin>>L>>D>>N;
	ofstream fout("out.txt");
	char str[10000][20];
	fin.getline(str[0],9);
	Rep(i,D)
	{
		fin.getline(str[i],20);
	}
	Rep(ti,N)
	{
		char chk[2000];
		fin.getline(chk,1900);
		int count=0;
		Rep(i,D)
		{
			if( satisfy(chk, str[i]))
				count++;
		}
		fout<<"Case #"<<ti+1<<": "<<count<<endl;
		cout<<"Case #"<<ti+1<<": "<<count<<endl;
	}
	fin.close();
	fout.close();
	getchar();
	return 0;
}
