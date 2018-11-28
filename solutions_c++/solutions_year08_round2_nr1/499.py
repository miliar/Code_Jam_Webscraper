#include <iostream>

using namespace std;

const int maxN = 10;
const int maxn = 100000;

int main()
{
	int N,n;
	long long A,B,C,D,x0,y0,M,x, y, cnt,c;
	long long X[3][3];

	cin >> N;
	for(int i=1; i<=N; i++){
		/************************************
			Input Data
		*************************************/
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		/************************************
			Solve the Problem
		*************************************/
		memset(X,'\0',sizeof(X));
		x = x0;	y = y0;
		X[x % 3][y % 3]=1;
		for(int j=1; j<n; j++) {
			x = (A*x+B) % M;
			y = (C*y+D) % M;
			X[x % 3][y % 3]++;
		}
		cnt = 0;
		// all are different by one coord. and the same by another
		for(int k=0; k<3; k++){				
			cnt+=X[k][0]*X[k][1]*X[k][2];
		}
		for(int k=0; k<3; k++){
			cnt+=X[0][k]*X[1][k]*X[2][k];
		}
		// all are of the same type
		for(int k=0; k<3; k++)
		for(int l=0; l<3; l++){
			if(X[k][l]>2) {
				c = X[k][l];
				cnt+=c*(c-1)*(c-2)/6;
			}
		}
		// different by both coord.
		cnt+= X[0][0]*X[1][1]*X[2][2];
		cnt+= X[0][0]*X[1][2]*X[2][1];
		cnt+= X[1][0]*X[0][1]*X[2][2];
		cnt+= X[1][0]*X[0][2]*X[2][1];
		cnt+= X[2][0]*X[0][2]*X[1][1];
		cnt+= X[2][0]*X[0][1]*X[1][2];
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << i << ": " << cnt << endl;
		/* Debug
		cout << "----------------\n";
		for(int j=0; j<n; j++)
			cout << X[j] << " " << Y[j] << endl;
		cout << "----------------\n";
		*/
	}
	return 0;
}

