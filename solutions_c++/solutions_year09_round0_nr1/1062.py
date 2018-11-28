#include<iostream>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<utility>
#include<fstream>
#include<iosfwd>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<cstring>
#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cassert>
#include<complex>
#include<numeric>

using namespace std;

#define DEBUGGING              0
#define VAR(x,a)               __typeof(a) x(a)
#define FORD(i,a,b)            for(int i = (int)a,_b = (int)b;i>=(_b);--i)
#define FOREACH(it,v)  	       for(VAR(it,(v).begin());it!=(v).end();++it)
#define FOR(i,a,b)             for(int i=(int)(a),_b = (int)b;i<(int)(_b);++i)
#define	REP(i,n)               FOR(i,0,n)
#define REPD(i,n)              FORD(i,n,0)
#define Size()                 size()
#define PushBack               push_back
#define PushFront              push_front
#define MakePair               make_pair
#define PopBack                pop_back
#define PopFront               pop_front
#define BitCount               __builtin_popcount
#define V(x)                   vector< x >
#define INF                    100000000
#define INFLL                  10000000000000000LL
#define First                  first
#define Second                 second

typedef V(int)                 VI;
typedef V(VI)                  VII;
typedef V(string)              VS;
typedef unsigned long long     ULL;
typedef long long              LL;
typedef pair<int,int>          PI;
typedef unsigned long          UL;

int GetResults(int L,int D,char Dictionary[][20],char Word[]);
int IsSubstring(int Length,char S[],char T[]);
bool IsContained(char s,char T[],int Low,int High);
int main()
{
    FILE *in=fopen("D:/rahulakaneo/rahulakaneo/gcj/aliens/input.txt","r");
    FILE *out=fopen("D:/rahulakaneo/rahulakaneo/gcj/aliens/output.txt","w");
    int L,D,N;
    char Word[1000];
    char Dictionary[5010][20];
    fscanf(in,"%d %d %d",&L,&D,&N);
    for(int i=0;i<D;++i) 
        fscanf(in,"%s",Dictionary[i]);
    for(int i=0;i<N;++i) {
        fscanf(in,"%s",Word);
        fprintf(out,"Case #%d: %d\n",i+1,GetResults(L,D,Dictionary,Word));
    }
    return 0;
}
int GetResults(int L,int D,char Dictionary[][20],char Word[])
{
    int Count=0;
    for(int i=0;i<D;++i) {
        Count+=IsSubstring(L,Dictionary[i],Word);
    }
    return Count;
}
int IsSubstring(int Length,char S[],char T[])
{
    for(int i=0,j=0;i<Length;++i,++j) {
        if(T[j]!='(') {
            if(S[i]!=T[j]) {
                return 0;
            }
        }
        else {
            int k=j+1;
            while(T[k]!=')') {
                ++k;
            }
            if(!IsContained(S[i],T,j+1,k-1))
                return 0;
            j=k;
        }
    }
    return 1;
}
bool IsContained(char s,char T[],int Low,int High)
{
    
    for(int i=Low;i<=High;++i) {
        if(T[i]==s)
            return true;
    }
    return false;
}
