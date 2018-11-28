#include<stdio.h>
#include<cstdlib>
#include<string.h>
#include<stdlib.h>
const int mxn=1500;
int C,A,B,P;
int f[mxn];
int p[mxn],rank[mxn],ct=0;
int gcd(int x,int y)
{
    if(y==0) return x;       
    return gcd(y,x%y);
}
int big(int x,int y)
{
    int ans=1;    
    int m=gcd(x,y);
    int i=2;
    while(m>1)
    {
         int sum=0;          
         while(!(m%i))
         {
              m/=i;             
              sum++;        
         }     
         if(sum)
         ans=i;
         i++;
         if(i*i>m)break;
              
    }
    if(m>1) ans=m;
    return ans;
}

void makeset(int x)
{
	rank[x]=0;
	p[x]=x;
	ct++;
}
void init()
{
	ct=0;
	memset(p,0,sizeof(p));
	memset(rank,0,sizeof(rank));
}
int findset(int x)
{
	int px=x,i;
	while (px!=p[px]) px=p[px]; 
	while (x!=px)
	{
		i=p[x];
		p[x]=px;
		x=i;
	}
	return px;
}

void unionset (int x , int y)
{
	ct--;
	if( rank[x] > rank[y]) p[y]=x;
	else
	{
		p[x]=y;
		if( rank[x]==rank[y]) rank[y]++;
	}
}
FILE *fout;
int main()
{
    fout=fopen("a.out","w");
    scanf("%d",&C);
    int index;
    for(index=1;index<=C;index++)
    {
        fprintf(fout,"Case #%d: ",index);
        scanf("%d%d%d",&A,&B,&P);                             
        int i,j;
        init();
        for(i=A;i<=B;i++) makeset(i);
        for(i=A;i<=B;i++)
        {
            for(j=i+1;j<=B;j++)
            if(big(j,i)>=P)
            {
               int l1,l2;
               l1=findset(i);
               l2=findset(j);
               if(l1!=l2)
               unionset(l1,l2);
               
            }                          
        }                         
        fprintf(fout,"%d\n",ct);                         
    }
    
system("pause");
return 0;    
}
