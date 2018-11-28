//#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <memory.h>
 
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
 
#define  INF 100000000
#define eps 1e-11
#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000000007
//#define free asdfasdfsdadsg
//#define szz 400
//#define pb push_back
#define MAXN 100000
#define free afdshjioey
//#define SIZE 60
#define FOR(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

long tests,wx,wy;
string st[10];
long flx,fly;
long flend;
long ts;

void check(char c)
{
if (c=='T')return;
if (c=='.')flx=1,fly=1;
if (c=='O')flx=1;
if (c=='X')fly=1;
}
int main(){
//freopen("icy.in","r",stdin);
//freopen("icy.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

cin>>tests;
for (;tests;--tests)
{
    ++ts;
    
 for (int i=0;i<4;i++)
 cin>>st[i];
 
 wx=0;
 wy=0;
 
 for (int i=0;i<4;i++)
 {
  flx=fly=0;
  for (int j=0;j<4;j++)
  check(st[i][j]);
  if (flx==0)wx++;
  if (fly==0)wy++;
 }
 
 for (int i=0;i<4;i++)
 {
     flx=fly=0;
     for (int j=0;j<4;j++)
     check(st[j][i]);
     if (flx==0)++wx;
     if (fly==0)wy++;
 }
 
 flx=fly=0;
 for (int i=0;i<4;i++)
 {
     check(st[i][i]);
 }
 if (flx==0)++wx;
 if (fly==0)++wy;
 
 flx=fly=0;
 for (int i=0;i<4;i++)
 check(st[4-i-1][i]);
 if (flx==0)++wx;
 if (fly==0)++wy;
 
 flend=0;
 for (int i=0;i<4;i++)
 for (int j=0;j<4;j++)
 if (st[i][j]=='.')flend++;
 
 cout<<"Case #"<<ts<<": ";
 if (wx>0)cout<<"X won"<<endl;
 else if (wy>0)cout<<"O won"<<endl;
 else if (flend)cout<<"Game has not completed"<<endl;
 else cout<<"Draw"<<endl;
}

cin.get();cin.get();
return 0;}
