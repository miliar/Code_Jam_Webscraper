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

struct Cor
{
	int from,to,speed;
	Cor(int a,int b,int c)
		:from(a),to(b),speed(c){}
	Cor(){}
	bool operator <(const Cor& a)const
	{
		return from < a.from;
	}
};

struct cmp
{
	bool operator ()(const Cor& a,const Cor& b)const
	{
		double l1 = a.to-a.from;
		double l2 = b.to-b.from;
		return a.speed<b.speed;
		//return l1/a.speed > l2/b.speed;
	}
};

Cor cor[2001];

int main()
{
	freopen("1.txt","rt",stdin);
	freopen("2.txt","wt",stdout);
	int t,X,S,R,mxt,n;
	int a,b,c;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d %d %d %d %d",&X,&S,&R,&mxt,&n);
		rep(i,0,n)
		{
			scanf("%d %d %d",&a,&b,&c);
			cor[i]=Cor(a,b,c);
		}
		sort(cor,cor+n);
		int fl=0;
		if(cor[0].from!=0){
			fl=1;
			cor[n++]=Cor(0,cor[0].from,0);
			if(cor[n-2].to!=X){
				Cor temp = Cor(cor[n-2].to,X,0);
				cor[n++]=temp;
			}
		}
		if(cor[n-1].to!=X&&!fl)
		{
			Cor temp = Cor(cor[n-1].to,X,0);
			cor[n++]=temp;
		}
		sort(cor,cor+n);
		int sz = n;
		rep(i,1,sz)
		{
			if(cor[i-1].to!=cor[i].from)
				cor[n++]=Cor(cor[i-1].to,cor[i].from,0);
		}
		sort(cor,cor+n,cmp());
		double rem = mxt;
		double res = 0;
		rep(i,0,n)
		{
			double l = cor[i].to - cor[i].from;
			double sp = cor[i].speed;
			double nsp = cor[i].speed+R;
			double nt = l/nsp;
			if(nt>rem)
			{
				res+=rem;
				res+= (l-(rem*(cor[i].speed+R)))/(cor[i].speed+S);
				rem=0;
			}else
			{
				res+=nt;
				rem-=nt;
			}
		}
		printf("Case #%d: %.10lf\n",tt+1,res);
	}
	return 0;
}
