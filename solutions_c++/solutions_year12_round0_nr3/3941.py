#include <iostream>
#include <cstring>

using namespace std;


const int MAX_POW = 10;
int ten_power[MAX_POW];

int get_pow(int x){
	int pow = 0;
	while(x>=ten_power[pow])
		++pow;
	return pow;
}

int rotate(int x, int pow){
	return x/10 + x%10*ten_power[pow-1];
}

bool valid_rotate(int x){
	return x%10;
}

bool visited[2000000+1];

int main(){
	ten_power[0]=1;
	for(size_t i=1; i<MAX_POW; ++i){
		ten_power[i] = ten_power[i-1]*10;
	}


	size_t T = 5;
	cin >> T;

	for(size_t Ti=1; Ti<=T; ++Ti){
		memset(visited, 0, sizeof(visited)/sizeof(*visited));
		int A, B;
		cin >> A >> B;
		long long unsigned int ans = 0;

		for(int x=A; x<=B; ++x){
			if(!visited[x]){
				visited[x]=true;
				long long unsigned int count = 1;
				int p = get_pow(x);
				for(size_t i=0; i<p; ++i){
					bool valid = valid_rotate(x);
					x = rotate(x, p);
					valid = valid && x>=A && x <= B && !visited[x];
					if(valid){
						++count;
						visited[x] = true;
					}
				}
				ans += count * (count-1) / 2;
			}
		}
		cout << "Case #" <<Ti << ": " << ans << '\n';
	}
}
