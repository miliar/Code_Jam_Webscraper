# include <iostream>
# include <cstdio>
# include <algorithm>
# include <cmath>
# include <string>
# include <vector>
using namespace std;



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TT;

	cin >> TT;
	


	for(int tt = 1; tt <= TT; tt++){

		int k, len,ans = 1000000;
		char text[2000];
		char tmp[2000];
		cin >>k >> text;

		int K[10];
		for(int i = 0; i < k; i++){
			K[i] = i;
		}
		len = strlen(text);

		do{


		for(int j = 0; j < len; j += k){
			for(int i = 0; i < k; i++){
					tmp[j+i] = text[j+K[i]];
			}
		}
	
		int sum = 1;

		for(int i = 1; i < len; i++){
			if(tmp[i] != tmp[i-1]) sum++;
		}

		ans= min(ans,sum);

		}while(next_permutation(K,K+k));
		
	
	 cout << "Case #" << tt <<": " << ans << endl;
	}




}

