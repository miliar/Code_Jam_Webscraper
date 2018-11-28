#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <climits>
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
using namespace std;
typedef long long ll;

int main(){
    int T;
    scanf("%d",&T);
    for(int ix=1;ix<=T;ix++){
        int X,S,R,t,N;
        scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
        vector<double> speed(X,0);
        for(int i=0;i<N;i++){
            int E,B,W;
            scanf("%d%d%d",&E,&B,&W);
            for(int j=E;j<B;j++){
                speed[j]=W;
            }
        }
        double ret=0;
        double nowt=t;
        sort(ALL(speed));
        for(int i=0;i<X;i++){
            double ti=speed[i]+R;
            if(nowt>=1.0/ti){
                ret+=1.0/ti;
                nowt-=1.0/ti;
            }else if(nowt>0){
                double dist=ti*nowt;
                ret+=nowt+(1.0-dist)/(speed[i]+S);
                nowt=0;
            }else{
                ret+=1.0/(speed[i]+S);
            }
        }
        printf("Case #%d: %.8f\n",ix,ret);
    }
}
