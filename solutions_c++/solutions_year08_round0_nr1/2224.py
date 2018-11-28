#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <fstream>
#include<queue>

using namespace std;

#define fr(i,a,b) for(i=(int)a;i<(int)b;i++)
#define frd(i,a,b) for(i=(int)a;i>(int)b;i--)
#define sz(v) (int)v.size()
#define clr(a,b) memset(a,b,sizeof(a)) 
#define frsz(i,v) for( i=0;i<(int)sz(v);i++)
#define frdsz(i,v) for( i=(int)sz(v)-1;i>=0;i--)
#define pb(v,i) v.push_back(i)
#define srt(a) sort(a.begin(),a.end())
#define revsrt(a) sort(a.rbegin(),a.rend())
#define tr(ii,v) for(ii=v.begin(); ii!=v.end(); ii++)
#define tr2(jj,ii) for(jj=(*ii).begin(); jj!=(*ii).end(); jj++)



typedef vector <int> vi;
typedef vector <string> vs;
typedef vector < vector <int> > vi2;
typedef vector <double> vd ;
typedef vector <long long> vll ;

int main()
{
	ofstream answer("final1.txt");
	int T,S,Q,i=0;
	cin >> T;
	while( T-- > 0 )
	{
		cin >> S;
		vs engine;
		while( S-- >= 0 )
		{
			char a[100];
			cin.getline( a ,100 );
			string b="";
			int i=0;
			while(a[i]!='\0')
			{
				b+=a[i];
				i++;
			}
			pb(engine,b);
		}
		
		cin >> Q;
		int q=Q;
		vs cases;
		while( Q-- >= 0 )
		{
			char a[100];
			cin.getline( a ,100 );
			string b="";
			int i=0;
			while(a[i]!='\0')
			{
				b+=a[i];
				i++;
			}
			pb(cases,b);
		} 
		int arr[sz(cases)][sz(engine)];
		
		int m,n;
		frsz(m,cases)
		if(cases[m]=="")
		{
			cases.erase(cases.begin()+m);
			m--;
		}
		frsz(n,engine)
		if(engine[n]=="")
		{
			engine.erase(engine.begin()+n);
			n--;
		}
		frsz(m,cases)
		{
			if(m==0)
				frsz(n,engine)
				if(cases[m]==engine[n]) arr[m][n]=10001;
				else arr[m][n]=0;
			else
			{
				int mn=1001;
				frsz(n,engine)
				mn=min(mn,arr[m-1][n]);
				vi temp;
				frsz(n,engine)
				if(arr[m-1][n]==mn) pb(temp,n);
				frsz(n,engine)
				if(engine[n]==cases[m])
					arr[m][n]=10001;
				else
				{
					int rt;
					bool g=0;
					frsz(rt,temp)
					if(temp[rt]==n)
					{
						g=1;
						arr[m][n]=mn;
					}
					if(g==0)
					arr[m][n]=mn+1;
				}
			}
			
		}
		int mn1=1001;
		frsz(m,engine)
		mn1=min(mn1,arr[sz(cases)-1][m]);
		int h,k;
		if(q==0)
		answer<<"Case #"<<i+1<<": "<<0<<endl;
		else answer<<"Case #"<<i+1<<": "<<mn1<<endl;
		i++;
	}
	return 0;
}