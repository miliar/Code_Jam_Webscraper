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


template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector <long double> vd;

int main()
{
    int T;
    double ans;
    cin>>T;
    rep(t,1,T+1)
    {
        int N;
        cin>>N;
        vector <vi> sch (N,vector <int> (N,-1));
        char temp;
        repi(N)
        {
            repj(N)
            {
                cin>>temp;
                if(temp!='.')
                sch[i][j]=temp-'0';
            }
        }
        vector <long double> RPI(N,0.0),WP(N,0.0),OWP(N,0.0),OOWP(N,0.0);

        repi(N){int tot=0;repj(N){if(sch[i][j]!=-1){WP[i]+=sch[i][j];tot++;}}WP[i]/=tot;}
        repi(N)
        {

            int tempt1=0;
            repj(N)
            {
                int tempt=0;
                long double tempv=0.0;
                if(i==j)
                continue;
                if(sch[j][i]!=-1)
                {
                    repk(N)
                    {
                        if(k==i||sch[j][k]==-1)
                        continue;
                        tempv+=sch[j][k];
                        tempt++;
                    }
                    tempv/=tempt;
                    OWP[i]+=tempv;
                    tempt1++;
                }


            }
            OWP[i]/=tempt1;
        }
        repi(N)
        {
            int tot1=0;
            repj(N)
            {
                if(sch[i][j]!=-1)
                {OOWP[i]+=OWP[j];
                tot1++;}
            }
            OOWP[i]/=tot1;
        }
        printf( "Case #%d:\n",t);
        repi(N)
        {
           // cout<<WP[i]<<" "<<OWP[i]<<" "<<OOWP[i]<<endl;
            RPI[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
            cout<<RPI[i]<<endl;
            //printf( "%d.8\n",RPI[i]);
        }

    }
    return 0;
}
