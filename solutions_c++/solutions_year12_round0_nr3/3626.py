#include<iostream>
#include<math.h>
using namespace std;
int main()
{
        int a,b,A[4],i,ncases,x,c,j,temp[4],k,l,m,count=0,cases=0;
        cin>>ncases;
        while(ncases--)
        {
                count=0;
                scanf("%d%d",&a,&b);
                x=a;
                c=1;
                cases++;
                while(x/10!=0)
                {
                        c++;
                        x=x/10;
                }
                l=pow(10,c-1);
                for(i=a;i<=b;i++)
                {
                                x=i;
                                for(j=c-1;j>=0;j--)
                                {
                                        A[j]=x%10;
                                        x/=10;
 
                                }
                                for(k=0;k<c-1;k++)
                                {
                                        m=l;
                                        temp[k]=0;
                                        for(j=k+1;j<c;j++)
                                        {
                                                temp[k]+=(A[j]*m);
                                                m=m/10;
                                        }
 
                                        for(j=0;j<k+1;j++)
                                        {
                                                temp[k]+=(A[j]*m);
                                                m=m/10;
                                        }
 
 
                                }
                                for(k=0;k<c-1;k++)
                                {
                                        for(j=k+1;j<c-1;j++)
                                        {
                                                if(temp[j]==temp[k])
                                                temp[j]=0;
                                        }
                                        if((temp[k]>i)&&(temp[k]<=b))
                                        count++;
                                }
 
                }
                cout<<"\nCase #"<<cases<<": "<<count;
        }
        return 0;
}
 
