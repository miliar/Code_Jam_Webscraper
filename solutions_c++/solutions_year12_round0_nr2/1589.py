#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int t, n, s, p;
	
	cin >>t;
	
	for (int k = 1 ; k <= t ; k ++){
		cin >>n >>s >>p;
		int goo[n],	sum = 0;
		for (int i = 0 ; i < n ; i ++) cin >> goo[i];
		sort(goo, goo+n, greater<int>());
		
		for (int i = 0 ; i < n ; i ++){
			int pos = -1;
			
			if (goo[i] >= (p*3)-2){
				sum++;
			}else if (goo[i]%3==1 && goo[i]/3+1 >= p){
				sum++;
			}else if (goo[i]%3==2){
				pos = goo[i]/3+2;
			}else if (goo[i] == 0){
				pos = 0;
			}else{
				pos = goo[i]/3+1;
			}
			
			if (s>0 && pos >= p){
				s--;
				sum++;
			}
		}
		
		printf("Case #%d: %d\n", k, sum);
	}
	
	return 0;
}
