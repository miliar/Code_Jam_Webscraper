#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forin(i,in,n) for(int i = (int)in; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)

string ff = "welcome to code jam";
string ss;
long long ma[1000][50];
long long dfs(int no,int pos)
{  
	if (ma[pos][no] != -1) return ma[pos][no];
	if (no == ff.size())
	{
		ma[pos][no] = 1;
	} 
	else
	{
		long long sum = 0;
		forin(i,pos,ss.size())
		{
			if (ss[i] == ff[no])
			{          
      
				sum+=dfs(no+1,i);
			}

		}
		ma[pos][no] = sum%10000;
	}
	return ma[pos][no];
}
main()
{
	int n;
	cin>>n;
	ff = "welcome to code jam";
	getline(cin,ss);
	forn(i,n)
	{
		forn(j,1000)
			forn(k,40)
				ma[j][k] = -1;
		getline(cin,ss);
	// cout<<ss;
		long long aa = dfs (0,0) % 10000;
		
		cout<<"Case #"<<i+1<<": ";
        cout<<aa/1000;
        aa = aa % 1000;
        cout<<aa/100;
        aa = aa%100;
        cout<<aa/10;
        aa = aa%10;
        cout<<aa<<endl;
		
	}
}




 
