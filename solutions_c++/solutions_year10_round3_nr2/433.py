#include<iostream>
using namespace std;
#include <math.h>


int main()
{
    
     freopen("out.txt","w",stdout);
   freopen("B-large.in", "r", stdin);
    int T;
cin>>T;

for(int I=1;I<=T;I++)
{
        double P,L,C;
        cin>>L>>P>>C;
        int cnt=0;
        while(P>L)
        {
                  P=ceil(P/C);
                  if(P>L)
                  cnt++;
        }
      //  cout<<cnt<<endl;
      if(cnt<1)
        cout<<"Case #"<<I<<": "<<cnt<<endl;
  //     else if(cnt==2)
    //    cout<<"Case #"<<I<<": "<<cnt<<endl;
        else
       cout<<"Case #"<<I<<": "<<ceil(log2 (cnt+1))<<endl;
}
 //   system("pause");
    return 0;
    
}
