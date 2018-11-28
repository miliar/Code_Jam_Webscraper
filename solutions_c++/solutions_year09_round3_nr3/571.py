#include<cstdio>
#include<cstring>
#include<cmath>
#include<deque>
#include<vector>
#include<queue>
#include<string>
#include<set>
#include<map>
#include<algorithm>

#define MAXN 1001

#define ll long long
#define DIM int T , N , M , P , K ;
#define ITER int i , j , k  , l;
#define AUX int a , b , d , aux ;

using namespace std;

DIM
AUX
ITER

priority_queue <int , vector <int> , greater<int> > MaxHeap;
priority_queue <int> MinHeap;
deque <int> Deque;
queue <int> Q;
vector <int > V;

int mins = MAXN * MAXN ;

int A[MAXN];
int len;
char s[MAXN] , c;
bool in[MAXN];



int main ()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    scanf("%d\n",&T);
    
    for ( i = 1 ; i <= T ; ++i ) {
          
          int cost = 0;
          mins = MAXN * MAXN;

          
          scanf("%d %d",&P ,&N);
          
          while ( V.size()) V.pop_back();
          
          for( j = 1 ; j <= N ; ++j) {
               scanf("%d",&a); 
               V.push_back(a);
               }
          
          sort( V.begin() , V.end());
          
          
          
          do {
                
                  for( j = 1;  j <= P ; ++j)
                   in[j] = true;
                cost = 0;
                for( k = 0 ; k < N ; ++k) {
                     in[V[k]] = false;
                     l = V[k] , j = V[k];
                     l -- , j++;
                     
                     while ( in[l] == true && l >=1 ) l--;
                     while( in[j] == true && j <= P ) j++;
                     cost = cost + ( V[k] - l ) + ( j - V[k] ) - 2;
                     }
                     
                     if ( cost < mins ) mins = cost;
                }while ( next_permutation( V.begin() , V.end()) );
    
          printf("Case #%d: %d\n",i ,mins);
          }

                     
          
               
                
         
return 0;
}
