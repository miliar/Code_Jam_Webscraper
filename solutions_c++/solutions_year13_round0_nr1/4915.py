#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<ctype.h>
#include<time.h>//srand(time(NULL))

using namespace std;

#include <cstring>

#define REP(i,N)    for(int i=0;i<N;i++)
#define REV(i,N)    for(int i=N;i>=0;i--)
#define FOR(i,a,b)  for(int __n=b,i=a;i<=__n;i++)
#define FORD(i,a,b) for(int __n=b,i=a;i>=__n;i--)

#define SZ(a)       (int)a.size()
#define ll          long long
#define ull         unsigned long long
#define ISS         istringstream
#define OSS         ostringstream
#define VS          vector<string>
#define vi          vector<int>
#define vd          vector<double>
#define vll         vector<long long>
#define SII         set<int>::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define fs          first
#define sc          second
#define pii         pair < int , int >
#define mp          make_pair

#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a,b,c)  for(int I=0;I<b;I++)    a[I] = c
#define CROSS(a,b,c,d) ((b.x-a.x)*(d.y-c.y)-(d.x-c.x)*(b.y-a.y))
#define sqr(a)      ((a)*(a))
#define FORE(i,a)   for(typeof((a).begin())i=(a).begin();i!=(a).end();i++)//reverse_iterator
#define BE(a)       a.begin(),a.end()
#define rev(a)      reverse(ALL(a));
#define sorta(a)    sort(ALL(a))
#define pb          push_back
#define popb        pop_back
#define round(i,a)  i = ( a < 0 ) ? a - 0.5 : a + 0.5;
#define makeint(n,s)  istringstream(s)>>n
#define read()      freopen("test.txt","r",stdin)

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

//bool operator()(const int &p,const int &q){return p<q;}//for map,set sort
//bool operator<(const data &p)const{return p.w<w;}


///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

int kkaass=1;
#define KAS()       printf("Case %d: ",kkaass++)
#define oo          (1<<30)
#define PI          3.141592653589793
#define pi          2*acos(0)
#define ERR         1e-5
#define PRE         1e-8
#define MAX         100009
//binary search backtracking map<int , bool>
//go dist1 mat2 way seen data mat box cont store dag nume var

char ch[4][4];

void print(int cas,int s)
{
    printf("Case #%d: ",cas);
    if(s==1)cout<<"X won"<<endl;
    if(s==2)cout<<"O won"<<endl;
    if(s==3)cout<<"Draw"<<endl;
    if(s==4)cout<<"Game has not completed"<<endl;
    return ;
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for(int cas=1; cas<=t; cas++)
    {
        for(int i=0; i<4; i++)cin>>ch[i];


        int x=0,o=0;
        for(int i=0; i<4; i++)
        {
            if(ch[i][i]=='X')x++;
            else if(ch[i][i]=='O')o++;
            else if(ch[i][i]=='T')
            {
                x++;
                o++;
            }
        }

        if(x==4)
        {
            print(cas,1);
            continue;
        }
        else if(o==4)
        {
            print(cas,2);
            continue;
        }

        x=0,o=0;
        for(int i=0; i<4; i++)
        {
            if(ch[i][3-i]=='X')x++;
            else if(ch[i][3-i]=='O')o++;
            else if(ch[i][3-i]=='T')
            {
                x++;
                o++;
            }
        }

        if(x==4)
        {
            print(cas,1);
            continue;
        }
        else if(o==4)
        {
            print(cas,2);
            continue;
        }

        int row[4][2]= {0};
        int col[4][2]= {0};

        int blank=0;

        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(ch[i][j]=='X')
                {
                    row[i][0]++;
                    col[j][0]++;
                }
                else if(ch[i][j]=='O')
                {
                    row[i][1]++;
                    col[j][1]++;
                }
                else if(ch[i][j]=='T')
                {
                    row[i][0]++;
                    row[i][1]++;

                    col[j][0]++;
                    col[j][1]++;
                }
                else blank++;
            }
        }

        bool f=1;
        for(int i=0; i<4; i++)
        {
            if(row[i][0]==4 || col[i][0]==4)
            {
                f=0;
                print(cas,1);
                break;
            }
            else if(row[i][1]==4 || col[i][1]==4)
            {
                f=0;
                print(cas,2);
                break;
            }
        }
        if(f)
        {
            if(blank==0)print(cas,3);
            else print(cas,4);
        }

        if(cas!=t)getchar();
    }


    return 0;
}
