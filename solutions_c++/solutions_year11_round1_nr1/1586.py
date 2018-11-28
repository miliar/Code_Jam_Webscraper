#include<iostream>
using namespace std;
int main()
{
    double n,pg,pd,i,j;
    int flag1=0,flag2=0,cas=0,t;
    cin>>t;
    while(t--)
    {
    while(cin>>n>>pd>>pg)
    {
                         cas++;
                         i=n;
                         while(i)
                         {
                                 //cout<<((pd/100)*i)<<" "<<(int)((pd/100)*i)<<"\n";
                                 if(((pd/100)*i)==(int)((pd/100)*i))
                                {
                                
                                 flag1=1;
                                 //cout<<"i "<<i<<"\n";
                                 break;
                                 
                                 }
                                  // ;
                                 i--;
                                 }
                                 j=i;
                                 while(j)
                                 {
                                         if(((pg/100)*j)==(int)((pg/100)*j))
                                         {
                                         flag2=1;
                                   //      cout<<" j "<<j<<"\n";
                                         break;
                                         }
                                         //
                                         j++;
                                         }
                                         if(i==j)
                                         {
                                                 if(((pg/100)*j)==((pd/100)*i))
                                                 flag1=1;
                                                 else
                                                 flag1=0;
                                                 }
                                         if((flag1==1 && flag2==1) &&(((pd/100)*i)<=((pg/100)*j)) && i>0 && j>0)
                                         cout<<"Case #"<<cas<<": Possible\n";
                                         else
                                         cout<<"Case #"<<cas<<": Broken\n";
                                         flag1=0;flag2=0;
                         
                         }
                         }
    return 0;
    }
