
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <queue>

using namespace std ;

typedef long long ll ;

ll gcd ( ll a, ll b ) { return b ? a : gcd(b, a%b) ; }
ll MAX ( ll a, ll b ) { return a > b ? a : b ; }
ll MIN ( ll a, ll b ) { return a < b ? a : b ; }
ll lcm ( ll a, ll b ) { return (a*b) / gcd(a,b) ; }

ll dist[1000001] ;

int main () {
	int Kases ;
	cin >> Kases ; 
	for ( int kases = 1 ; kases <= Kases ; kases ++ ) {
		ll L, t, N, C ;
		cin >> L >> t >> N >> C ;
		ll totalDist = 0 ; 
		for ( int i = 0 ; i < C ; i ++ ) { 
			scanf("%lld",dist+i ) ; 
			totalDist += dist[i] ;
			ll j = i+C ; 
			while ( j < N ) { 
				dist[j] = dist[i] ; 
				j += C ;
				totalDist += dist[i] ;
			}
		} 
		ll totalTime = 2*totalDist ; 
		ll current = 0 ;
		ll dist1 = 0 ;
		while ( current < N ) {
			if ( dist1 + 2*dist[current] <= t ) {
				dist1 += 2*dist[current] ;
				current ++ ; 
			} else { 
				priority_queue<ll> pQueue ;
				pQueue.push(dist[current]-((t-dist1)/2)) ;
			        for ( int star = current+1; star < N ; star++ ) {
					pQueue.push(dist[star]) ;
				}
				int boost = 0 ;
				while ( boost < L ) {
					if ( pQueue.empty()) {
						break ; 
					}
					totalTime -= pQueue.top() ; pQueue.pop() ;
					boost ++ ;
				}
				break ;
			}
		}
		
		printf("Case #%d: %lld\n", kases, totalTime ) ;
	}
	return 0 ;
}
