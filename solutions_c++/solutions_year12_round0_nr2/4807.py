#include<iostream>
#include<cmath>
#include<conio.h>
using namespace std;
int main()
{
    int a;
    cin>>a;
    for(int i=1;i<=a;i++)
    {
            int t[31],n,s,p,count=0;
            cin>>n;
            cin>>s;
            cin>>p;
            for(int j=1;j<=n;j++)
            cin>>t[j];
            for(int j=1;j<=n;j++)
            {
                    int fl,flag=0,flag2=0;
                    float div;
                    div=t[j]/3;
                    fl=floor(div);
                    for(int k=((fl-2)>0?(fl-2):0);k<=fl+2;k++)
                    {
                            for(int l=((fl-2)>0?(fl-2):0);l<=fl+2;l++)
                            {
                                    for(int m=((fl-2)>0?(fl-2):0);m<=fl+2;m++)
                                    {
                                                       if((k+l+m)==t[j]&&((k>=p)||(l>=p)||(m>=p))&&((fabs(k-l)<=1)&&(fabs(l-m)<=1)&&(fabs(k-m)<=1)))
                                                       {
                                                          if((flag==1)&&(flag2==1))
                                                          {
                                                          s++;
                                                          flag2=0;
                                                          }
                                                          if(flag==0)
                                                          {
                                                          count++;
                                                          flag=1;
                                                          }
                                                       }
                                                       else
                                                       if((k+l+m)==t[j]&&((k>=p)||(l>=p)||(m>=p))&&((fabs(k-l)<=2)&&(fabs(l-m)<=2)&&(fabs(k-m)<=2)) && (s!=0))
                                                       {
                                                          if(flag==0)
                                                          {
                                                          s--;
                                                          count++;
                                                          flag=1;
                                                          flag2=1;
                                                          }
                                                       }
                                    }
                            }
                    }
            }
            cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
