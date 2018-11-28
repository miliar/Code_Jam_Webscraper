#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<locale>
using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
#define inp(n) scanf("%d",&n)
#define MOD 1000000007
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef  unsigned long long ull;
int main()
{
	string s = "ynficwlbkuomxsevzpdrjgthaq";
	string s1 = "abcdefghijklmnopqrstuvwxyz";
	int n;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>n;
	getchar();
	char ss[100];
	rep(i,n){
		string ret = "";
		gets(ss);
		rep(j,strlen(ss)){
			if(isspace(ss[j])){
				ret+=" ";
			}
			else{
				string temp ="";
				rep(k,s.size())
				if(s[k] == ss[j])
					temp = s1.substr(k,1);
				
				
				ret+= temp;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}	