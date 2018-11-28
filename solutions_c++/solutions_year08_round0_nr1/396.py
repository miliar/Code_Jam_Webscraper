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
typedef long long ll;
typedef vector<int> VI;

FILE* fi; FILE* fo;
int u,i,j,k,x, n,s,q;
string a[101], o; char t[200];
bool y[101];

int main()
{
	fi=fopen("a-large.in","r");
	fo=fopen("a-large.res","w");
	fscanf(fi,"%d",&n);
	rep(u,n)
	{
		x=0; k=0; mset(y,0);
		fscanf(fi,"%d\n",&s);
		rep(i,s) fgets(t,200,fi), a[i]=string(t);
		fscanf(fi,"%d\n",&q);
		rep(j,q)
		{
			fgets(t,200,fi), o=string(t);// printf("%d: %s",j,o.c_str());
			rep(i,s) if(o==a[i])
			{
				if(!y[i])	{	k++;
					if(k==s) x++, mset(y,0), k=1; }
				y[i]=1; break;
			}
		}
		fprintf(fo,"Case #%d: %d\n",u+1,x);
	}
	fclose(fi); fclose(fo);
//	getchar();
	return 0;
}
