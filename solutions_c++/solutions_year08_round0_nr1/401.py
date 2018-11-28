#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define REP(i,u) for(long long i=0;i<u;i++)
#define FOR(i,z,u) for(long long i=(z);i<=(u);i++)
#define FORO(i,z,u,p) for(long long i=(z);i<=(u);i=i+(p))
#define M 100
using namespace std;


bool bol[105];
int N,S,Q,res,poc,ind;
char c;
string s;
string v[105];
int q[1005];

int finds(string s)
{
	REP(i,S) 
		if(v[i]==s) 
			return i;
	return -1;
}

int main() 
{
	cin>>N;
	REP(p,N)
	{
		memset(bol,0,sizeof(bol));
		res=poc=0;
		cin>>S;
		getchar();
		REP(i,S)
		{
			s="";
			while((c=getchar())!='\n')s+=c;
			v[i]=s;
		}
		cin>>Q;
		getchar();
		REP(i,Q)
		{
			s="";
			while((c=getchar())!='\n')s+=c;
			ind=finds(s);
			if(bol[ind]==0)
			{
				poc++;
				bol[ind]=1;
			}
		//	cout<<s<<" "<<poc<<" "<<S<<endl;
			if(poc==S)
			{
				res++;
				poc=0;
				memset(bol,0,sizeof(bol));
				poc++;
				bol[ind]=1;
			}
		}
		cout<<"Case #"<<p+1<<": "<<res<<endl;
	}
	return 0;
}
