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
#define For(i,a,b) for (int64 i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int64 i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int64 i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int64 i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

int64 ans=0;

template<typename T, typename S> T cast(S s)
{
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}


int L,D,N;

int main()
{
	ifstream fin("ReadMe.txt");
	fin>>N;
	ofstream fout("out.txt");
	char str[2000];
	//fin.getline(str,1000);
	
	fin.getline(str,2000);
	Rep(ti,N)
	{
		char p[100];
		fin.getline(p,100);
		vi dig;
		int64 i,l;
		for(i=0;p[i]!=0;i++)
				dig.push_back(p[i]-'0');
		l=dig.size();
		int chk=0;
		for(i=l-1;i>0;i--)
		{
			if(dig[i]>dig[i-1])
			{
				chk=1;
				break;
			}
		}
		if(chk==0)
		{
			dig.push_back(0);
			sort(dig.begin(),dig.end());
			int i;
			for(i=0;i<=l;i++)
				if(dig[i]>0)
					break;
			int x=dig[0];
			dig[0]=dig[i];
			dig[i]=x;
			l++;
		}
		else
		{
			for(int i=l-1;i>=0;i--)
			{
				if(dig[i]<=dig[i-1]);
				else
				{
					i--;
					int no=dig[i+1],pos=i+1;
					int j;
					for(j=i+1;j<l;j++)
						if(dig[j]>dig[i] && dig[j]<no)
						{
							no=dig[j];
							pos=j;
						}
					j=pos;
					int x=dig[i];
					dig[i]=dig[j];
					dig[j]=x;
					//swap(dig.begin()+i,dig.begin()+j);
					sort(dig.begin()+i+1,dig.end());
					break;
				}
			}


		}
		fout<<"Case #"<<ti+1<<": ";
		Rep(k,l)
			fout<<dig[k];
		fout<<endl;
		cout<<"Case #"<<ti+1<<": ";
		Rep(k,l)
			cout<<dig[k];
		
		cout<<endl;
	}
	fin.close();
	fout.close();
	getchar();
	return 0;
}