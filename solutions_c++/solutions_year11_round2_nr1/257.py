#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int n,T,Ti,m;

double d1a[110],d1b[110],d2[110],d3[110];
double eps=1e-3;
char r[110][110];

void xx()
{
	int i;
	for(i=0;i<100;i++)cout<<endl;
}
int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,c,d,j,k;
    double z,a,b;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%s",r[i]);
		
		for(i=0;i<n;i++)
		{
			d1a[i]=d1b[i]=0;
			for(j=0;j<n;j++)			
			{
				if(r[i][j]=='1')
				{
					d1a[i]+=1;
					d1b[i]+=1;					
			//		cout<<"---"<<i<<' '<<j<<endl;
				}
				if(r[i][j]=='0')
				{
					 d1b[i]+=1;				
			//		 cout<<"-0--"<<i<<' '<<j<<endl;
				}
			}
		//	cout<<"++++ "<<i<<' '<<d1a[i]<<' '<<d1b[i]<<endl;
		}
		
		for(i=0;i<n;i++)
		if(d1b[i]<eps)xx();
		
		for(i=0;i<n;i++)
		{
			z=0;b=0;
			for(j=0;j<n;j++)
			if(r[i][j]=='0' || r[i][j]=='1' )
			{
				if(r[j][i]=='1')
				{
					if(d1b[j]-1<eps)xx();
					z+=(d1a[j]-1)/(d1b[j]-1);
				}
				if(r[j][i]=='0')
				{
					if(d1b[j]-1<eps)xx();
					z+=(d1a[j])/(d1b[j]-1);
				}
				if(r[j][i]=='.')z+=d1a[j]/d1b[j];								
				b++;
			}			
			d2[i]=z/b;	
			if(b<eps)xx();		
		}
		
		for(i=0;i<n;i++)
		{
			a=0;b=0;
			for(j=0;j<n;j++)
			if(r[i][j]=='0' || r[i][j]=='1' )
			{
				a+=d2[j];
				b++;
			}
			d3[i]=a/b;
			if(b<eps)xx();
		}
		
	//	for(i=0;i<n;i++)cout<<d1a[i]<<' ';cout<<endl;cout<<endl;
///		for(i=0;i<n;i++)cout<<d1b[i]<<' ';cout<<endl;cout<<endl;
	//	for(i=0;i<n;i++)cout<<d2[i]<<' ';cout<<endl;cout<<endl;
	//	for(i=0;i<n;i++)cout<<d3[i]<<' ';cout<<endl;cout<<endl;
		
		putchar('\n');		
		for(i=0;i<n;i++)printf("%.12lf\n",0.25*d1a[i]/d1b[i] + 0.5*d2[i] + 0.25*d3[i]);
	}	
    return 0;
}
