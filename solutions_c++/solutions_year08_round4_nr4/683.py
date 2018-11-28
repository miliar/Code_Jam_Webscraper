#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vvi vector<vector<int> >
#define co continue
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define br break
#define re return
#define ALL(v) v.begin(),v.end() 

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define SZ size()
#define INF (2<<29)

#define pii pair<int ,int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin() ; it!=(c).end() ;it++)
template <class T> inline int BITCNT(T x) { int ret=0; while (x) { ret++; x&=x-1; } return ret; }

using namespace std;
int perm[17];
int main()
{
    int kases;
    cin>>kases;
    for(int kase = 1 ; kase<=kases; kase++)
    {
		int k;
		cin>>k;
		string s;
		cin>>s;
		REP(i,k) perm[i] = i;
		int ans = 10000000;
		do
		{
			string res;
			for(int pos = 0 ; pos < s.size();pos+=k)
			{
				string t;
				
				REP(i , k)
				{
					int ind = i + pos;
					t+= s[pos + perm[i]];
				}
				res += t;
			}
			int ret=0;
			for(int i=1;i<res.size();i++)
			{
				if(res[i-1]!=res[i]) ret++;	
			}
			ans = min(ans , ret);
		}while(next_permutation(perm , perm+k));
		cout<<"Case #"<<kase<<": "<<ans+1<<endl;
	}
}
