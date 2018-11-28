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

char str[1000],len;
int s[1000][30];


int getval(int pos,char combo[])
{
	int ret=0;
	if(s[pos][19-strlen(combo)]!=-1)
		return s[pos][19-strlen(combo)];
	if(combo[0]==0)
		return 1;
	for(int i=pos;str[i]!=0;i++)
		if(str[i]==combo[0])
		{
			ret+=getval(i+1,combo+1);
		}
	s[pos][19-strlen(combo)]=ret;
	return ret;
}

int main()
{
	ifstream fin("ReadMe.txt");
	fin>>N;
	ofstream fout("out.txt");
	fin.getline(str,9);
	Rep(ti,N)
	{
		Fill(s,-1);
		fin.getline(str,900);
		for(int i=0;str[i]!=0;i++)
			if( str[i]=='w' ||str[i]=='e' ||str[i]=='l' ||str[i]=='c' ||str[i]=='o' ||str[i]=='m' ||str[i]=='e' ||str[i]==' ' ||str[i]=='t' ||str[i]=='j' ||str[i]=='d' ||str[i]=='a' ||str[i]=='m');
			else
			{
				for(int j=i;str[j]!=0;j++)
					str[j]=str[j+1];
				i--;
			}
		len=strlen(str);
		int count=getval(0,"welcome to code jam");
		fout<<"Case #"<<ti+1<<": ";
		if(count<1000)
			fout<<'0';
		if(count<100)
			fout<<'0';
		if(count<10)
			fout<<'0';

		fout<<count<<endl;
		cout<<"Case #"<<ti+1<<": "<<count<<endl;
	}
	fin.close();
	fout.close();
	getchar();
	return 0;
}