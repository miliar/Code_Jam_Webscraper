#include<iostream>
using namespace std;

int main() {
    int T, C=1;
	cin >> T;
	while(T--) {
		int i, cnt, N, a[1000], sorted[1000];
	    cin >> N;
		for(i=0; i<N; i++) {
			cin>>a[i];
			int j;
			for(j=i-1; j>=0; j--) {
			    if(sorted[j] > a[i]) {
				    sorted[j+1] = sorted[j];
				} else {
				    break;
				}
			}
			sorted[j+1] = a[i];
			cerr<<"Inserted " << a[i] <<" in element " << j+1 << endl;
		}
		
		for(i=0, cnt=0; i<N; i++) {
		    cerr << sorted[i] << ' ';
		    if(sorted[i] != a[i]) {
			    cnt++;
			}
		}
		cerr << endl;
		
		cout<< "Case #" << C++ <<": "<< cnt << ".000000" << endl;
	}
}
