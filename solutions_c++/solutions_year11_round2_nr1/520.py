#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

char a[201][201];
int mat[201][201];
int n,t;
double WP[201],OWP[201],OOWP[201],res[201];

double compWP(int ind,int x=-1)
{
	int tot=0,win=0;
	rep(i,0,n){
		if(i==x)
			continue;
		if(mat[ind][i]!=-1)
			tot++,win+=mat[ind][i];
	}
	return 1.*win/tot;
}

double compOWP(int ind)
{
	double r=0,tot=0;
	rep(i,0,n)
	{
		if(mat[ind][i]!=-1)
		{
			r+=compWP(i,ind);
			tot++;
		}
	}
	return r/tot;
}

double compOOWP(int ind)
{
	double r=0,tot=0;
	rep(i,0,n)
	{
		if(mat[ind][i]!=-1)
			r+=OWP[i],tot++;
	}
	return r/tot;
}

int main()
{
	freopen("1.txt","rt",stdin);
	freopen("2.txt","wt",stdout);

	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d ",&n);
		rep(i,0,n)
			gets(a[i]);
		rep(i,0,n)
		{
			rep(j,0,n){
				if(a[i][j]=='1')
					mat[i][j]=1;
				else if(a[i][j]=='0')
					mat[i][j]=0;
				else
					mat[i][j]=-1;
			}
		}
		rep(i,0,n)
			WP[i]  = compWP(i);
		rep(i,0,n)
			OWP[i] = compOWP(i);
		rep(i,0,n)
			OOWP[i] = compOOWP(i);
		rep(i,0,n)
			res[i]= .25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
		printf("Case #%d:\n",tt+1);
		rep(i,0,n)
			printf("%.12lf\n",res[i]);
	}

	return 0;
}
