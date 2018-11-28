#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int n,T,Ti,da;

struct cla
{
	char a[10];
	int b;
}r[110];

int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,a,b,c,d,j,k,z;
    
    int ai,bi;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s%d",r[i].a,&r[i].b);
			
		a=b=1;
		da=0;
		for(i=0;i<n;i++)
		{
			ai=bi=-1;
			for(j=i;j<n;j++)
			if(r[j].a[0]=='O'){ai=r[j].b;break;}
			for(j=i;j<n;j++)
			if(r[j].a[0]=='B'){bi=r[j].b;break;}
			
		//	cout<<da<<' '<<ai<<' '<<bi<<' '<<a<<' '<<b<<endl;
			if(r[i].a[0]=='O')
			{
				z=abs(r[i].b-a)+1;
				da+=z;
				a=r[i].b;
				if(bi==-1)continue;
				if(abs(bi-b)<=z)b=bi;
				else
					if(b<bi)b+=z;
					else b-=z;				
				continue;
			}
			
			z=abs(r[i].b-b)+1;
				b=r[i].b;
				da+=z;
				if(ai==-1)continue;
				if(abs(ai-a)<=z)a=ai;
				else
					if(a<ai)a+=z;
					else a-=z;				
		}
		
		printf("%d\n",da);
	}	
    return 0;
}
