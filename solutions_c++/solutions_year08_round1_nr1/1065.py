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
	int T,n;
	int z=1;
	cin >> T;
	while(T-- >0)
	{
		cin >>n;
		vi a1,a2;
		
		int i,j,m;
		fr( i,0,2 )
		{
			char a[10000];
			int y,x=0;
			cin>>y;
			cin.getline( a ,10000 );
			string b="";
			int k=0;			
			while(a[k]!='\0')
			{
				b+=a[k];
				k++;
			}
			stringstream s;
			s<<b;
			if(i==0)
			{
				pb(a1,y);
				while(s>>x)
				pb(a1,x);
			}
			else 
			{
				pb(a2,y);
				while(s>>x)
				pb(a2,x);
			}
		}
		srt(a1);
		revsrt(a2);
		int sum=0;
		frsz(m,a1)
		{
			sum+=a1[m]*a2[m];
		}
		answer<<"Case #"<<z<<": "<<sum<<endl;
		z++;
	}
	return 0;
}