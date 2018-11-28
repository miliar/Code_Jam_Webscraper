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

char who[101];
int pos[101];
int n;

int getTar(char w, int from) {
    For(i,from,n) {
        if (who[i]==w) {
            return pos[i];
        }
    }
    return -1;
}

int main()
{
	//freopen("test.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        cl(who,0);
        cl(pos,0);
        // input
        cin>>n;
        rep(i,n){
            cin>>who[i]>>pos[i];
        }
        char next=who[0];
        int posO=1;
        int posB=1;
        int tarO=getTar('O',0);
        int tarB=getTar('B',0);
        int ctO=abs(posO-tarO);
        int ctB=abs(posB-tarB);
        int p=0;
        int ct=0;
        while(p<n) {
            if (next == 'O'){
                ctO++;
                ct += ctO;
                ctB-=ctO;
                if (ctB<0) ctB=0;
                posO=tarO;
                tarO=getTar('O',p+1);
                ctO=abs(posO-tarO);
            }
            else if (next == 'B'){
                ctB++;
                ct += ctB;
                ctO-=ctB;
                if (ctO<0) ctO=0;
                posB=tarB;
                tarB=getTar('B',p+1);
                ctB=abs(posB-tarB);
            }
            next=who[++p];
        }

        // output
        cout << "Case #"<<caseId<<": "<<ct<<"\n";
	}
    return 0;
}