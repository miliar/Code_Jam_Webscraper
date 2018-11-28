#include<iostream>
#include<map>
#include<vector>
#include<list>
#include<sstream>

using namespace std;

unsigned int g[1000];


int main(){

	int t;
	cin >> t;

	for(int i=0;i<t;++i){
		unsigned int r, k, n;
		unsigned long long result = 0;
		cin >> r >> k >> n;
		for(int j=0;j<n;++j) cin >> g[j];

		unsigned long long num = 0;//number of people riding
		unsigned int num_group = 1;//number of group riding
		unsigned long long num_per_loop = 0; // number of people can ride per loop
		int one_loop = r+1;
		for(int j=0, l=0;j<r;++j){
			for(;;++l,++num_group){
				if(l >= n) l=0;
				num += g[l];
				if(num > k){ // leaving
					num -= g[l];
					num_per_loop += num;
					num = 0;
					num_group = 0;
					break;
				}else if(num_group == n){
					num_per_loop += num;
					//cout << num_per_loop << endl;
					num = 0;
					num_group = 0;
					l = 0;
					break;
				}
			}
			if(l == 0){ // loop end
				one_loop = j+1;
				break;
			}
			num=0;
		}

		num = 0;
		num_group = 0;

		unsigned int num_loop = r / one_loop;

		//cout << "num_per_loop: " << num_per_loop << endl;
		//cout << "num_loop: " << num_loop << endl;
		
		unsigned int mod = r % one_loop;
		result = num_loop * num_per_loop;
		for(int j=0, l=0;j<mod;++j){
			for(;;++l){
				if(l >= n) l=0;
				num += g[l];
				if(num > k){ // leaving
					num -= g[l];
					result += num;
					num = 0;
					break;
				}
			}
		}
		result += num;

		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}
