/*
TASK: park
LANG: C++
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <algorithm>
#define foreach(_v,_c) for( typeof((_c).begin()) _v = (_c).begin() ; _v != (_c).end() ; ++_v )

using namespace std;

const int MAXN = 1000;

/**
N -> Number of groups
K -> max people
R -> Number of runs
*/

int N,K,R;
int g[MAXN << 1];
int next[MAXN];
long long sums[MAXN];
int used[MAXN];
long long sofar[MAXN];
int prenum[MAXN];

void process(){
    memset( next , 0 , sizeof( next ) );
    memset( sums , 0 , sizeof( sums ) );
    memset( used , 0 , sizeof( used ) );
    
    for( int i = 0 ; i < N ; i++ ){
        /// this starts at i
        if( g[i] > K ){
            next[i] = -1;
            continue;
        }
        
        int sum = g[i];
        int j;
        for( j = i+1 ; j < N+i and sum+g[j] <= K ; j++ ){
            sum += g[j];
        }
        //printf("From %d sum is %d( stopped at %d )\n", i , sum , j%N );
        next[i] = j % N;
        sums[i] = sum;
    }
}

int cyclebefore;
int cyclefrom;
int cyclelen;
int visitnumber;
int euros;

void dfs( int vertex , long long parentsum = 0 ){
    used[vertex] = 1;
    prenum[vertex] = visitnumber++;
    sofar[ vertex ] = parentsum;
    //printf("Vertex %d :: visit num %d, sum of %d\n", vertex , visitnumber-1 , parentsum);
    if( !used[ next[vertex] ] ){
        dfs( next[vertex] , sofar[vertex]+sums[vertex] );
    }else{
        cyclebefore = prenum[ next[vertex] ] - prenum[0];
        cyclelen = 1+prenum[vertex] - prenum[ next[vertex] ];
        cyclefrom = vertex;
    }
}

int main(){
	freopen("park.in","r",stdin);
	freopen("park.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 0 ; i < T ; i++ ){
        scanf("%d%d%d",&R,&K,&N);
        cyclebefore = 0;
        cyclefrom = 0;
        cyclelen = 0;
        visitnumber = 0;
        for( int j = 0 ; j < N ; j++ ){
            int current;
            scanf("%d",&current);
            g[j] = g[j+N] = current;
            //printf("%d ",current);
        }
        //printf("\n");
        process();
        for( int i = 0 ; i < N ; i++ ){
            //printf("%d ",next[i]);
        }
        //printf("\n");
        if( next[0] == -1 ){
            //printf("Impossible...\n");
            printf("0\n");
        }else{
            dfs(0);
            //printf("Before the cycle %d\n", sofar[ next[cyclefrom] ] - sofar[0] );
            //printf("Found the cycle( from %d, end is %d, total length %d, one-time-run %d )\n", next[cyclefrom], cyclefrom, cyclelen, sofar[ cyclefrom ]-sofar[ next[cyclefrom] ]+sums[ cyclefrom ] );
            
            int X = prenum[ next[cyclefrom] ] - prenum[0];
            int Y = cyclelen;
            long long cyclecost = sofar[ cyclefrom ]-sofar[ next[cyclefrom] ]+sums[cyclefrom];
            
            long long answer;
            
            /// X + A*Y + S = R
            /// IF X >= R it's okay
            
            //printf("Gotta ride %d times. X = %d , Y = %d\n",R,X,Y);
            
            if( R <= X ){
                int at = 0;
                for( int j = 0 ; j < R ; j++ ){
                    answer += sums[at];
                    at = next[at];
                }
            }else{
                R -= X;/// A*Y + S = R-X, so S = (R-X) % Y, A = (R-X)/Y
                int S = R%Y;
                int A = R/Y;
                
                //printf("Should do %d cycles and next %d one-timers\n", A,S);
                
                answer = 0;
                
                int at = 0;
                for( int j = 0 ; j < X ; j++ ){
                    answer += sums[at];
                    at = next[at];
                }
                
                //printf("Ready to start cycling, answer so far %d\n",answer);
                
                answer += A*cyclecost;
                
                //printf("Cycling done... answer so far %d\n", answer );
                
                at = next[cyclefrom];
                
                for( int j = 0 ; j < S ; j++ ){
                    answer += sums[at];
                    at = next[at];
                }
                
                //printf("Done.. final answer :: %d\n", answer );
                
            }
            //printf("Answer is %d\n", answer);
            cout << "Case #"<<i+1<<": "<<answer<<endl;
        }
	}
	return 0;
}
