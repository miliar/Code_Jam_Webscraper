#include <iostream>
#include <string>

using namespace std;

int N, M, A;

void work() {
	for(int x2=0; x2<=N; x2++)
		for(int x3=x2; x3<=N; x3++)
			for(int y2=0; y2<=M; y2++) {
				int my3 = M;
				if(y2*x3 < M*x2)
					my3 = y2*x3/x2;
				for(int y3=0; y3<=my3; y3++)
					if(x2*y2 + (x3-x2)*(y2+y3) - x3*y3 == A) {
						cout <<"0 0 " <<x2 <<" " <<y2 <<" " <<x3 <<" " <<y3 <<endl;
						cerr <<x2*y2 + (x3-x2)*(y2+y3) - x3*y3 <<endl;
						return;
					}
			}
	cout <<"IMPOSSIBLE" <<endl;
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>N >>M >>A;
		cout <<"Case #" <<i+1 <<": ";
		work();
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/