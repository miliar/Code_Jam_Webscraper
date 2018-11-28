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


 /*getline(cin,s);
      istringstream ss(s);
    
    
      while(ss>>t) {
	}*/
//#define fout cout
int N;


int main()
{
	ifstream fin("ReadMe.txt");
	fin>>N;
	ofstream fout("out.txt");

	char sr[1000];
	fin.getline(sr,10);
	Rep(ti,N)
	{
		char str[1000];
		fin.getline(str,100);
		char ch=str[0];
		for(int i=0;str[i]!=0;i++)
			if(str[i]==ch)
				str[i]=2;
		int count=1;
		for(int i=0;str[i]!=0;i++)
		{
			if(str[i]>11)
			{
				char ch=str[i];
				for(int j=i;str[j]!=0;j++)
					if(str[j]==ch)
						str[j]=count;
			
				if(count==1)count=3;
				else
					count++;
			}
		}
		count--;
		//if(count
		int64 sum=0,b=1;
		if(count==0)
			count=2;
		for(int i=strlen(str)-1;i>=0;i--)
		{
			sum+=(str[i]-1)*b;
			b*=count;
		}
	
		fout<<"Case #"<<ti+1<<": "<<sum<<endl;
		cout<<"Case #"<<ti+1<<": "<<sum<<endl;
	}
	fin.close();
	fout.close();
	getchar();
	return 0;
}
