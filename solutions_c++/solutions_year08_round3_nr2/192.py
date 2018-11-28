#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include<cmath>
#include<iomanip>
#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll Dat[15][15];
string word;
int len;
set<ll>comm;
ll Ans;
void Solve(ll last,int a,int b,int cha)
{
	ll tmp1=last;
	if(cha==0)
	{
		tmp1=tmp1+Dat[a][b];
	}
	else
	{
		tmp1=tmp1-Dat[a][b];
	}
	if(tmp1%2==0||tmp1%3==0||tmp1%5==0||tmp1%7==0)
	{
		Ans++;
	}
	for(int i=a+1;i<=b;i++)
	{
		ll tmp=last;
		if(cha==0)
		{
			tmp=tmp+Dat[a][i-1];		
		}
		else
		{
			tmp=tmp-Dat[a][i-1];
		}
		Solve(tmp,i,b,0);
		Solve(tmp,i,b,1);
	}
}
int  main(){
	string filein;
	filein="B-small-attempt2.in";
	//filein="A-large.in";
	//filein="A-small(3).in";
	//filein="A-small-attempt0.in";
	//filein="B-small-attempt0.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	//fileout="Anssmall.txt";
	freopen(filein.c_str(), "r", stdin);
	freopen(fileout.c_str(), "w", stdout);
	int  Case;
	cin>>Case;
	for(int  i=1;i<=Case;i++)
	{
		printf("Case #%d: ",i);
		cin>>word;
		len=word.length();
		memset(Dat,0,sizeof(Dat));
		//Dat[1][len]=atoi(word.c_str());
		stringstream ss;
		ss<<word;
		ss>>Dat[1][len];
		for(int j=2;j<=len;j++)
		{
			string tmp=string(word.begin()+j-1,word.end());
			//Dat[j][len]=atoi(tmp.c_str());
			ss.clear();
			ss<<tmp;
			ss>>Dat[j][len];
		}
		for(int j=1;j<=len;j++)
		{
			for(int k=len-1;k>=1;k--)
			{
				Dat[j][k]=Dat[j][k+1]/10;
			}
		}
		//comm.clear();
		Ans=0;
		Solve(0,1,len,0);
		cout<<Ans<<endl;
	}
	return 0;
}