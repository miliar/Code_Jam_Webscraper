#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;

const int maxn = 30;

char tmp[maxn];
int input[maxn];
int output[maxn];
int len;

void get_next(){
	int i, j, k, p, q;
	bool flag = true;
	for(i = len - 1; i > 0; i--){
		if(input[i] > input[i - 1]){
			flag = false;
			break;
		}
	}
	if(flag){
		for(k = len - 1; k >= 0; k--){
			if(input[k]) break;
		}
		output[0] = input[k];
		output[1] = 0;
		for(i = 2, j = len - 1; j >= 0; i++, j--){
			if(j == k) j--;
			output[i] = input[j];
		}
		len++;
		return;
	}
	for(j = i; j < len - 1; j++){
		if(input[j + 1] <= input[i - 1]) break;
	}
	for(k = 0; k <= i - 2; k++) output[k] = input[k];
	output[i - 1] = input[j];
	for(k = i, p = len - 1; k < len; k++, p--){
		if(p == j) output[k] = input[i - 1];
		else output[k] = input[p];
	}
}

void read_in(){
	int i, j, k;
	stack<int> s;
	gets(tmp);
	len = strlen(tmp);
	for(i = 0; i < len; i++){
		input[i] = tmp[i] - '0';
	}
}

void write(int cases){
	int i;
	printf("Case #%d: ", cases);
	for(i = 0; i < len; i++) printf("%d", output[i]);
	printf("\n");
}

int main(){
	int t, i;
	scanf("%d\n", &t);
	for(i = 1; i <= t; i++){
		read_in();
		get_next();
		write(i);
	}
}
		

