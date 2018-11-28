#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int nt;
	cin>>nt;
	int * A = new int[100];
	int * B = new int[100];
	for (int it = 1; it <= nt; it++){
		cout<<"Case #"<<it<<": ";
		int n, s, p, count = 0;
		cin>>n>>s>>p;
		for (int i = 0; i < n; i++) cin>>A[i];
		sort(A, A + n);
		int used = 0, i, begin = 0; 
		for (i = 0; i < n; i++) if (A[i]/3 + 1 + (A[i] % 3 == 2) >= p) break;
		begin = i;
		for (; used < s && i < n; i++) {
			if (A[i] != 0) A[i] = A[i]/3 + 1 + (A[i] % 3 == 2);
			used++;
		}
		for (; i < n; i++) A[i] = A[i]/3 + (A[i] % 3 != 0);
		for (int i = begin; i < n; i++){
			if (A[i] >= p) count++;
		}
		cout<<count<<endl;
	}
	return 0;
}
