#include <iostream>

using namespace std;

int T, N, S, p, t[100];

int analyze(int n, int s, int p, int *t) {
	int count = 0;
	for(int i = 0; i < n; i++) {
		switch(t[i] % 3) {
			case 0: if(t[i]/3 >= p) 
					count++; 
				else if(s > 0 && ((t[i]/3) > 0) && ( (t[i]/3 + 1) >=p )) { 
					s--; 
					count++; 
				} 
				break;
			case 1: if( ((t[i]-1)/3 + 1 >= p) || ((t[i]-1)/3 >= p) )
					count++;
				else if(s > 0 && ((t[i]-1)/3 - 1 >= 0) && ((t[i]-1)/3 + 1 >= p)) {
					s--;
					count++;
				}
				break;
			case 2: if( ((t[i]-2)/3 + 1 >= p) || ((t[i]-2)/3 >= p))
					count++;
				else if(s > 0  && ((t[i]-2)/3 >= 0) && (((t[i]-2)/3 + 2) >= p) ) {
					s--;
					count++;
				}
				break;
		}
	}
	return count;
}

int main() {
	cin>>T;
	for(int i = 0; i < T; i++) {
		cin>>N;
		cin>>S;
		cin>>p;
		for(int j = 0; j < N; j++) {
			cin>>t[j];
		}
		cout<<"Case #"<<i+1<<": "<<analyze(N, S, p, t)<<endl;
	}
}
