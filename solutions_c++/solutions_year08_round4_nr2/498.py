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
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int n,m,N,M,P,T,K,A;

int main()
{
    scanf("%d",&T);
    for (int id=1;id<=T;id++)
    {
		scanf("%d%d%d",&N,&M,&A);
		//cout<<"-----------------CASE "<<id<<endl;
		int dx1,dy1; double num,den; double dx2,dy2;
		for (int x=0;x<=N;x++) //swap and y=x...
		 for (int y=0;y<=M;y++)
		  {
			/*	dx1=x,dy1=-y;
				if (dx1)
				 {
				   num=A*dx1; den=dx1*dx1+dy1*dy1;
				  // if (num%den) goto sux;
				   dy2=(double)num/den;
				   num=-dy1*dy2;
				  // if (num%dx1) goto sux;
				   dx2=(double)num/dx1;
				 }
				else if (dy1)
				 {
				   num=A*dy1; den=dx1*dx1+dy1*dy1;
				 //  if (num%den) goto sux;
				   dx2=(double)num/den;
				   num=-dx1*dx2;
				  // if (num%dy1) goto sux;
				   dy2=(double)num/dy1;
				 }
				else goto sux;
				if (dx2<=0 && dy2<=0) dx2=-dx2,dy2=-dy2;
				cout<<"   "<<x<<" "<<y<<" - "<<dx2<<" "<<dy2<<" ("<<dx1<<" "<<dy1<<")"<<endl;
				sux:;*/
				for (int x1=0;x1<=N;x1++)
				 for (int y1=0;y1<=M;y1++)
				  if (abs(x*(y1-y)-x1*(-y))==A)
				   {
						printf("Case #%d: %d 0 0 %d %d %d\n",id,x,y,x1,y1);
						goto next;
				   }
		  }
	  printf("Case #%d: IMPOSSIBLE\n",id); 
	  next:;
	}
    return 0;
}
