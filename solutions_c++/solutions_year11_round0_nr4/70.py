#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
#include<math.h>
using namespace std;
int n,T,Ti;

double f[1010],jie[1010],d[1010],da;
int r[1010],v[1010];

int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,a,b,c,j,k;
    
    double z;
    int s;
    
    jie[1]=1;
    for(i=2;i<=1000;i++)jie[i]=jie[i-1]/double(i);
    
    f[1]=0;
    f[2]=0.5;
    for(i=3;i<=1000;i++)//fc[i]=(fc[i-2]+fc[i-1])*(i-1),cout<<fc[i]<<endl;;
    f[i]=f[i-2]/double(i)+f[i-1]*(i-1)/double(i);//,cout<<f[i]<<endl;
    
    d[1]=0;
    d[2]=2;
    
    for(i=3;i<=1000;i++)
    {
		z=jie[i]+f[i];
		for(j=1;j<=i-2;j++)z+=f[i-j]*(d[i-j]+1)*jie[j];
		d[i]=z/double(1.0-f[i]);
	}
	
/*	for(i=2;i<=1000;i++)
	if(fabs(d[i]-double(i))>1e-6)cout<<"---------"<<d[i]<<endl;*/
	
//	for(i=2;i<=1000;i++)d[i]=i;//cout<<d[i]<<endl;
	
	
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		scanf("%d",&n);
		for(i=1;i<=n;i++)scanf("%d",&r[i]),v[i]=1;//,cout<<r[i]<<' ';cout<<endl;
		
		da=0;
		
		for(i=1;i<=n;i++)
		if(v[i])
		{
			if(r[i]==i)continue;
			j=i;s=1;
			v[j]=0;
			while(1)
			{
				j=r[j];
				v[j]=0;
				s++;
				if(!v[r[j]])break;				
			}
			da+=d[s];
		//	cout<<"----"<<s<<endl;
		}
		printf("%.6lf\n",da);
	}	
    return 0;
}
