#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include<string.h>
#define MAX 3050
using namespace std;

int main()
{
      ifstream cin("A-large.in");
      ofstream cout ("output.txt");
      int t,r=1;
      cin>>t;
      while(t--)
      {
            cout<<"Case #"<<r++<<": ";
            string s1[4];
            for(int i=0;i<4;i++)
            {
                  cin>>s1[i];
            }
           int flag=0,f2=0;
            for(int i=0;i<4 && flag==0;i++)
            {
                   int r1=0,r2=0,r3=0,r4=0;
                   for(int j=0;j<4;j++)
                   {
                        if(s1[i][j]=='T')
                        r1++,r2++;
                        else if(s1[i][j]=='X')
                        r1++;
                        else if(s1[i][j]=='O')
                        r2++;
                        else
                        f2=1;
                        if(s1[j][i]=='T')
                        r3++,r4++;
                        else if(s1[j][i]=='X')
                        r3++;
                        else if(s1[j][i]=='O')
                        r4++;
                   }
                   if(r1==4 || r3==4)
                   {
                        cout<<"X won"<<endl;
                        flag=1;
                   }
                   else if(r2==4 || r4==4)
                   cout<<"O won"<<endl,flag=1;
            }
            if(flag==1)
            continue;
            int r1=0,r2=0,r3=0,r4=0;
            for(int i=0;i<4;i++)
            {
                  if(s1[i][i]=='T')
                        r1++,r2++;
                        else if(s1[i][i]=='X')
                        r1++;
                        else if(s1[i][i]=='O')
                        r2++;
                        if(s1[3-i][i]=='T')
                        r3++,r4++;
                        else if(s1[3-i][i]=='X')
                        r3++;
                        else if(s1[3-i][i]=='O')
                        r4++;
                  
            }
             if(r1==4 || r3==4)
                   {
                        cout<<"X won"<<endl;
                        flag=1;
                   }
                   else if(r2==4 || r4==4)
                   cout<<"O won"<<endl,flag=1;
            if(flag==0 && f2==1 )
            {
            cout<<"Game has not completed"<<endl;
            }
            else if(flag==0 && f2==0)
            cout<<"Draw"<<endl;
      }
      return 0;
}
