#include <iostream>
#include <fstream>
using namespace std;



int C;
int R;
bool flag[2][110][110];
int ans;
int total;
int optr,nptr;

int main()
{
    ifstream fin("Csmall.in");
    ofstream fou("Csmall.out");
    fin>>C;
    for (int c=0;c<C;c++)
    {
      fin>>R;
      int X1,Y1,X2,Y2;
      for (int i=0;i<=100;i++)
        for (int j=0;j<=100;j++) flag[0][i][j]=flag[1][i][j]=false;
      total =0;ans = 0;
      for (int i=1;i<=R;i++)
      {
        fin>>Y1>>X1>>Y2>>X2;
        for (int px=min(X1,X2);px<=max(X1,X2);px++)
          for (int py=min(Y1,Y2);py<=max(Y1,Y2);py++)
          {if (flag[0][px][py]==0) total++;flag[0][px][py]=1;}
      }
      nptr=1;optr=0;
      while (total>0)
      {
     //   cout<<total<<endl;
     /*   for (int i=1;i<=80;i++)
        { for (int j=1;j<=80;j++)
        cout<<flag[optr][i][j];cout<<endl;
        }
        system("pause");
        */
        ans++;
        for (int i=1;i<=100;i++)
          for (int j=1;j<=100;j++)
          if (flag[optr][i][j]==0)
          {
            if (flag[optr][i-1][j]&&(flag[optr][i][j-1]))
            {flag[nptr][i][j]=1;total++;}
            else flag[nptr][i][j]=0;
          }
          else
          {
             if ((!flag[optr][i-1][j])&&(!flag[optr][i][j-1]))
             {flag[nptr][i][j]=0;total--;}
             else flag[nptr][i][j]=1;
          }
        nptr=(nptr+1)%2;
        optr=(optr+1)%2;
      }
      fou<<"Case #"<<c+1<<": "<<ans<<endl;
    }
    fin.close();
    fou.close();
    return 0;
}
