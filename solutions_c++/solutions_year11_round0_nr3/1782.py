#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin >> T;
	for(int q=0;q<T;q++){
		int n;
		cin >> n;
		int s=0;
		int x=0;
		int m=1e7;
		for(int i=0;i<n;i++){
			int k;
			cin >> k;
			x^=k;
			s+=k;
			m=min(m,k);
		}
		cout << "Case #" << q+1 << ": ";
		if(x==0){
			cout << s-m << endl;
		}
		else{
			cout << "NO\n";
		}
	}
	return 0;
}