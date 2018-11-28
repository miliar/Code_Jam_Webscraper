#include<cstdio>
/*
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
#define Dimensiuni int T , N , M , P , K ;
#define Iteratori int i , j , k ;
#define Auxiliare int a , b , c , d ;

using namespace std;

Dimensiuni
Auxiliare
Iteratori

priority_queue <int , vector <int> , greater<int> > MaxHeap;
priority_queue <int> MinHeap;
deque <int> Deque;
queue <int> Q;
vector <int > v;

*/

int T , N , i , j , k , a , b;

int cifre[10] , cifre2[10];


void process ( int a ) {

     int aux = a;
     
     while ( aux ) {
           cifre[aux % 10] ++;
           aux /= 10;
           }

}

bool check ( int a ) {
     
     int i;
     int aux = a;
     
     while ( aux )  {
           cifre2[aux % 10] ++;
           aux /= 10;
           }
     for( i = 1 ; i <= 9 ; ++i)
          if( cifre[i] != cifre2[i] ) return false;

return true;
          
}



/*
int number ( vector < int >  v)   {
    
    Iteratori
    Auxiliare
    
    for( i = 0 ; i < v.size() ; ++i)
         a = a * 10 + v[i];
         
    return a;
}
*/
int main ()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    scanf("%d",&T);
    
    for(j = 1 ;j <= T ; ++j) {
           
           scanf("%d",&a);
           
           for( i  = 0 ; i <= 9 ; ++i)
               cifre[i] = cifre2[i] = 0;
           
           process(a);
           
             
             for( i = 0 ; i <= 9 ; ++i)
                  cifre2[i] = 0;
             
             b = a;
             
             while ( !check(a) || a == b) {
                   
                   a++;
                   for( i = 0 ; i <= 9 ; ++i)
                    cifre2[i] = 0;
                  }
           printf("Case #%d: %d\n",j,a);
           
           //while ( v.size()) v.pop_back();
           
           }
    
         
return 0;
}
