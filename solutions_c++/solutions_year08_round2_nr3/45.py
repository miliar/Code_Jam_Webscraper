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
int i,j,c, u,N, k,n,d, k1,v,t;

int main()
{
	fi=fopen("c-large.in","r");
	fo=fopen("c-large.res","w");
	fscanf(fi,"%d",&N);
	rep(u,N)
	{
		fscanf(fi,"%d%d",&k,&n);
		fprintf(fo,"Case #%d: ",u+1);
		rep(i,n)
		{
			fscanf(fi,"%d",&d); d--;
			k1=k; v=1;
			while(d>0)
			{
				v++; k1--; t=v%k1;
//				cout<<v<<':'<<k1<<','<<d<<' ';
				if(d>=t) d=(d-t) % k1;
				else d=(k1-t+d) % k1;		
			}
//			cout<<'0'; getchar();
			fprintf(fo,"%d ",v);
		}
		fprintf(fo,"\n");
	}
	fclose(fi); fclose(fo);
//	getchar();
	return 0;
}
