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

/*
** Description :
*/
int GetCount(string S);
int main()
{
    FILE *IN=fopen("D:/rahulakaneo/rahulakaneo/gcj/welcome to code jam/input.txt","r");
    FILE *OUT=fopen("D:/rahulakaneo/rahulakaneo/gcj/welcome to code jam/output.txt","w");
    char s[1000];
    int N;
    fscanf(IN,"%d",&N);
    fgets(s,550,IN);
    for(int i=0;i<N;++i) {
        string S;
        fgets(s,550,IN);
        for(int j=0;j<strlen(s)-1;++j)
            S.PushBack(s[j]);
        int Count=GetCount(S);
        fprintf(OUT,"Case #%d: %04d\n",i+1,Count);
    }    
    return 0;
}
int GetCount(string S)
{
    int w=0;
    int we=0;
    int wel=0;
    int welc=0;
    int welco=0;
    int welcom=0;
    int welcome=0;
    int welcomeSP=0;
    int welcomeSPt=0;
    int welcomeSPto=0;
    int welcomeSPtoSP=0;
    int welcomeSPtoSPc=0;
    int welcomeSPtoSPco=0;    
    int welcomeSPtoSPcod=0;
    int welcomeSPtoSPcode=0;
    int welcomeSPtoSPcodeSP=0;
    int welcomeSPtoSPcodeSPj=0;
    int welcomeSPtoSPcodeSPja=0;
    int welcomeSPtoSPcodeSPjam=0;
    for(int i=0;i<S.size();++i) {
        if(S[i]=='w') {
            w=(w+1)%10000;
        }
        if(S[i]=='e') {
            we=(w+we)%10000;
            welcome+=welcom%10000;
            welcomeSPtoSPcode+=welcomeSPtoSPcod%10000;
        }
        if(S[i]=='l') {
            wel+=we%10000;
        }
        if(S[i]=='c') {
            welc+=wel%10000;
            welcomeSPtoSPc+=welcomeSPtoSP%10000;
        }
        if(S[i]=='o') {
            welco+=welc%10000;
            welcomeSPto+=welcomeSPt%10000;
            welcomeSPtoSPco+=welcomeSPtoSPc%10000;
        }
        if(S[i]=='m') {
            welcom+=welco%10000;
            welcomeSPtoSPcodeSPjam+=welcomeSPtoSPcodeSPja%10000;
        }
        if(S[i]==' ') { // SP
            welcomeSP+=welcome%10000;
            welcomeSPtoSP+=welcomeSPto%10000;
            welcomeSPtoSPcodeSP+=welcomeSPtoSPcode%10000;
        }
        if(S[i]=='t') {
            welcomeSPt+=welcomeSP%10000;            
        }
        if(S[i]=='d') {
            welcomeSPtoSPcod+=welcomeSPtoSPco%10000;
        }
        if(S[i]=='j') {
            welcomeSPtoSPcodeSPj+=welcomeSPtoSPcodeSP%10000;
        }
        if(S[i]=='a') {
            welcomeSPtoSPcodeSPja+=welcomeSPtoSPcodeSPj%10000;
        }
    }
    return welcomeSPtoSPcodeSPjam%10000;
}
