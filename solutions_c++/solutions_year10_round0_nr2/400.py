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
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
const int oo=1000000;

#pragma warning(disable:4996)

int GetGCD(int *arr, int len)
{
    int iMax = arr[0], iCurr, iRemainder;

    for(int i = 1; i < len; i++)
    {
        iCurr = arr[i];

        if (iMax < iCurr)
        {
            iMax ^= iCurr;
            iCurr ^= iMax;
            iMax ^= iCurr;
        }

        iRemainder = iMax % iCurr;

        while (iRemainder)
        {
            iMax = iCurr;
            iCurr = iRemainder;
            iRemainder = iMax % iCurr;
        }
        
        iMax = iCurr;
    }//for

    return iMax;

}

int main()
{
    int V[1000];
    int D[1000];

    //const char flnm[] = "test";
    const char flnm[] = "B-small-attempt1";
    //const char flnm[] = "B-large";
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
        int n;
        i_file>>n;
        rep(i,n){
            i_file>>V[i];
        }
        int k=0;
        rep(i,n-1){
            int tmp=V[i+1]-V[i];
            if (tmp==0)
                continue;
            if (tmp<0)
                D[k]=-tmp;
            else
                D[k]=tmp;
            k++;
        }
        int res=(k>1)? GetGCD(D, k) : D[0];
        int tt=V[0] % res;
        if(tt>0){
            tt=res-tt;
        }
        cout << "Case #"<<caseId<<": "<<tt<<"\n";
        o_file << "Case #"<<caseId<<": "<<tt<<"\n";
	}
    i_file.close();
    o_file.flush();
    o_file.close();
    return 0;
}