#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main()
{
  int nt;
  cin>>nt;
  
  for(int p=1;p<=nt;p++)
  {
    int nos;
    cin>>nos;
     char c; int d;
     int i,j;
     i=j=0;
     int tot;
     int curO,curB;
     curO=curB=1;
     while(nos--)
     {
       cin>>c>>d;
       if(c=='O'){
         i=max(i+(int)abs((float)curO-d),j)+1;
          curO=d;
         }
       if(c=='B'){
         j=max(j+(int)abs((float)curB-d),i)+1;
         curB=d;
        }
     }
    cout<<"Case #"<<p<<": "<<max(i,j)<<endl;
  }  
}



