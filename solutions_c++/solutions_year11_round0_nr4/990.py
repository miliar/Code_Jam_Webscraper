#include<iostream>

using namespace std;

int main(){
	int test, n, aux, ans;
	
	cin >> test;
	for(int t=1;t<=test;t++){
		cin >> n;
		ans=0;
		
		for(int i=1;i<=n;i++){
			cin >> aux;
			if(aux != i) ans++;
		}
		
		cout << "Case #" << t << ": " << ans << ".000000\n";
	}
	
	return 0;
}
