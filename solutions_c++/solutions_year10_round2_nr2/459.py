#include <iostream>

using namespace std;

int x[55];
int v[55];
int a[55];

int main(){
	int c;
	cin >> c;
	for(int f=1;f<=c;f++){
		int n,k,b,t;
		cin >> n >> k >> b >> t;
		cout << "Case #"<<f << ": ";
		for(int j=0;j<n;j++)
			cin >> x[j];
		for(int j=0;j<n;j++)
			cin >> v[j];
			
		int cnt = 0;
		for(int j=0;j<n;j++){
			if((b-x[j]-1)/v[j] +1 <= t){
				a[j] = 1;
				cnt++;
			}
			else a[j] = 0;
			//printf("!!!%d %d\n",j,a[j]);
		}
		if(cnt < k) {cout<<"IMPOSSIBLE"<<endl; continue;}
		
		
		cnt =0;
		for(int j=n-1;j>=n-k;j--){
			int i=j;
			while(a[i]!=1) {i--; cnt++;}
			int tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
		}
		cout << cnt << endl;
	}
	return 0;
}
