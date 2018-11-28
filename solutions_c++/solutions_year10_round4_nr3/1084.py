#include <iostream>

using namespace std;

int tc,R,x1,y1,x2,y2;
int tot,ans;
bool ar[2][111][111];

int main()
{
    cin >> tc;
    for(int tt=0;tt<tc;tt++)
    {
     cin >> R;
     memset(ar,0,sizeof(ar));
     tot = 0;
     ans = 0;
     
     for(int i=0;i<R;i++)
      {
       cin >> x1 >> y1 >> x2 >> y2;
       for(int ii=x1;ii<=x2;ii++)
        for(int iii=y1;iii<=y2;iii++)
        {if(!ar[0][iii][ii])tot++;ar[0][iii][ii] = true; }
      }
      
      while(tot>0)
      {
       ans++;
       for(int i=1;i<=100;i++)
        for(int ii=1;ii<=100;ii++)
        {
        ar[1][i][ii] = ar[0][i][ii];
        if(!ar[0][i][ii] && ar[0][i-1][ii] && ar[0][i][ii-1]) {ar[1][i][ii] = true;tot++;}
        if(ar[0][i][ii] && !ar[0][i-1][ii] && !ar[0][i][ii-1]) {ar[1][i][ii] = false;tot--;}
        }
       
        for(int i=0;i<=100;i++)
         for(int ii=0;ii<=100;ii++)
         ar[0][i][ii] = ar[1][i][ii];
      }
     
     
     cout << "Case #" << tt+1 << ": ";
     cout << ans << endl;
    }
}
