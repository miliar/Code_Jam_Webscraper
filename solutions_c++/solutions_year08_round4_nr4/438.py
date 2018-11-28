#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
//#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
int cnt,cc;
string s,t,p;
int k;
vi ch;
int i,j,rez,ans;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		cout<<"Case #"<<cc<<": ";
		cin>>k;
		cin>>s;
		ch.clear();
		for(i=0;i<k;i++)
			ch.pb(i);
		ans=inf;
		for(int cn=0;cn<120;cn++)
		{
			t="";
			for(i=0;i<L(s);i++)
				t+=" ";
			for(i=0;i<L(s);i+=k)
			{
				for(j=i;j<i+k;j++)
					t[j]=s[i+ch[j%k]];
			}
			rez=1;
			for(i=1;i<L(t);i++)
				if (t[i]!=t[i-1])
					rez++;
			ans=min(ans,rez);
			next_permutation(all(ch));
		}
		cout<<ans<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}