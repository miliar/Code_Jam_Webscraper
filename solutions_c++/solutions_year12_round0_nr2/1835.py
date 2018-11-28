#include<iostream>
using namespace std;


int main() {
	int T;
	cin>>T;
	int*count = new int[T];
	for (int j=0;j<T;j++) {
		cin>>ws;
		int N,S,p;
		cin>>N>>S>>p;
		int *t = new int [N];
		for (int i=0;i<N;i++)
			cin>>t[i];
	
		int *r = new int[N];
		int *q = new int[N];
		count[j] = 0;
		for (int i=0;i<N;i++){
			r[i] = t[i]%3;
			q[i] = t[i]/3;
			if (q[i] >= p || (q[i] == p-1 && r[i] >= 1))
				count[j]++;
			else if (q[i] == p-1 && S>0 && (p-2)>=0) {
				count[j]++;
				S--;
			}
			else if (q[i] == p-2 && r[i]>=2 && S>0) {
				count[j]++;
				S--;
			}
		}
		
	}
	for (int i=0;i<T;i++)
		cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
	return 0;
}
