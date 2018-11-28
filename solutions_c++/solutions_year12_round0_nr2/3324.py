#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long

int cnt[50];
int ans[50][50][3];
int a[50];

int main() {
    memset(cnt,0,sizeof(cnt));
    for (int i=0; i<=10; i++){
        for (int j=0; j<=10; j++){
            for (int k=0; k<=10; k++){
                if (abs(i-j)<=2 && abs(i-k)<=2 && abs(j-k)<=2) {
                    int tmp=i+j+k;
                    ans[tmp][cnt[tmp]][0]=i;
                    ans[tmp][cnt[tmp]][1]=j;
                    ans[tmp][cnt[tmp]][2]=k;
                    cnt[tmp]++;
                }
            }
        }
    }
    /*for (int i=0; i<=30; i++){
        cout << i <<":" << endl;
        for (int j=0; j<cnt[i]; j++){
          for (int k=0; k<3; k++) cout << ans[i][j][k] << " ";
          cout << endl;
        }
    }*/
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T,Cas=0;
    int n,s,p;
    int ans1;
    bool flag,flag1;
    cin >> T;
    while (T--){
        ans1=0;
        cin >> n >> s >> p;
        for (int i=0; i<n; i++) cin >> a[i];
        sort(a,a+n);
        for (int i=0; i<n; i++){
            flag=false; //判断是否有大于等于p的三元组
            flag1=false; //是否存在>=p的不奇异的三元组
            for (int j=0; j<cnt[a[i]]; j++){
                int p1,p2,p3;
                p1=ans[a[i]][j][0];
                p2=ans[a[i]][j][1];
                p3=ans[a[i]][j][2];
                int tmp=max(p1,max(p2,p3));
                if (tmp>=p) {
                    if ((abs(p1-p2)==2 || abs(p1-p3)==2 || abs(p2-p3)==2) && s>0){
                         {flag=true; flag1=true;}
                    }
                    else if ((abs(p1-p2)<=1 && abs(p1-p3)<=1 && abs(p2-p3)<=1)){flag=true; flag1=false; break;} 
                }               
            }
            if (flag){
                ans1++;
                if (flag1) s--;
            }
        }
        Cas++;
        printf("Case #%d: ",Cas);
        cout << ans1 << endl;
    }
    return 0;
}
/*
100
3 1 5 15 13 11
3 0 8 23 22 21
2 2 5 14 11
2 0 10 30 30
1 1 0 22
3 0 3 14 6 5
1 0 0 30
2 0 1 7 17
2 2 5 20 28
1 0 8 0
2 1 3 5 5
3 1 9 24 24 24
1 0 9 14
1 1 4 18
1 1 9 4
2 0 9 14 19
2 0 9 15 27
1 0 7 17
1 0 8 20
2 2 3 26 3
2 0 3 4 18
1 0 10 12
3 0 7 18 30 13
2 0 3 26 6
2 0 8 3 15
2 0 10 26 26
1 1 6 13
2 0 8 20 15
2 2 0 27 6
3 0 0 0 0 0
1 0 6 28
1 0 10 27
3 0 2 26 2 3
3 0 10 26 26 12
2 2 7 2 20
3 0 8 15 30 0
3 0 9 16 14 24
2 0 9 23 23
3 0 4 28 24 17
2 0 9 26 13
1 0 6 15
3 1 8 6 21 20
3 1 9 24 24 23
2 0 8 27 10
2 0 7 10 0
3 2 9 24 6 14
2 0 1 0 0
1 0 10 26
2 2 7 20 14
3 1 3 13 9 19
3 2 0 18 7 13
3 3 1 22 21 22
1 0 4 18
3 2 4 13 14 26
3 0 10 27 27 6
2 0 9 23 24
1 0 5 11
1 0 6 22
1 0 9 23
3 3 2 3 6 21
3 2 2 9 8 11
3 0 10 26 20 13
1 0 9 23
2 0 4 9 8
3 0 9 23 5 21
1 1 7 14
3 1 5 21 22 25
3 0 10 26 8 25
2 0 7 15 18
3 0 5 23 11 17
1 0 4 30
3 1 10 26 27 3
2 1 7 13 26
3 0 3 24 6 6
2 1 4 8 9
1 0 0 30
2 0 3 20 15
2 0 7 18 8
2 2 8 16 19
1 0 3 5
2 0 9 19 0
1 0 1 16
3 3 2 19 19 10
1 0 8 20
3 3 5 2 18 15
2 0 0 30 30
3 1 1 27 21 30
1 1 5 27
1 1 7 2
1 0 7 17
1 1 3 7
2 0 4 1 8
2 1 4 16 27
2 2 8 18 3
3 0 6 1 15 15
1 1 5 17
2 2 9 18 4
2 2 3 22 21
3 2 1 0 11 16
2 0 4 29 25
 */
