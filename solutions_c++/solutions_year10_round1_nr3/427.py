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
const int oo=1000000;

#pragma warning(disable:4996)


bool calc(int a,int b)
{
    int cc=1;
    int c=a-b;
    a=b;
    b=c;
    while(c>1)
    {
        c=a-b;
        a=b;
        b=c;
        cc++;
    }
    return cc%2?false:true;
}

bool check(int a, int b)
{
    if (a<b)
        Swap(a,b);
    if (a==b)
        return false;
    else if (a%b==0 || b==1)
        return true;

    bool bb=(a>=b*2);
    if (bb)
        return true;
    return calc(a,b);
}

int main()
{
    //int V[1000];

    //const char flnm[] = "test";
    const char flnm[] = "C-small-attempt0";
    //const char flnm[] = "C-large";
    char flnm_in[255];
    char flnm_out[255];
    strcpy(flnm_in, flnm);
    strcat(flnm_in, ".in");
    strcpy(flnm_out, flnm);
    strcat(flnm_out, ".out");
    ifstream i_file;
    i_file.open(flnm_in);
    ofstream o_file;
    o_file.open(flnm_out);
    if (!i_file.is_open())
        return 0;
    if (!o_file.is_open())
        return 0;
    int T=0;
    i_file>>T;
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int a1,a2,b1,b2;
        i_file>>a1>>a2>>b1>>b2;

        int cc=0;
        For(i,a1,a2+1){
            For(j,b1,b2+1){
                if (check(i,j))
                    cc++;
            }
        }
        // output
        cout << "Case #"<<caseId<<": "<<cc<<"\n";
        o_file << "Case #"<<caseId<<": "<<cc<<"\n";
	}
    i_file.close();
    o_file.flush();
    o_file.close();
    return 0;
}