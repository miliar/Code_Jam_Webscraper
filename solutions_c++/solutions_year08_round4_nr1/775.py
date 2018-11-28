#include<stdio.h>

long cas,cas1,m,v,i,a[10009],b[10009];
long v0[10009],v1[10009],flag,t1,t2,t;
long left,right;

int main()
{
    
////freopen("A-large.in","r",stdin);
////freopen("A_l.out","w",stdout);    

scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%ld %ld",&m,&v);
for(i=0;i<(m-1)/2;i++)
{
scanf("%ld %ld",&a[i],&b[i]);                      
}

for(i=(m-1)/2;i<m;i++)
{
scanf("%ld",&t);                      
if(t==0)                      
{v0[i]=0; v1[i]=2*m;}
else
{v0[i]=2*m; v1[i]=0;}                                            
}

for(i=(m-1)/2-1;i>=0;i--)
{
                         

v0[i]=2*m;
v1[i]=2*m;
left=i*2+1;
right=i*2+2;
if(left>=m)
continue;
else if(right>=m)
{
v0[i]=v0[left];
v1[i]=v1[left];     
}

if(a[i]==1)
{
if(v1[left]+v1[right]<v1[i])
v1[i]=v1[left]+v1[right];
if(v1[left]+v0[right]<v0[i])
v0[i]=v1[left]+v0[right];
if(v0[left]+v1[right]<v0[i])
v0[i]=v0[left]+v1[right];
if(v0[left]+v0[right]<v0[i])
v0[i]=v0[left]+v0[right];
           
if(b[i]==1)
{
if(v0[left]+v0[right]+1<v0[i])
v0[i]=v0[left]+v0[right]+1;
if(v0[left]+v1[right]+1<v1[i])
v1[i]=v0[left]+v1[right]+1;
if(v1[left]+v0[right]+1<v1[i])
v1[i]=v1[left]+v0[right]+1;
if(v1[left]+v1[right]+1<v1[i])
v1[i]=v1[left]+v1[right]+1;           
}
}
else
{
if(v0[left]+v0[right]<v0[i])
v0[i]=v0[left]+v0[right];
if(v0[left]+v1[right]<v1[i])
v1[i]=v0[left]+v1[right];
if(v1[left]+v0[right]<v1[i])
v1[i]=v1[left]+v0[right];
if(v1[left]+v1[right]<v1[i])
v1[i]=v1[left]+v1[right];
if(b[i]==1)
{
if(v1[left]+v1[right]+1<v1[i])
v1[i]=v1[left]+v1[right]+1;
if(v1[left]+v0[right]+1<v0[i])
v0[i]=v1[left]+v0[right]+1;
if(v0[left]+v1[right]+1<v0[i])
v0[i]=v0[left]+v1[right]+1;
if(v0[left]+v0[right]+1<v0[i])
v0[i]=v0[left]+v0[right]+1;           
}   
}                         
}

flag=2*m;

if(v==0)
flag=v0[0];
else
flag=v1[0];                            
           
           if(flag>m)
           printf("Case #%ld: IMPOSSIBLE\n",cas1);
           else
           printf("Case #%ld: %ld\n",cas1,flag);                 
                            
}
}
