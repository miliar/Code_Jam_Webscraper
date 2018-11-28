#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

vector<int> v;

void doit(int test){
    int t ,a, suma = 0;
    int arr[1001];
    memset(arr,0,sizeof(arr));
    v.clear();
    scanf("%d",&t);
    for(int i = 0 ; i < t ; i++){
        scanf("%d",&a);
        v.push_back(a);
    }
    int c = v[0];
    for(int i = 1 ; i < v.size() ; i++) c = c^v[i];
    if( c != 0 ){
        printf("Case #%d: NO\n",test);
        return;
    }
    sort(v.begin() , v.end() );
    for(int i = 0 ; i < v.size() ; i++){
        arr[i] = suma + v[i];
        suma += v[i];
    }
    for(int i = 1 ; i < v.size() ; i++){
        int p = v[0] , q = v[i];
        for(int j = 1 ; j < i ; j++){
            p = p ^ v[j];
        }
        for(int j = i+1 ; j < v.size() ; j++){
            q = q ^ v[j];
        }
        if(p == q){
            printf("Case #%d: %d\n",test,suma-arr[i-1]);
            return;
        }
    }
    return;
}

int main(){
    int n;
    scanf("%d",&n);
    for(int i = 0 ; i < n ; i++) doit(i+1);
}
