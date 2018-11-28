#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
const int N = 1000007;
int k;
double pos[N];
const double eps = 1e-9;
double d,high,mid,low;
bool lzs(double r)
{
	int i;
	double p=pos[0]-r;
	for(i=1;i<k;i++)
	{
		if(pos[i]+r+eps<p+d)return false;
		if(pos[i]-r+eps<p+d)p=p+d;
		else p=pos[i]-r;
	}
	return true;
} 
int main()
{
	int t,i,c,ca=1,P,V;
	//freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",ca++);
		scanf("%d%lf",&c,&d);
		k=0;
		while(c--)
		{
			scanf("%d%d",&P,&V);
			while(V--)
			{
				pos[k++]=P;
			}
		}
		sort(pos,pos+k);
		low=0;high=10000;
		while(high-low>eps)
		{
			mid=(low+high)/2;
			if(lzs(mid))high=mid;
			else low=mid;
		}
		printf("%.9lf\n",low);
	}
}
