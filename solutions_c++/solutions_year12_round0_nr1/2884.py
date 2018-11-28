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

char mm[256];

int main()
{
//	freopen("A.txt","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    char s0[]="y qee";
    char s1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char s2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char s3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char b0[]="a zoo";
    char b1[]="our language is impossible to understand";
    char b2[]="there are twenty six factorial possibilitie";
    char b3[]="so it is okay if you want to just give up";
    cl(mm,0);
    bool maped[256];
    cl(maped,0);
    int l=sizeof(s0);
    rep(i,l){
        mm[s0[i]]=b0[i];
    }
    l=sizeof(s1);
    rep(i,l){
        mm[s1[i]]=b1[i];
    }
    l=sizeof(s2);
    rep(i,l){
        mm[s2[i]]=b2[i];
    }
    l=sizeof(s3);
    rep(i,l){
        mm[s3[i]]=b3[i];
    }
    char ch=0;
    For(i,'a','z'+1){
        if (mm[i])
            maped[mm[i]]=true;
        else
            ch=i;
    }
    char missed=0;
    For(i,'a','z'+1){
        if (!maped[i]) {missed=i;break;}
    }
    mm[ch]=missed;
    /*For(i,'a','z'+1){
        cout << (char)i;
    }
    cout<<endl;
    For(i,'a','z'+1){
        maped[mm[i]]=true;
        cout << mm[i];
    }
    cout<<endl;*/
    int T=0;
    char str[200];
	scanf("%d",&T);
    cin.getline(str, 200);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        cin.getline(str, 200);
        rep(i,strlen(str)){
            str[i]=mm[str[i]];
        }
        // output
        cout << "Case #"<<caseId<<": "<<str<<endl;
	}
    return 0;
}