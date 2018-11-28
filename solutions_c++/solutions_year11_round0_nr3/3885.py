#include<iostream>
#include<fstream>
using namespace std;
int check(char t)
{
    if(t=='O')return 0;
    else return 1;
}
#define M ((1<<32)-1)
int main()
{
    fstream  fout;
    fout.open("1.txt",ios::out);
    int cas,N,l,data[20],i,j;
    cin>>cas;
    for(l=1;l<=cas;l++)
    {
               fout<<"Case #"<<l<<": ";
              // cout<<"Case #"<<l<<": ";
               cin>>N;
               int sum=0;
               for(i=0;i<N;i++)
               {
                                    cin>>data[i];
                                    sum^=data[i];
                                    }
            //   cout<<sum;
               if(sum!=0)fout<<"NO"<<endl;
               else
               {
               
               int sum1=0,sum2=0,ma=0;
               for(i=1;i<(1<<N)-1;i++)
               {
                                    int nowm=0;
                                    for(j=0;j<N;j++)
                                    {
                                                    if(((1<<j)&i)!=0)
                                                    {
                                                                   sum1^=data[j];  
                                                                   nowm+=data[j];
                                                                     }
                                                                     else sum2^=data[j];
                                                    }
                                    
                                    
                                    if(sum1==sum2&&nowm>ma)
                                    {
                                                          // cout<<sum1<<' '<<sum2<<nowm<<' '<<i<<endl;
                                                           ma=nowm;
                                                           }
                                    }
               
               if(ma==0)fout<<"NO\n";
               else fout<<ma<<endl;
              // cout<<ma<<endl;
               }
             //  cout<<"Case #"<<l<<": "<<res<<endl;
    }
    fout.close();
   // cin>>i;
    return 0;
    
}
 
