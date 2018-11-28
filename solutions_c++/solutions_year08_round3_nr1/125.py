#include<stdio.h>
#include<iostream.h>
long long p,k,l,i,a[10009],sum,j,key,num;
long cas,cas1;

int main()
{
    
////freopen("a_la.txt","r",stdin);
/////freopen("A_large_out.in","w",stdout);    

cin>>cas;

for(cas1=1;cas1<=cas;cas1++)
    {
  cin>>k>>p>>l;                        
    for(i=0;i<l;i++)
    cin>>a[i];
printf("Case #%ld: ",cas1);
    
    if(p*k<l)
    printf("Impossible\n");
    else
    {
    for(i=0;i<l-1;i++)
    for(j=0;j<l-i-1;j++)
    if(a[j]<a[j+1])
    {
    a[l]=a[j];
    a[j]=a[j+1];
    a[j+1]=a[l];               
    }    
    key=1;
    num=p;
    sum=0;
    for(i=0;i<l;i++)
    {
    sum+=key*a[i];
    num--;                
    if(num==0)
    {
    num=p;
    key++;          
    }          
    }    
    cout<<sum<<endl;    
        
    }
                            
                            
    }
    
return 0;    
}
