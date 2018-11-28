#include <iostream>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	bool prime[1000000];
	for(int i=2;i<1000000;i++) prime[i] = true;
	prime[0] = prime[1] = false;
	for(int i=2;i<1000000;i++){
		if(!prime[i]) continue;
		for(int j=2*i;j<1000000;j+=i)
			prime[j] = false;
	}
	for(int test=1;test<=TEST;test++){
		int D, K; cin >> D >> K;
		int num[10];
		for(int i=0;i<K;i++) cin >> num[i];
		int end = 1;
		int ans = -1;
		int start = 0;
		for(int i=0;i<K;i++) start = max(start, num[i]+1);
		for(int i=0;i<D;i++) end *= 10;
		for(int i=start;i<end;i++){
			if(!prime[i]) continue;
			for(int A=0;A<i;A++){
				bool flag = true;
				if(K==1) flag = false;
				int B = (num[1]+i-(A*num[0])%i)%i;
				for(int l=1;l+1<K;l++)
					if(num[l+1]!=(A*num[l]+B)%i) flag = false;
//				cout << i << " " << A << " " << B << endl;
//				int tmp = num[0]; cout << num[0] << " " ;
//				for(int l=0;l+1<K;l++) { tmp = (A*tmp+B)%i; cout << tmp << " "; }
//				cout << endl;
				if(flag){
					if(ans == -1) ans = (A*num[K-1]+B)%i;
					else if(ans != (A*num[K-1]+B)%i) ans = -2;
				}
			}
		}
		if(ans < 0) printf("Case #%d: I don't know.\n", test);
		else        printf("Case #%d: %d\n", test, ans);
	}
}
