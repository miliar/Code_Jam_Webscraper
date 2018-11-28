#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

const int N = 105;

struct node {
       int g[N][N];
};

int dir[2][2] = {0,-1,-1,0} , n;

inline int check(node st ){
       int i , j;
       for( i = 1; i <= n;i++)
       for( j = 1; j <= n;j++)
            if( st.g[i][j] == 1 )
             return 0;
       return 1;

}

void out( node st ) {
       int i , j;
       for( i = 1; i <= n;i++) {
       for( j = 1; j <= n;j++)
            cout<<st.g[i][j]<<" ";
       cout<<endl;
       }
       cout<<endl;
}

inline int solve(node st ) {
     int ans = 0;
     int i , j ,k ;
     while( 1 ) {
            //out(st);
            if( check(st) )  break;
            
            node  next = st;
            
            for( i = 1; i <= n;i++)
            for( j = 1; j <= n;j++) {
                      if( st.g[i][j] == 0 && st.g[i-1][j] == 1 && st.g[i][j-1] == 1 ) next.g[i][j] = 1;
                      else if( st.g[i][j] == 1 && st.g[i-1][j] == 0 && st.g[i][j-1] == 0 )next.g[i][j] = 0;
                 
            }
            st = next;
            ans++;
     }
     return ans;
}


int main() {
   // freopen("c-small.in","r",stdin);
   // freopen("c-smallout.txt","w",stdout);
    
    int tc , test, i , j,k ;
    scanf("%d",&test);
    for( tc = 1;tc <= test;tc++ ) {
         scanf("%d",&n);
       //  if( tc == 45 ) cout<<n<<endl;
         node st;
         memset(st.g,0,sizeof(st.g));
         
         int num = 0;
         for( i = 0; i < n ;i++ ) {
              int x2, y2 ,x1,y1 ;
              scanf("%d%d%d%d", &y1, &x1, &y2, &x2 );
              //if( tc == 45 ) cout<<x0<<" " <<y0<<" "<<x1<<" "<<y1<<endl;

              for( j = x1 ;j <= x2;j++)
                   for( k = y1 ;k <= y2;k++)
                        st.g[k][j] = 1;
         }
         n = 100;
        // out(st);
         printf("Case #%d: %d\n",tc,solve(st));

    }
    return 0;
}
