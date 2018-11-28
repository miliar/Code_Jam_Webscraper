#include <iostream>
#include <cstring>

#define MAX 1010

using namespace std;

int test, t = 1, n;
int res, aux;

int main(){
	ios_base::sync_with_stdio(false);
	
	cin >> test;
	while (test --){
		cin >> n;
		res = 0;
		for (int i=1; i<=n; i++){
			cin >> aux;
			if (aux != i) res++;
		}
		
		cout << "Case #" << t++ << ": " << res << ".000000\n";
	}
	return 0;
}