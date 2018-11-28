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
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


/*  
bool arr[N];  
void getprim(){ arr[0]=1;arr[1]=1;int i;long long j;for(i=2;i<N;i++){if(arr[i]==0){ for(j=i,j=j*i;j<N;j+=i){arr[j]=1;}}}}  
*/  
//priority_queue  
//lower_bound,upper_bound  
//#define vs vector<string>
//#define N 4500005
//#define vi vector<int>
//typedef long long ll;
//next_permutation

//bool cmp(int a,int b)//从小到大
//{
//	return a<b;
//}typedef long long LL;#define N  1010100LL dis[N];LL cost[N];int ss[N];int main(){    freopen("1.in", "r", stdin);    freopen("out.txt", "w", stdout);    int T;    scanf("%d", &T);    for(int cas = 1; cas <= T; cas++){               int l, n, c;        long long t;        int cnt = 0, a[1010];;        scanf("%d%lld%d%d", &l, &t, &n, &c);        for(int i = 0; i < c; i ++){            scanf("%d", a+i);        }        bool xx = true;        for(int k = 0; xx; k ++){            for(int i = 0; i < c;i ++){                if(k * c + i >= n){                    xx = false;                    break;                }                dis[k * c + i] = a[i];            }        }        cost[0] = 0;        int po  = -1;        for(int i = 1; i <= n; i ++){            cost[i] = cost[i - 1] + dis[i-1];            if(cost[i] >= t/2 && po == -1) po = i;            else if(po != -1){                ss[cnt++] = dis[i-1];            }        }        ss[cnt++] = cost[po] - t/2;        sort(ss, ss+cnt);        LL ans = cost[n]*2;        while(cnt-- && l--){            ans -= ss[cnt];        }        printf("Case #%d: %lld\n", cas, ans);    }    return 0;}