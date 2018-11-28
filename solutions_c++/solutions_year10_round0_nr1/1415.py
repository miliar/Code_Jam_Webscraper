#include<iostream>
#include<cstdio>
using namespace std;

typedef long long ll;

int main(){
	ll runs  , n , k;
	int cont = 1;
	cin >> runs;
	while(runs--){
		cin >> n >> k;
		if((k&((1<<n)-1)) == (1<<n)-1) printf("Case #%d: ON\n",cont++);
		else printf("Case #%d: OFF\n",cont++);
	}
	return 0;
}