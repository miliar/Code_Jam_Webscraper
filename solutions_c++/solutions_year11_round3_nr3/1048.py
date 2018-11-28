#include <iostream>
using namespace std;

bool cek(int a, int b){
	int tmp;
	if (a<b){
		tmp = a;
		a = b;
		b = tmp;
	}
	
	return (a%b==0);
}

int main(){
	int t, n, h, l, in, o;
	
	cin >>t;
	
	for (int k = 1 ; k <= t ; k++){
		cin >>n >>l >>h;
		int ar[n];
		
		for (int i = 0 ; i < n ; i ++){
			cin >>ar[i];
		}
		
		bool can = false;
		
		for (int i = l ; i <= h ; i ++){
			for (int j = 0 ; j <= n ; j ++){
				if (j==n){
					can = true;
				}else if (!cek(i, ar[j])){
					break;
				}
			}
			
			if (can){
				o = i;
				break;
			}
		}
		
		printf("Case #%d: ", k);
		
		if (can)
			cout <<o <<endl;
		else
			cout <<"NO" <<endl;
	}
	
	return 0;
}
