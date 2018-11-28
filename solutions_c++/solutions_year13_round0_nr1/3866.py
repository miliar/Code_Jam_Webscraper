#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>

#define ss stringstream
#define fo(a, b, c) for(a = (b); a < ( c ); a++ )
#define fr(a, b) fo(a, 0, ( b ) )
#define fi(a) fr(i, ( a ) )
#define fj(a) fr (j, ( a ) )
#define fk(a) fr(k, ( a ) )
#define _(a, b) memset(a, b, sizeof( a ) )

using namespace std;

int ni() { int a; cin>>a;  return a;}
char nc() { char a; cin>>a; return a;}
float nf() { float a; cin>>a; return a;}
long long  nll() { long long  a; cin>>a; return a;}

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define XXXX 352
#define XXXT 348
#define OOOO 316
#define OOOT 321

int main()
{
    int complete, n, i, j, k, tt;
    int rsum[4], csum[4], dsum[2];
    char mve[4][4];
    freopen("A-large.IN", "r", stdin);
    freopen("A-large.OUT", "w", stdout);
    cin>>tt;
    fr(n, tt)
    {
        rsum = {0, 0, 0, 0};
        csum = {0, 0, 0, 0};
        dsum = {0, 0};
        complete = 1;
        cout<<"Case #"<<n+1<<": ";
        fi(4)
            fj(4)
            {
                cin>>mve[i][j];
            }
        fi(4)
        {
            dsum[0] += (int)mve[i][i];
            dsum[1] += (int)mve[i][3-i];
            //cout<<mve[i][3-i]<<endl;
            fj(4)
            {
                if(mve[i][j]=='.')
                    complete = 0;
                rsum[i] += (int)mve[i][j];
                csum[i] += (int)mve[j][i];
            }

            if(rsum[i]==XXXX ||rsum[i]==XXXT ||csum[i]==XXXX ||csum[i]==XXXT)
            {
                cout<<"X won"<<endl;
                goto X_WIN;
            }
            else if(rsum[i]==OOOO ||rsum[i]==OOOT ||csum[i]==OOOO ||csum[i]==OOOT)
            {
                cout<<"O won"<<endl;
                goto O_WIN;
            }
        }
        if(dsum[0]==XXXX || dsum[0]==XXXT || dsum[1]==XXXX || dsum[1]==XXXT)
        {
            cout<<"X won"<<endl;
            goto X_WIN;
        }
        else if(dsum[0]==OOOO || dsum[0]==OOOT || dsum[1]==OOOO || dsum[1]==OOOT)
        {
            cout<<"O won"<<endl;
            goto O_WIN;
        }

        if(complete==0)
            cout<<"Game has not completed"<<endl;
        else if(complete == 1)
            cout<<"Draw"<<endl;
        O_WIN:
        X_WIN:
            complete = 1;
    }
}
