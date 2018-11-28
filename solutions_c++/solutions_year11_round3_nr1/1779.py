#include<iostream>
#include<cstdio>
#include<string>
#include<list>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<bitset>
#include<conio.h>
#define rep(a,s,n) for(int a=s;a<n;a++)
#define repn(a,s,n) for(int a=n-1;a>=s;a--)
#define repi(n) rep(i,0,n)
#define repj(n) rep(j,0,n)
#define repk(n) rep(k,0,n)

#define overallr(class,beg,end) for(class::iterator it=beg;it!=end;it++)
#define overallrn(class,beg,end) for(class::iterator it=end;it!=beg;it--)
#define overall(class,obj) overallr(class,obj.begin(),obj.end())

#define all(v) (v).begin( ), (v).end( )
#define pub push_back
#define puf push_front
#define pob pop_back
#define pof pop_front

using namespace std;


template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( "" ); first = false; cout << * i; } printf( "" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;

int main()
{
    int T;
    double ans;
    cin>>T;
    rep(tt,1,T+1)
    {
        int R,C;
        cin>>R>>C;
        vector< vector<char> > t(R,vector<char> (C,'.'));
        bool ok=true;
        int sum=0;
        repi(R)repj(C){cin>>t[i][j];if(t[i][j]=='#')sum++;}
        printf( "Case #%d:\n",tt);
        //repi(R){repj(C){cout<<t[i][j];}cout<<"\n";}
        if(sum%4!=0)
        {
            printf( "Impossible\n");
            continue;
        }
        if(R<2 || C<2)
        {
            repi(R){repj(C){cout<<t[i][j];}cout<<"\n";}
            ok=false;
        }
        else
        {
            repi(R-1)
            {
                repj(C-1)
                {
                    //cout<<t[i][j]<<endl;
                    if(t[i][j]=='#')
                    {

                        if(t[i][j+1]=='#'&&t[i+1][j]=='#'&&t[i+1][j+1]=='#')
                        {
                            t[i][j]='/';
                            t[i][j+1]='\\';
                            t[i+1][j]='\\';
                            t[i+1][j+1]='/';
                            //repi(R){repj(C){cout<<t[i][j];}cout<<"\n";}
                        }
                        else
                        {
                            printf( "Impossible\n");
                            ok=false;
                            break;
                        }
                    }

                }
                 if(not(ok))
                break;


            }
        }
        if(ok)
        {
            repi(R){repj(C){cout<<t[i][j];}cout<<"\n";}
        }

       // printf( "Case #%d: %d\n", t ,ans);
    }
    return 0;
}
