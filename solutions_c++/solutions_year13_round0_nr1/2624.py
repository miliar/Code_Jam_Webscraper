#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<algorithm>
#include<stack>
#include<set>
#include<map>
#include<math.h>
#include<ctime>
#define LL long long
#define ULL unsigned long long
#define L long
#define VCTP vector<pair<LL,LL> >
#define PII pair<LL,LL>
#define PDD pair<double,double>
#define F first
#define S second
#define FOR(i,lb,ub) for(i=lb;i<=ub;i++)
#define RFOR(i,ub,lb) for(i=ub;i>=lb;i--)
#define FORS(it,v) for(it=v.begin();it!=v.end();it++)
#define st_clk double st=clock();
#define end_clk double en=clock();
#define show_time cout<<"\tTIME="<<(en-st)/CLOCKS_PER_SEC<<endl;
#define sc(n) scanf("%d",&n)
#define scst(n) scanf("%s",n)
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
using namespace std;
 #ifndef ONLINE_JUDGE
inline int getchar_unlocked() { return getchar(); }
#endif
template <class T>
inline void r_f(T &p)
{
         char c;
         while ((c=getchar_unlocked()) < 48 || c > 57);
         p=c-48;
         while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
}
char str[5][5];
bool horiz(char c)
{
     int i,cnt=0,j;
     FOR(i,0,3)
     {
               cnt=0;
               FOR(j,0,3)
                         if (str[i][j]=='T' || str[i][j]==c)
                            cnt++;
               if (cnt==4)
                  return 1;
     }
     return 0;
}
bool vert(char c)
{
     int i,cnt=0,j;
     FOR(i,0,3)
     {
               cnt=0;
               FOR(j,0,3)
                         if (str[j][i]=='T' || str[j][i]==c)
                            cnt++;
               if (cnt==4)
                  return 1;
     }
     return 0;
}
bool diag(char c)
{
     int i,j,cnt=0;
     FOR(i,0,3)
               if (str[i][i]=='T' || str[i][i]==c)
                  cnt++;
     if (cnt==4)
                  return 1;
     cnt=0;
     i=3;
     FOR(j,0,3)
     {
               if (str[i][j]=='T' || str[i][j]==c)
                  cnt++;
               i--;
     }
     if (cnt==4)
                  return 1;
     return 0;
}
 bool draw()
 {
      int i,j,flag=0;
      FOR(i,0,3){
                 FOR(j,0,3){
                            if (str[i][j]=='.')
                               return 0;
                               }
                 }
      return 1;
 }
     
int main()
{
     #ifndef ONLINE_JUDGE
     f_in("A-large.in");
     f_out("out.txt");
     #endif
     int t,i=1;
     cin>>t;
     while (t--)
     {
           cout<<"Case #"<<i++<<": ";
           cin>>str[0]>>str[1]>>str[2]>>str[3];
           char c='X';
           if (horiz(c) || vert(c) || diag(c))
              cout<<"X won\n";
           
           else if (c='O', (horiz(c) || vert(c) || diag(c)))
              cout<<"O won\n";
           else if (draw())
                cout<<"Draw\n";
           else cout<<"Game has not completed\n";
     }

//system("pause");
return 0;
}
