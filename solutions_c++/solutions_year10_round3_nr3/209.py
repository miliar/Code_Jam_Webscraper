/*
 * Round1C_C.cpp
 *
 *  Created on: 2010/05/23
 *      Author: haru
 */

#include "Round1C_C.h"

#include <iostream>
#include <vector>

using namespace std;

typedef vector<int>  VI;
typedef vector<VI>  VVI;

int hex(char ch){
	if( '0' <= ch && ch <= '9' ) return ch - '0';
	return ch - 'A' + 10;
}

Round1C_C::Round1C_C() {
	// TODO Auto-generated constructor stub
	int T;
	cin >> T;
	for(int i=1;i<=T;i++){
		int M, N;
		cin >> M >> N;
		VVI b(M, VI(N, 0));
		VVI tb(M, VI(N, -1));
		for(int j=0;j<M;j++){
			string s;
			cin >> s;
			for(int k=0;k<N/4;k++){
				int v = hex(s[k]);
				for(int l=0;l<4;l++){
					b[j][k*4+3-l] = v%2;
					v /= 2;
				}
			}
		}
		/*
		for(int r=0;r<M;r++){
			for(int c=0;c<N;c++){
				cout << b[r][c];
			}
			cout << endl;
		}
		*/
		tb = b;

		VI ans(min(M,N)+1, 0);
		int smax = 1;
		for(int r=0;r<M;r++){
			for(int c=0;c<N;c++){
				//if( b[r][c] == -1 )continue;
				int s;
				for(s=2;r+s-1<M&&c+s-1<N;s++){
					int bad = 0;
					for(int t=0;t<s;t++){
						int cr = r + s - 1;
						int cc = c + t;
						if( b[cr][cc] == b[cr-1][cc] ){
							bad = 1;
							break;
						}
					}
					if( bad )break;
					for(int t=0;t<s;t++){
						int cr = r + t;
						int cc = c + s - 1;
						if( b[cr][cc] == b[cr][cc-1] ){
							bad = 1;
							break;
						}
					}
					if( bad )break;
				}
				s--;
				if( smax < s ) smax = s;
				//cout << r << " " << c << " " << s << endl;
				//ans[s]++;
				tb[r][c] = s;
			}
		}

		/*
		for(int r=0;r<M;r++){
			for(int c=0;c<N;c++){
				cout << tb[r][c];
			}
			cout << endl;
		}
		*/

		for(int s=smax;s>=1;s--){
			for(int r=0;r<M;r++){
				for(int c=0;c<N;c++){
					if( tb[r][c] >= s ){
						int bad = 0;
						for(int rr=r;rr<r+s;rr++){
							for(int cc=c;cc<c+s;cc++){
								if( b[rr][cc] == 2 ){
									bad = 1;
									break;
								}
							}
							if( bad )break;
						}
						if( !bad ){
							ans[s]++;
							for(int rr=r;rr<r+s;rr++){
								for(int cc=c;cc<c+s;cc++){
									b[rr][cc] = 2;
								}
							}
						}
					}
				}
			}
			/*
			cout << "size: " << s << endl;
			for(int r=0;r<M;r++){
				for(int c=0;c<N;c++){
					cout << b[r][c];
				}
				cout << endl;
			}
			*/
		}
		cout << "Case #" << i << ": ";
//		cout << ans;
		int cnt = 0;
		for(int i=ans.size()-1;i>=0;i--){
			if( ans[i] > 0 )cnt++;
		}
		cout << cnt << endl;
		for(int i=ans.size()-1;i>=0;i--){
			if( ans[i] > 0 ){
				cout << i << " " << ans[i] << endl;
			}
		}
		//cout << endl;
	}

}

Round1C_C::~Round1C_C() {
	// TODO Auto-generated destructor stub
}
