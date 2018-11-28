#include<iostream>
#include<math.h>

int power(int n,int j)
{
    int p=1,i;
    for(i=0;i<j;i++)
    p=p*n;
    return p;
}
    
using namespace std;
int main()
{
    int t,n,m,temp,g,count,n1,c,i,j,z;
    scanf("%d",&t);
    z=t;
    while(t--)
    {
              scanf("%d %d",&n,&m);
              count=0;
           //   cout<<n<<endl;
              for(i=n;i<m;i++)
              {
                               c=0;
                               temp=i;
                               if((i%10)>=0)
                               {
                               while(temp>0)
                               {
                                            c++;
                                            temp=temp/10;
                               }
                               g=power(10,c);
     //                          cout<<c<<" "<<g<<endl;
                               for(j=1;j<c;j++)
                               {
                                               temp=power(10,j);
                //                              cout<<"temp = "<<temp<<endl;
                                               n1=((i%temp)*(g/temp))+(i/temp);
   //                                            cout<<n1<<"\n";
                                               if(n1>i && n1<=m)
                                {              count++;
//                               cout<<" n is "<<i<<" " <<n1<<endl;
                                //j=c+1;
                                }
                               }
                               }
              }
              printf("Case #%d: %d\n",z-t,count);
    }
    return 0;
}
                               
                                    
                                              
                                       
              
