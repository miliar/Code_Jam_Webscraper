#include<iostream>
#include<cstring>
using namespace std;
int main()
{
   double n,d,g,i,j=1,t,temp;
   cin>>t;
   while(t--)
   {
    cin>>n>>d>>g;
    int flag=0;
    if((d>100 || g>100) ||(d<100 && g==100)){cout<<"Case #"<<j++<<": Broken\n";continue;} 
    if(d>0 && g==0){cout<<"Case #"<<j++<<": Broken\n";continue;}
    for(i=1;i<=n;i++)
    {
    temp=d/100*i;
    if(!(temp-int (temp)))
      {flag=1;
      //cout<<i<<endl;
      break;}
}  
    if(flag)
    cout<<"Case #"<<j++<<": Possible\n";
    else
    cout<<"Case #"<<j++<<": Broken\n";
    }               //while((d/100)*(i++)==1);
   
   //system("pause");
   return 0;
}
