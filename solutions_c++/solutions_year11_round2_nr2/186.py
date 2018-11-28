#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;
double eps  = 1e-7;
int pos[1000],num[1000];
int N,D;
bool check(double mid){
    double left = -1e20;
    int i,j;
    for (i=0;i<N;i++){
        for (j=0;j<num[i];j++){
            double tmp = max(left+D,1.0*pos[i]-mid);
            if (tmp>pos[i]+mid) return false;
            left = tmp;
        }
    }
    return true;
    
}
int main(){
    int tt,i,j,o,k,choose,c,cost;
    freopen("B-large.in","r",stdin);    freopen("B-large.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1;tcas<=tt;tcas++){
        scanf("%d%d",&N,&D);
        double sum = 0;
        for (i=0;i<N;i++){
            scanf("%d%d",&pos[i],&num[i]);
            sum+=num[i];
        }
        double L = 0,R = sum*D,mid,res;
        int Limit = 100;
        while(L+eps<R&&Limit--){
            mid = (L+R)/2;
            if (check(mid)) res = mid,R = mid-eps;
            else L = mid+eps;
        }
        printf("Case #%d: %.7lf\n",tcas,res);
        
    
    
    }
}
