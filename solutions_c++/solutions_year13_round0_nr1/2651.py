
/*
Author Name::Himanshu Tomar
Lang::C++
*/

// header files

#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cassert>
#include<utility>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<conio.h>
#include<iomanip>
#include<map>
#include<set>
#include<ctime>
#include<cstring>
#include<cmath>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

// definitions

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define ppb() pop_back()
#define ll long long int
#define s(a) scanf("%d",&a)
#define clr(x) memset(x,0,sizeof(x))
#define bs(a,b,c) binary_search(a,b,c)
#define ub(a,b,c) upper_bound(a,b,c)
#define lb(a,b,c) lower_bound(a,b,c)
#define mod 1000000007
using namespace std;

void init()
{}

int main()
{
     freopen("C:\\Users\\JI\\Desktop\\input.txt","r",stdin);
     freopen("C:\\Users\\JI\\Desktop\\output.txt","w",stdout);
      char arr[4][10];
      int in=1;
      int tc;
      s(tc);
      getchar();
      while(tc--)
      {
                 bool flag=false;
                 bool flag2=false;
                 for(int i=0;i<4;i++)
                 {
                        
                         cin>>arr[i];
                          getchar();
                 }
                 
                 int count_x=0,cx=0,count_o=0,co=0,count_t=0,ct=0;
                 for(int i=0;i<4;i++)
                 {
                         if(arr[i][i]=='X')
                         count_x++;
                         if(arr[i][i]=='O')
                         count_o++;
                         else if(arr[i][i]=='T')
                         count_t++;
                         
                         if(arr[3-i][i]=='X')
                         cx++;
                         if(arr[3-i][i]=='O')
                         co++;
                         else if(arr[3-i][i]=='T')
                         ct++;
                 }
                 
                 if(count_x+count_t==4 or cx+ct==4)
                 {cout<<"Case #"<<in<<": "<<"X won"<<endl;in++;continue;}
                 
                 if(count_o+count_t==4 or co+ct==4)
                 {cout<<"Case #"<<in<<": "<<"O won"<<endl;in++;continue;}
                 
                 cx=0;co=0;ct=0,count_x=0,count_o=0,count_t=0;
                 int cdot=0;
                 
                 for(int i=0;i<4;i++)
                 {
                         cx=co=ct=count_x=count_t=count_o=0;
                         for(int j=0;j<4;j++)
                 {
                          
                                if(arr[i][j]=='X')
                                cx++;
                                
                                if(arr[i][j]=='O')
                                co++;
                                
                                if(arr[i][j]=='T')
                                ct++;
                                
                                if(arr[i][j]=='.' or arr[j][i]=='.')
                                cdot++;
                         
                                if(arr[j][i]=='X')
                                count_x++;
                                
                                if(arr[j][i]=='O')
                                count_o++;
                                
                                else if(arr[j][i]=='T')
                                count_t++;
                                
                         }
                         
                         if(cx+ct==4 or count_x+count_t==4)
                         {cout<<"Case #"<<in<<": "<<"X won"<<endl;flag=true;break;}
                         
                         if(co+ct==4 or count_o+count_t==4)
                         {cout<<"Case #"<<in<<": "<<"O won"<<endl;flag=true;break;}
                         
                         }
                         
                         if(!flag)
                         {
                         if(cdot>0)
                         cout<<"Case #"<<in<<": "<<"Game has not completed"<<endl;
                         else
                         cout<<"Case #"<<in<<": "<<"Draw"<<endl;
                         }
                         in++;
                 }
                 getch();
      return 0;
}
