// {{{
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define ALL(A)		(A).begin(),(A).end()
#define DUMP(A)    cout<<#A<<"="<<(A)<< endl
#define SIZE(A)    (int)((A).size())
#define MP  make_pair
#define PB  push_back
using namespace std;
typedef long long ll;

int vx[]={1,0,-1,0},vy[]={0,1,0,-1};
// }}}

int rs[1000];
double px[1000],py[1000];
const int DIV=5000;
const double EPS=1e-6;
double p2(double x){
    return x*x;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int ix=0;ix<T;ix++){
        printf("Case #%d:",ix+1);
        int N,W,L;
        scanf("%d%d%d",&N,&W,&L);
        for(int i=0;i<N;i++){
            scanf("%d",&rs[i]);
        }
        double dd2=(double)((ll)W*(ll)L)/(double)DIV;
        double dd=sqrt((double)dd2);
        px[0]=EPS,py[0]=EPS;
        for(int i=1;i<N;i++){
            bool is2=false;
            for(double y=EPS;y+EPS<L;y+=dd){
                for(double x=EPS;x+EPS<W;x+=dd){
                    bool is=true;
                    for(int j=0;j<i;j++){
                        if(sqrt(p2(x-px[j])+p2(y-py[j]))+EPS <= rs[i]+rs[j]){
                            is=false;
                        }
                    }
                    if(is){
                        is2=true;
                        px[i]=x;
                        py[i]=y;
                        goto EXIT;
                    }
                }
            }
EXIT:       ;
            if(!is2) printf("fuck\n");
        }
        for(int i=0;i<N;i++){
            printf(" %.6f %.6f",px[i],py[i]);
        }
        printf("\n");
    }
}
