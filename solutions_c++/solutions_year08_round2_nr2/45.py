#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
template<class T> T gcd(T a, T b) { return(b>0) ? gcd(b,a%b) : a; }
typedef long long ll;
typedef vector<int> VI;

FILE* fi; FILE* fo;
int i,j, u,n, a,b,p, k, t,v;
int c[1000000];
int pr(int x) { if(c[x]!=x) c[x]=pr(c[x]); return c[x]; }

int main()
{
	fi=fopen("b-small.in","r"); //large
	fo=fopen("b-small.res","w");
	fscanf(fi,"%d",&n);
	rep(u,n)
	{
		fscanf(fi,"%d%d%d",&a,&b,&p);
		forr(i,a,b) c[i]=i;
		forr(i,a,b) forr(j,i+1,b)
		{ t=gcd(i,j);
			forr(v,2,p-1) while(t%v==0) t/=v;
			if(t>=p) c[pr(j)]=pr(i);
		}
		k=0;
		forr(i,a,b)
		{
//			cout<<i<<' '<<pr(i)<<'\n';
			if(pr(i)==i) k++;
		}
		fprintf(fo,"Case #%d: %d\n",u+1,k);
	}
	fclose(fi); fclose(fo);
	getchar();
	return 0;
}
