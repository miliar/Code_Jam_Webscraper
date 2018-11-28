#include<iostream>
using namespace std;

const int N = 100005;

int a[N];

struct node {
    int x,y;
};
node rec[N];

inline int lowbit(int x) {
    return (x&(-x));
}

inline void add( int id) {
    while( id <= N ) {
        a[id]++;
        id += lowbit(id);
    }
}

inline int get(int id) {
    int ans = 0 ;
    while( id > 0 ) {
      //  cout<<"id= "<<id<<" "<<a[id]<<endl;
        ans += a[id];
        id -= lowbit(id);
    }
    return ans;
}

bool cmp( node x,node y ){
    return x.x > y.x;
}


int main() {
  //  freopen("A-large.in","r",stdin);
   // freopen("A-bigout.txt","w",stdout);
    
    int test, i , n ,j ;
    scanf("%d",&test);
    for( int tc = 1; tc <= test; tc++ ) {
        scanf("%d",&n);
        memset(a,0,sizeof(a));
        
        for( i = 0 ; i < n;i++ ) {
            scanf("%d%d",&rec[i].x,&rec[i].y);
        }
        
        sort( rec,rec+n,cmp );
        
        int ans = 0;
        for( i = 0 ; i < n;i++ ) {
            ans += get( rec[i].y );
            add( rec[i].y );
        }
        printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}
