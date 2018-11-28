#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

const int MAX_A = 3;

int main(){
	int T;
	// cin >> T;
	scanf("%d", &T);
	for(int t_ = 1 ; t_ <= T ; ++t_ ){
		double ans = 0;
		int A, B;
		double p[MAX_A];
		vector<double> Pr;
		
		//cin >> A >> B;
		scanf("%d %d", &A, &B);
		for(int i=0 ; i < A ; i++ ){
			//cin >> p[i];
			scanf("%lf", &p[i]);
		}
		for(int bits = 0 ; bits < (1 << A) ; bits++ ){
			double Pr_ = 1.0;
			int b = bits;
			
			for(int j=0 ; j < A ; j++ ){
				bool flag = b & (1 << (A-1));
				b <<= 1;
				Pr_ *= (flag)? 1.0 - p[j] : p[j];
			}
			// cout << Pr_ << endl;
			Pr.push_back( Pr_ );
		}
		
		{
			double E = 0.0;
			for(int i = 0 ; i < Pr.size() ; i++ ){
				E += Pr[i] * (B + 2);
			}
			// cout << E << endl;
			ans = E;
		}
		
		for(int i=0 ; i <= A ; i++ ){
			double E = 0.0;
			for(int bits = 0 ; bits < (1 << A) ; bits++ ){
				int k = B - A + 1 + 2*i;
				if( bits >= (1 << i) ){
					k += B + 1;
				}
				E += Pr[bits] * k;
			}
			ans = min( ans , E );
			// cout << E << endl;
		}
		
		//cout << "Case #" << t_ << ": " << ans << endl; 
		printf("Case #%d: %.6f\n", t_ , ans );
	}
}

