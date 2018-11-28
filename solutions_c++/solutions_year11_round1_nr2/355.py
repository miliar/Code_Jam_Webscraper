#include<iostream>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<set>
using namespace std;
const int N = 10005;

vector<int>pos[N][26];
char a[N][12];
char b[30];
set<int>res;
int vis[N];
 
inline void get( int id ) {
       int i , j;
       for( i = 0 ; i < 26;i++ ){
            pos[id][i].clear();
       }
       for( i = 0 ; i < strlen( a[id] ) ; i++ ) {
            pos[id][ a[id][i]-'a' ].push_back( i );
       }
}

inline int isnot( int x,int y,int val) {
       if( pos[x][val].size() != pos[y][val].size()) return 1;
       int i , size = pos[x][val].size();
       for( i = 0 ; i < size;i++ ) {
            if( pos[x][val][i] != pos[y][val][i] ) 
                return 1;     
       }
       return 0;
}

inline int calc( int id,int n  ){
       int i , j , len = strlen( a[id] );
       res.clear();
       memset( vis, 0 ,sizeof( vis)); 
       for( i = 0 ; i < n;i++ ) {
            if( len == strlen( a[i] ) ) {
                res.insert( i );
            }
       }
       int ans = 0;
       for( i = 0 ; i < 26;i++ ) {
            int tmp = b[i] - 'a' , flag = 0;
            
            
            //if( (int)res.size() == 1 ) break;
            //printf("%c %d\n",b[i] , tmp );
            int count = 0;
            for( set<int>::iterator it = res.begin() ; it != res.end() ; it++ ) {
                 if( vis[*it] == 0 ) count++;
                 if( pos[ *it ][tmp].size() && vis[*it] == 0 ) {
                     flag = 1; 
                 }
            }
            if( count == 1 ) break; 
            if( flag == 0 ) continue;
            
           // printf("flag = %d\n",flag);
            
            for( set<int>::iterator it = res.begin() ; it != res.end() ; it++ ) {
                 //set<int>::iterator tmpit = it;
                 if( isnot( *it ,id , tmp) ) {
                     //res.erase( it );
                     //it = tmpit;
                     vis[*it] = 1;
                 }
            }
            if( pos[id][tmp].size() == 0 ) ans++;
       } 
       return ans;
}

inline int solve( int n ){
       int min = -1, ans = -1;
       for(int i = 0 ; i < n;i++ ) {
            int tmp = calc( i , n );
            if( tmp > min ) {
                min = tmp ; ans = i;
            }
       }
       return ans;
}

int main() {
    int test , i , j , n , m ,tc = 1;
    
    freopen("s.in","r",stdin);
    freopen("s.out","w",stdout);
    
    scanf("%d",&test);
    while( test-- && scanf("%d%d",&n,&m) != EOF ) {
           for( i = 0 ; i < n;i++) {
                scanf("%s",a[i]);
                get( i );
           }
           printf("Case #%d:",tc++); 
           for( i = 0 ; i < m;i++ ) {
                scanf("%s",b);
                int ans = solve(n);
                printf(" %s",a[ans]);
           }
           puts("");
    }
    return 0;
}
