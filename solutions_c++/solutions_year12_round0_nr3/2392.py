#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstdio>
#include<string>
using namespace std;

int least[2000001];
int num[2000001];
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);
	int a, b;
	int t;
	cin >> t;
	for(int i = 1; i < 2000001; i++){
		int d = 1;
		int x = i;
		while(x){
			x /= 10;
			d *= 10;
		}
		d /= 10;
		least[i] = i;
		x = i;
		while(x % 10 == 0)
			x = x / 10 + (x % 10) * d;
		x = x / 10 + (x % 10) * d;
		while(x != i){
			least[i] = min(least[i], x);
			while(x % 10 == 0)
				x = x / 10 + (x % 10) * d;
			x = x / 10 + (x % 10) * d;
		}
	}
	for(int i = 0; i < t; i++){
		cin >> a >> b;
		int ans = 0;
		memset(num, 0, sizeof num);
		for(int i = a; i <= b; i++)
			num[least[i]]++;
		for(int i = 0; i <= b; i++)
			ans += num[i] * (num[i] - 1) / 2;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
			
