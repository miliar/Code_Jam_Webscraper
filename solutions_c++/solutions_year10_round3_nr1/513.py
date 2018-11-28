#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>
using namespace std;
struct node{
	int a,b;
	int hia,hib;
	node(int aa=0,int bb=0,int cc=0,int dd=0){
		a=aa;b=bb;hia=cc;hib=dd;
	}
};
bool operator<(const node& p,const node& q)
{
	if(p.a!=q.a)
		return p.a<q.a;
	if(p.b!=q.b)
		return p.b<q.b;
	if(p.hia!=q.hia)
		return p.hia<q.hia;
	return p.hib<q.hib;
}
int ha[1010],hb[1010];
set<node> s1;
int gcd(int n,int m)
{
	while(n!=0){
		int t=n;
		n=m%n;
		m=t;
	}
	return m;
}
inline int myabs(int num)
{
	return num>0?num:-num;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		int n;
		scanf("%d",&n);
		int i,j;
		for(i=1;i<=n;i++){
			scanf("%d%d",&ha[i],&hb[i]);
		}
		s1.clear();
		int ans=0;
		for(i=1;i<n;i++)
			for(j=i+1;j<=n;j++)
			{
				if((ha[i]-ha[j])*(hb[i]-hb[j])<0){
					node p;
					p.a=myabs(ha[i]-ha[j]);
					p.b=myabs(hb[i]-hb[j]);
					int d=gcd(p.a,p.b);
					p.a/=d;p.b/=d;
					int ti=i,tj=j;
					if(ha[ti]<ha[tj]){
						int tt=ti;
						ti=tj;
						tj=tt;
					}
					p.hia=(p.a+p.b);
					p.hib=myabs(hb[tj]-ha[tj]);
					d=gcd(p.hia,p.hib);
					p.hia/=d;p.hib/=d;
					p.hib+=p.hia*ha[tj];
					if(s1.find(p)==s1.end()){
						ans++;
						s1.insert(p);
					}
				}
			}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

