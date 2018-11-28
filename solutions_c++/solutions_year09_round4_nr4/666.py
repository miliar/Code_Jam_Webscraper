#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;


int n;
char s[1000];
int val[1000];
struct point 
{
	double x,y,r;
}p[100];
double max(double a,double b) {return a>b?a:b;}
double dis(point a,point b) 
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca,kk=1;
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
		printf("Case #%d: ",kk++);
		if(n==1) printf("%lf\n",p[0].r);
		else if(n==2) printf("%lf\n",max(p[0].r,p[1].r));
		else 
		{
			double ans[10];
			int has=0;
			for(i=0;i<3;i++) for(j=i+1;j<3;j++) 
			ans[has++]=dis(p[i],p[j])+p[i].r+p[j].r;
			sort(ans,ans+has);
			printf("%lf\n",ans[0]/2);
		}
	}
	return 0;
}