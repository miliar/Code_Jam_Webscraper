#include<iostream>
using namespace std;
int main()
{
    int A,B,i,j,t,flag=0,k=1,x,y,pow,c,cas;
    cin>>t;
    cas=t;
    while(t--)
    {
              cin>>A;
              cin>>B;
              c=0;
              for(i=A;i<B;i++)
              {
                              for(j=i+1;j<=B;j++)
                              {
                                                 k=1;
                                                 flag=0;
                                                 x=i;
                                                 y=j;
                                                 if((y>=1)&&(y<=9))
                                                 pow=1;
                                                 else if((y>=10)&&(y<=99))
                                                 pow=10;
                                                 else if((y>=100)&&(y<=999))
                                                 pow=100;
                                                 if((i==9)||(i==99)||(i==999))
                                                 break;
                                                 while(k<=3)
                                                 {
                                                        k++;
                                                        if(x==y)
                                                        {
                                                        flag=1;
                                                        break;
                                                        }
                                                        y=y/10+((y%10)*pow);
                                                 }
                                                 if(flag==1)
                                                 c++;
                              }
              }
cout<<"Case #"<<(cas-t)<<": "<<c<<"\n";
}
}
