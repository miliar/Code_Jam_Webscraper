#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int n , a , l , h;
vector<int> v;

long long gcd( long long p , long long q ){
    if( q == 0 ) return p;
    return gcd( q , p%q );
}

void doit(int test){
    printf("Case #%d: ",test);
    v.clear();
    scanf("%d%d%d",&n,&l,&h);
    for(int i = 0 ; i < n ; i++){
        scanf("%d",&a);
        v.push_back(a);
    }
    int mini = 10000000;
    for(int i = l ; i <= h ; i++){
        int ct = 0;
        for(int j = 0 ; j < n ; j++){
            if( i % v[j] == 0 || v[j] % i == 0 ) ct++;
        }
        if( ct == n ){ printf("%d\n",i); return; }
    }
    puts("NO");
}

int main(){
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++) doit( i );
}
