#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX = 2000001;

int main(){
	static int v[MAX][6];
	for(int i=10;i<MAX;i++){
		int k=0;
		for(int j=1;j<7;j++){
			int a = i / (int)(pow(10.0,(double)j));
			if(a <= 0) break;
			int b = i % (int)(pow(10.0,(double)j));
			int c = (int)(log10((double)i * 10.0)) - j;
			c = (int)(pow(10.0,(double)c));
			int m = b * c + a;
			//cout << "i=" << i << " m=" << m <<" a=" << a <<" c=" << c << endl;
			if(i < m /*&& (int)log10((double)i) == (int)log10((double)m)*/){
				v[i][k++] = m;
				//cout << "(" << i << ", " << m << ")" << endl;
			}
		}
	}

	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int A, B, ans=0;
		cin >> A >> B;
		for(int i=A;i<=B;i++){
			for(int j=0;j<6;j++){
				if(v[i][j] && v[i][j] <= B){
					ans++;
				}
				else if(!v[i][j]) break;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}