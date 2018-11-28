#include <iostream>
#include <string>

using namespace std;

int N, M;
int request[2000][2000];
int milk[2000];
int num_r[2000];
bool positive[2000];

bool solve() {
	while(true) {
		int i;
		for(i=0; i<M; i++)
			if(positive[i] && num_r[i] == 1)
				break;
		if(i==M)
			return true;

		for(int j=0; j<N; j++)
			if(request[i][j] == 1) {
				milk[j] = 1;
				for(int k=0; k<M; k++)
					if(request[k][j] == 0) {
						request[k][j] = -1;
						num_r[k] --;
						if(num_r[k] == 0)
							return false;
					}
			}
		positive[i] = false;
	}
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>N >>M;
		memset(request, -1, sizeof(request));
		memset(milk, 0, sizeof(milk));
		memset(positive, false, sizeof(positive));
		for(int j=0; j<M; j++) {
			int t;
			cin >>t;
			num_r[j] = 0;
			for(int k=0; k<t; k++) {
				int m, f;
				cin >>m >>f;
				if(request[j][m-1] == -1) {
					request[j][m-1] = f;
					num_r[j] ++;
				}
				else {
					cerr <<"duplicate " <<j <<" " <<m <<" " <<f <<endl;
					if(request[j][m-1] != f) {
						request[j][m-1] = -1;
						num_r[j] = 9999;
					}
				}
				if(f == 1)
					positive[j] = true;
			}
		}
		cout <<"Case #" <<i+1 <<":";
		if(solve()) {
			for(int j=0; j<N; j++)
				cout <<" " <<milk[j];
		}
		else
			cout <<" IMPOSSIBLE";
		cout <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/