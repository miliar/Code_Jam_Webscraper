#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
   
    int t,c=0,f,g,i,j;
    cin>>t;
    while(t--)
    {
              c++;
              string s[4],s1[4],s2[4];
              f=0,g=0;
              for(i=0;i<4;i++)
              {
              cin>>s[i];
              s1[i]=s[i];
              s2[i]=s[i];
              }
              for(i=0;i<4;i++)
              {
                      for(j=0;j<4;j++)
                      {
                              if(s[i][j]=='T')
                              {
                              s1[i][j]='X';
                              s2[i][j]='O';
                              }
                              if(s[i][j]=='.')
                              g=1;
                      }
              }
              for(i=0;i<4;i++)
              {
                      if((s1[i][0]==s1[i][1] && s1[i][1]==s1[i][2] && s1[i][2]==s1[i][3] && s1[i][0]=='X') || (s1[0][i]==s1[1][i] && s1[1][i]==s1[2][i] && s1[2][i]==s1[3][i] && s1[0][i]=='X'))
                      f=1;
                      else if((s2[i][0]==s2[i][1] && s2[i][1]==s2[i][2] && s2[i][2]==s2[i][3] && s2[i][0]=='O') || (s2[0][i]==s2[1][i] && s2[1][i]==s2[2][i] && s2[2][i]==s2[3][i] && s2[0][i]=='O'))
                      f=2;
              }
              if(f==0)
              {
                      if((s1[0][0]==s1[1][1] && s1[1][1]==s1[2][2] && s1[2][2]==s1[3][3] && s1[0][0]=='X') || (s1[0][3]==s1[1][2] && s1[1][2]==s1[2][1] && s1[2][1]==s1[3][0] && s1[3][0]=='X'))
                      f=1;
                      else if((s2[0][0]==s2[1][1] && s2[1][1]==s2[2][2] && s2[2][2]==s2[3][3] && s2[0][0]=='O') || (s2[0][3]==s2[1][2] && s2[1][2]==s2[2][1] && s2[2][1]==s2[3][0] && s2[3][0]=='O'))
                      f=2;
              }
              cout<<"Case #"<<c<<": ";
              if(f==1)
              cout<<"X won"<<endl;
              else if(f==2)
              cout<<"O won"<<endl;
              else if(g==0)
              cout<<"Draw"<<endl;
              else
              cout<<"Game has not completed"<<endl;
    }
   // system("pause");
    return 0;
}
 
