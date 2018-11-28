# include <iostream>
# include <cstdio>
# include <algorithm>
# include <cmath>
# include <string>
# include <vector>
using namespace std;



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TT,state;

	cin >> TT;
	


	for(int tt = 1; tt <= TT; tt++){

		int N,M,A;
		long long x1,x2,y1,y2;
		cin >> N >> M >> A;
		state = 1;

		for(x1 = 0; x1 <= N && state ; x1++){
			for(x2 = 0; x2 <= N && state; x2++){
				for(y1 = 0; y1 <= M && state; y1++){
					for(y2 = 0; y2 <= M && state; y2++){
						if(x1*y2 - x2*y1 == A && state){
							cout << "Case #" << tt <<": " << x1 <<' ' << y1 << ' ' << x2 << ' ' << y2 <<" 0 0"<< endl;
							state = 0;
						}
					}
				}
			}
		}

		
		if(state){
			cout << "Case #" << tt <<": IMPOSSIBLE" << endl;
		}
	}




}

