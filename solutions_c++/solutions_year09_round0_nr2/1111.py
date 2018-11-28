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

int Row,Col;
void GetResults(int M[][120],int O[120][120]);
int Smallest(int A,int B,int C,int D);
int main()
{
    FILE *IN=fopen("D:/rahulakaneo/rahulakaneo/gcj/watershed/input.txt","r");
    FILE *OUT=fopen("D:/rahulakaneo/rahulakaneo/gcj/watershed/output.txt","w");
    int TestCases;
    fscanf(IN,"%d",&TestCases);
    int Matrix[120][120];
    int Output[120][120];
    printf("yes");
    for(int T=0;T<TestCases;++T) {
        fscanf(IN,"%d %d",&Row,&Col);
        for(int i=0;i<=Row+1;++i)
            Matrix[i][0]=Matrix[i][Col+1]=INF;
        for(int j=0;j<=Col+1;++j)
            Matrix[0][j]=Matrix[Row+1][j]=INF;
        for(int i=0;i<Row;++i)
            for(int j=0;j<Col;++j)
                fscanf(IN,"%d",&Matrix[i+1][j+1]);
        GetResults(Matrix,Output);
        fprintf(OUT,"Case #%d:\n",T+1);
        for(int i=1;i<=Row;++i) {
            for(int j=1;j<=Col;++j) {
                fprintf(OUT,"%c ",Output[i][j]+'a'-1);
            }
            fprintf(OUT,"\n");
        }
    }
    return 0;
}
void GetResults(int M[][120],int O[120][120])
{
    int Sink[120][120];
    int T=1;
    int Sinks;
    memset(Sink,0,sizeof(Sink));
    for(int i=1;i<=Row;++i) {
        for(int j=1;j<=Col;++j) {
            int X=i;
            int Y=j;
            while(!Sink[X][Y]) {
                int Small=Smallest(M[X+1][Y],M[X-1][Y],M[X][Y+1],M[X][Y-1]);
                if(M[X][Y]<=M[X][Y+1]&&M[X][Y]<=M[X+1][Y]&&M[X][Y]<=M[X-1][Y]&&M[X][Y]<=M[X][Y-1]) {
                    Sink[X][Y]=T++;
                    break;
                }
                else if(Small==M[X-1][Y]) {
                    X=X-1;
                }
                else if(Small==M[X][Y-1]) {
                    Y=Y-1;
                }
                else if(Small==M[X][Y+1]) {
                    Y=Y+1;
                }
                else if(Small==M[X+1][Y]) {
                    X=X+1;
                }
            }
            O[i][j]=Sink[X][Y];
        }
    }
}
int Smallest(int A,int B,int C,int D)
{
    int Small1 = A<B?A:B;
    int Small2 = C<D?C:D;
    return Small1<Small2?Small1:Small2;
}
