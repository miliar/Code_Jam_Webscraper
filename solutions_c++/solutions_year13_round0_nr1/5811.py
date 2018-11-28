#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "A"

char mm[256];

int main()
{
//	freopen("" QX ".txt","r",stdin);
//	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);

	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        char gm[4][4];
        bool finished = true;
        rep(i,4){
            rep(j,4){
                cin>>gm[i][j];
                if (gm[i][j]=='.')
                    finished = false;
            }
        }
        bool XW=false;
        bool OW=false;
        // detect rows
        rep(i,4) {
            bool xw=true;
            bool ow=true;
            rep(j,4) {
                char ch = gm[i][j];
                if (ch=='X'||ch=='.')
                    ow=false;
                if (ch=='O'||ch=='.')
                    xw=false;
            }
            if (xw){
                XW=true;
                break;
            }
            if (ow){
                OW=true;
                break;
            }
        }

        rep(i,4) {
            bool xw=true;
            bool ow=true;
            rep(j,4) {
                char ch = gm[j][i];
                if (ch=='X'||ch=='.')
                    ow=false;
                if (ch=='O'||ch=='.')
                    xw=false;
            }
            if (xw){
                XW=true;
                break;
            }
            if (ow){
                OW=true;
                break;
            }
        }
        {
            bool xw=true;
            bool ow=true;
            rep(i,4) {
                char ch = gm[i][i];
                if (ch=='X'||ch=='.')
                    ow=false;
                if (ch=='O'||ch=='.')
                    xw=false;
            }
            if (xw){
                XW=true;
            }
            if (ow){
                OW=true;
            }
        }
        if (XW==false&&OW==false)
        {
            bool xw=true;
            bool ow=true;
            rep(i,4) {
                char ch = gm[i][3-i];
                if (ch=='X'||ch=='.')
                    ow=false;
                if (ch=='O'||ch=='.')
                    xw=false;
            }
            if (xw){
                XW=true;
            }
            if (ow){
                OW=true;
            }
        }

        // output
        std::string str;
        if (XW && !OW)
            str = "X won"; //(the game is over, and X won)
        else if (!XW && OW)
            str = "O won"; //(the game is over, and O won)
        else if (finished)
            str = "Draw"; //(the game is over, and it ended in a draw)
        else
            str = "Game has not completed"; //(the game is not over yet)
        cout << "Case #"<<caseId<<": "<<str<<endl;
	}
    return 0;
}