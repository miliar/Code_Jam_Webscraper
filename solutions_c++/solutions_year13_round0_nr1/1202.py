#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <istream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <list>
#include <cstdio>
#include <set>
#include <iomanip>
#include <stack>
#include <ctime>
#include <climits>
#include <iterator>
#define LOCAL
#ifdef ONLINE_JUDGE
#define COUT(s)
#undef LOCAL
#endif
#ifdef LOCAL
#define cin in
#define cout out
#define COUT(s) cout<<"-----"<<s<<"-----"<<endl;
#endif

using namespace std;

bool between(int e,int a,int b)
{
    return e>=a&&e<=b;
}


int main(int argc,char **argv)
{
#ifdef LOCAL
    ifstream in("input.txt");
    ofstream out("output.txt");
#endif
    int dx[8]={0,0,1,1,1,-1,-1,-1};
    int dy[8]={1,-1,0,1,-1,0,1,-1};
    int nb_cas;
    cin>>nb_cas;
    for(int c=1;c<=nb_cas;c++)
    {
        cout<<"Case #"<<c<<": ";
        vector<string> v(4);
        for(int c=0;c<v.size();c++)
            cin>>v[c];
        bool vide=false;
        for(int x=0;x<v.size();x++)
            for(int y=0;y<v.size();y++)
            {
                vide|=(v[x][y]=='.');
                if(v[x][y]=='.'||v[x][y]=='T')
                    continue;
                for(int c2=0;c2<8;c2++)
                {
                    int c3=0;
                    for(;c3<4;c3++)
                    {

                        int x2=x+dx[c2]*c3;
                        int y2=y+dy[c2]*c3;
                        if(!(between(x2,0,v.size()-1)&&between(y2,0,v.size()-1)&&(v[x2][y2]==v[x][y]||v[x2][y2]=='T')))
                        {
                            break;
                        }
                    }
                    if(c3==4)
                    {
                        cout<<v[x][y]<<" won";
                        goto end;
                    }
                }
            }
        cout<<(vide?"Game has not completed":"Draw");
        end:
            cout<<endl;
    }

}
