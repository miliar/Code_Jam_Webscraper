#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>

#define X first
#define Y second
#define ll long long

using namespace std;
char s[6][6];
void solve()
{
     for (int i=0; i<4; i++)
         cin>>s[i];
     
     for (int i=0; i<4; i++)
     {
         
         bool fl=1;
         for (int j=0; j<4; j++)
         {
             if ( s[i][j]!='X' && s[i][j]!='T' )
                fl=0;
         }    
         if ( fl==1 )
         {
            cout<<"X won"<<endl;
            return ;     
         }
     }
     
     for (int i=0; i<4; i++)
     {
         
         bool fl=1;
         for (int j=0; j<4; j++)
         {
             if ( s[j][i]!='X' && s[i][j]!='T' )
                fl=0;
         }    
         if ( fl==1 )
         {
            cout<<"X won"<<endl;
            return ;     
         }
     }
     bool g1x=1, g2x=1;
     for (int i=0; i<4; i++)
         if ( s[i][i]!='X' && s[i][i]!='T' )
            g1x=0;
     for (int i=0; i<4; i++)
         if ( s[3-i][i]!='X' && s[3-i][i]!='T' )
            g2x=0;
     if ( g1x || g2x )
     {
        cout<<"X won"<<endl;
        return ;
     }
     for (int i=0; i<4; i++)
     {
         
         bool fl=1;
         for (int j=0; j<4; j++)
         {
             if ( s[i][j]!='O' && s[i][j]!='T' )
                fl=0;
         }    
         if ( fl==1 )
         {
            cout<<"O won"<<endl;
            return ;     
         }
     }
     
     for (int i=0; i<4; i++)
     {
         
         bool fl=1;
         for (int j=0; j<4; j++)
         {
             if ( s[j][i]!='O' && s[i][j]!='T' )
                fl=0;
         }    
         if ( fl==1 )
         {
            cout<<"O won"<<endl;
            return ;     
         }
     }
     
     bool g1o=1, g2o=1;
     for (int i=0; i<4; i++)
         if ( s[i][i]!='O' && s[i][i]!='T' )
            g1o=0;
     for (int i=0; i<4; i++)
         if ( s[3-i][i]!='O' && s[3-i][i]!='T' )
            g2o=0;
     if ( g1o || g2o )
     {
        cout<<"O won"<<endl;
        return ;
     }
     for (int i=0; i<4; i++)
         for (int j=0; j<4; j++)
             if ( s[i][j]=='.' )
             {
                cout<<"Game has not completed"<<endl;
                return ;     
             }
     cout<<"Draw"<<endl;
}
int main ()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int i=1; i<=test; i++)
        printf("Case #%d: ", i), solve();    
    return 0;
}
