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
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define EPS 1e-9

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

int n,w,l;

int main(){
    int t;
    cin >> t;
    for(int k=1;k<=t;k++){
        srand(time(NULL));
        cin >> n >> w >> l;
        int r[n];
        for(int i=0;i<n;i++){
            cin >> r[i];
        }
        double x[n], y[n];
        while(1){
            for(int i=0;i<n;i++){
                x[i] = ((double)rand() / ((double)RAND_MAX + 1)) * w - EPS; 
                y[i] = ((double)rand() / ((double)RAND_MAX + 1)) * l - EPS; 
            }

            bool isok = true;
            for(int i=0;i<n && isok;i++){
                for(int j=i+1;j<n && isok;j++){
                    if(!(sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) >= r[i]+r[j]+EPS)){
                        isok = false;
                    }
                }
            }
            if(isok) break;
        }
        printf("Case #%d: ", k);
        for(int i=0;i<n;i++){
            printf("%.3lf ", x[i]);
            if(i != n-1){
                printf("%.3lf ", y[i]);
            }else{
                printf("%.3lf\n", y[i]);
            }
        }
    }
}
