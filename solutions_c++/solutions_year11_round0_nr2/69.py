#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
using namespace std;
int n,T,Ti,da;

map<string,char> fm;
map<string,char>::iterator it;
map<string,bool> fm2;
map<string,bool>::iterator it2;

char rs[1100],d[1100];
int dn;


int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,a,b,c,j,k,z;
    
    string zs;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		fm.clear();fm2.clear();dn=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",rs);
			zs=rs[0];
			zs+=rs[1];
			fm[zs]=rs[2];
			zs=rs[1];
			zs+=rs[0];
			fm[zs]=rs[2];
		}
		
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",rs);
			zs=rs[0];
			zs+=rs[1];
			fm2[zs]=1;
			zs=rs[1];
			zs+=rs[0];
			fm2[zs]=1;
		}
		
		dn=0;
		
		scanf("%d%s",&n,rs);
		for(i=0;rs[i];i++)
		{
			if(dn==0)
			{
				d[dn++]=rs[i];
				continue;
			}
			zs=d[dn-1];
			zs+=rs[i];
			it=fm.find(zs);
			if(it!=fm.end())
			{
				d[dn-1]=it->second;
				continue;
			}
			
			for(j=0;j<dn;j++)
			{
				zs=d[j];
				zs+=rs[i];
				it2=fm2.find(zs);			
				if(it2!=fm2.end())
				{
					dn=0;
	//				cout<<"----"<<zs<<"----";
					break;
				}			
			}
			
			if(dn==0)continue;
			
			d[dn++]=rs[i];
		}
		printf("[");
		for(i=0;i<dn;i++)
		{
			putchar(d[i]);
			if(i<dn-1)printf(", ");
		}
		printf("]\n");		
	}	
    return 0;
}
