#include<cstdio>
#include<limits.h>
#include<string>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
   freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,max1,z=0;
  scanf("%d",&t);
  while(t--)
  {
            z++;
            char a[4][4];
            int i,j,flag=0;
            for(i=0;i<4;i++)
            {
                            for(j=0;j<4;j++)
                            cin>>a[i][j];
            }
            for(i=0;i<4;i++)
            {
            if((a[i][0]=='X' ||a[i][0]=='T') && (a[i][1]=='X' ||a[i][1]=='T') && (a[i][2]=='X' ||a[i][2]=='T') && (a[i][3]=='X' ||a[i][3]=='T'))
            {flag =1;}
            else if((a[i][0]=='O' ||a[i][0]=='T') && (a[i][1]=='O' ||a[i][1]=='T') && (a[i][2]=='O' ||a[i][2]=='T') && (a[i][3]=='O' ||a[i][3]=='T'))
            {flag =2;}
            if((a[0][i]=='X' ||a[0][i]=='T') && (a[1][i]=='X' ||a[1][i]=='T') && (a[2][i]=='X' ||a[2][i]=='T') && (a[3][i]=='X' ||a[3][i]=='T'))
            {flag =1;}
            if((a[0][i]=='O' ||a[0][i]=='T') && (a[1][i]=='O' ||a[1][i]=='T') && (a[2][i]=='O' ||a[2][i]=='T') && (a[3][i]=='O' ||a[3][i]=='T'))
            {flag =2;}
            }
            if((a[0][0]=='O' ||a[0][0]=='T') && (a[1][1]=='O' ||a[1][1]=='T') && (a[2][2]=='O' ||a[2][2]=='T') && (a[3][3]=='O' ||a[3][3]=='T'))
            {;flag =2;}
            else if((a[0][0]=='X' ||a[0][0]=='T') && (a[1][1]=='X' ||a[1][1]=='T') && (a[2][2]=='X' ||a[2][2]=='T') && (a[3][3]=='X' ||a[3][3]=='T'))
            {flag =1;}
            if((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' ||a[2][1]=='T') && (a[3][0]=='O' ||a[3][0]=='T'))
            {flag =2;}
            else if((a[0][3]=='X' ||a[0][3]=='T') && (a[1][2]=='X' ||a[1][2]=='T') && (a[2][1]=='X' ||a[2][1]=='T') && (a[3][0]=='X' ||a[3][0]=='T'))
            {flag =1;}
            if(flag==1)
            cout<<"Case #"<<z<<": X won\n";
            if(flag==2)
            cout<<"Case #"<<z<<": O won\n";
            if(flag==0)
            {
                       for(i=0;i<4;i++)
                       {
                                       for(j=0;j<4;j++)
                                       {
                                                       if(a[i][j]=='.')
                                                       {flag=1;
                                                       break;}
                                       }
                                       if(flag==1)
                                       break;
                       }
                       if(flag==1)
                       cout<<"Case #"<<z<<": Game has not completed\n";
                       else
                       cout<<"Case #"<<z<<": Draw\n";
            }
  }
  return 0;
}
