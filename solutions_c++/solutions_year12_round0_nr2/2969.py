#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
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
#include <stdio.h>
#include <string.h>
#define INF 2000000000
using namespace std;

#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))
int main(){
    freopen("B-large.in","r",stdin);
    freopen("solution.out","w",stdout);
    int cas;
    cin>>cas;
    int N,S,p, res, aux;
    for(int i=1; i<=cas; i++){
        res=0;
        //vector<int>num;
        cin>>N>>S>>p;
        for(int j=0; j<N; j++){
            cin>>aux;
            if(aux>=p+2*(max(0,(p-1)))){
                res++;
            }else if(S && aux>=p+2*max(0,(p-2))){
                res++;
                S--;
            }
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }

return 0;
}
