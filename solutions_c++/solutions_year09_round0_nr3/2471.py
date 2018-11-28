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

#define DEBUGGING              1
#define VAR(x,a)               __typeof(a) x(a)
#define FORD(i,a,b)            for(int i = (int)a,_b = (int)b;i>=(_b);--i)
#define FOREACH(it,v)  	       for(VAR(it,(v).begin());it!=(v).end();++it)
#define FOR(i,a,b)             for(int i=(a) ; i<(b) ; ++i)
#define	REP(i,n)               FOR(i,0,n)
#define REPD(i,n)              FORD(i,n,0)
#define Size()                 size()
#define PB                     push_back
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
int Count;
int GetCount(string S);
void Search(int Index,string S,int State,int High);
int main()
{
    FILE *in=fopen("D:/rahulakaneo/rahulakaneo/gcj/input.txt","r");
    FILE *out=fopen("D:/rahulakaneo/rahulakaneo/gcj/output.txt","w");
    int N;
    fscanf(in,"%d",&N);
    char s[550];
    fgets(s,100,in);
    for(int i=0;i<N;++i) {
        fgets(s,510,in);
        string S;
        for(int i=0;i<strlen(s)-1;++i)
            S.PushBack(s[i]);
        if(DEBUGGING)
            cout<<S<<endl;
        GetCount(S);
        fprintf(out,"Case #%d: %04d\n",i+1,Count);
    }
    if(DEBUGGING) {
        fflush(stdin);
        getchar();
    }
    return 0;
}
int GetCount(string S)
{
    /* 
    ** welcome to code jam 
    */
    Count=0;
    for(int i=0;i<S.size();++i) {
        if(S[i]=='w') {
            Search(i+1,S,2,S.size());
        }
    }
    return Count;
}
void Search(int Index,string S,int State,int High)
{
    if(State==19) {
        for(int i=Index;i<High;++i) {
            if(S[i]=='m')
             Count++;
        }
    }
    else if(State==18) {
        for(int i=Index;i<High;++i)
            if(S[i]=='a')
                Search(i+1,S,State+1,High);
    }
    else if(State==17) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='j')
                Search(i+1,S,State+1,High);
    }
    else if(State==16) {
        for(int i=Index;i<High;++i) 
            if(S[i]==' ')
                Search(i+1,S,State+1,High);
    }
    else if(State==15) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='e')
                Search(i+1,S,State+1,High);
    }
    else if(State==14) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='d')
                Search(i+1,S,State+1,High);
    }
    else if(State==13) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='o')
                Search(i+1,S,State+1,High);
    }
    else if(State==12) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='c')
                Search(i+1,S,State+1,High);
    }
    else if(State==11) {
        for(int i=Index;i<High;++i) 
            if(S[i]==' ')
                Search(i+1,S,State+1,High);
    }
    else if(State==10) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='o')
                Search(i+1,S,State+1,High);
    }
    else if(State==9) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='t')
                Search(i+1,S,State+1,High);
    }
    else if(State==8) {
        for(int i=Index;i<High;++i) 
            if(S[i]==' ')
                Search(i+1,S,State+1,High);
    }
    else if(State==7) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='e')
                Search(i+1,S,State+1,High);
    }
    else if(State==6) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='m')
                Search(i+1,S,State+1,High);
    }
    else if(State==5) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='o')
                Search(i+1,S,State+1,High);
    }
    else if(State==4) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='c')
                Search(i+1,S,State+1,High);
    }
    else if(State==3) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='l')
                Search(i+1,S,State+1,High);
    }
    else if(State==2) {
        for(int i=Index;i<High;++i) 
            if(S[i]=='e')
                Search(i+1,S,State+1,High);
    }
    
    /* welcome to code jam */
    
}
