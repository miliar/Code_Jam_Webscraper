#include <iostream>

using namespace std;

int power[] = {1,
               10,
               100,
               1000,
               10000,
               100000,
               1000000,
               10000000};

int main(void){
	//x / 10^3 + 10^3 * (x % 10^3) = y

	int T;
	cin >> T;

	for(int t=1; t<=T; t++){
		int A, B;
		cin >> A >> B;
		
		int n;
		for(n=0; n<7; n++){
			if(A / power[n] < 10)
				break;
		}
		
		int y = 0;
		for(int x=A; x<=B; x++){
			//cout << x << ": ";
			int xx = x;
			int yy = 0;
			for(int k=1; k<=n; k++){
				int z = xx / 10 + power[n] * (xx % 10);
				//cout << z << " ";
				if(z > x && z <= B)
					yy++;
				xx = z;
			}
			y += yy;
			//cout << " -> " << yy << endl;
		}
		
		cout << "Case #" << t << ": " << y << endl;
	}

	return 0;
}
