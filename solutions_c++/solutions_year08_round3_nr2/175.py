#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdio.h>
using namespace std;

long long ans;
long long result;
void divide(char *in, int start, int len){
	long long v = 0;
	char tmp[14] = "";
	if(start >= len){
		long long tmp = result;
		if(tmp % 2 == 0 || tmp % 3 == 0 || tmp % 5 == 0 || tmp % 7 == 0){
			ans++;
			return;
		}
	}
	for(int i = 0; i < len - start; i++){
		strncpy(tmp, in + start, i + 1);
		sscanf(tmp, "%lld", &v);
		result += v;
		divide(in, start + i + 1, len);
		result -= v;
		if(start == 0){
			continue;
		}
		result -= v;
		divide(in, start + i + 1, len);
		result += v;
	}
	return;
}

int main(){
	int N;
	cin >> N;
	for(int times = 1; times <= N; times++){
		char in[14];
		cin >> in;
		ans = 0;
		result = 0;
		divide(in, 0, strlen(in));

		cout << "Case #" << times << ": " << ans << endl;
	}
	return 0;
}
