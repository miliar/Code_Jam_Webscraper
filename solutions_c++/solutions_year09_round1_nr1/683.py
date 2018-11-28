#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int nil = -1;

const int maxn = 100001;

bool visited[maxn];

bool judge(int num, int base){
	int i, j, k = num, len, tmp[50];
	memset(visited, 0, sizeof(visited));
	for(i = 0; k; i++){
		tmp[i] = k % base;
		k /= base;
	}
	len = i;
	visited[num] = true;
	while(true){
		k = 0;
		for(i = 0; i < len; i++){
			j = tmp[i] * tmp[i];
			k += j;
		}
		if(k == 1) return true;
		if(visited[k]) return false;
		visited[k] = true;
		for(i = 0; k; i++){
			tmp[i] = k % base;
			k /= base;
		}
		len = i;
	}
}		

bool end;

int my_scanf(){
	int ans = 0, i, j, k;
	char c;
	while(true){
		c = getchar();
		if(c >= '0' && c <= '9') break;
	}
	ans = c - '0';
	while(true){
		c = getchar();
		if(c < '0' || c > '9'){
			if(c == '\n') end = true;
			return ans;
		}
		i = c - '0';
		ans = ans * 10 + i;
	}
	return ans;
}

int main(){
	int max, t, i, j, k;
	vector<int> input;
	bool flag;
	scanf("%d\n", &t);
	for(k = 1; k <= t; k++){
		input.clear();
		end = false;
		while(true){
			i = my_scanf();
			input.push_back(i);
			if(end) break;
		}
		printf("Case #%d: ", k);
		i = 2;
		while(true){
			flag = true;
			for(j = 0; j < input.size(); j++){
				if(!judge(i, input[j])){
					flag = false;
					break;
				}
			}
			if(flag){
				printf("%d\n", i);
				break;
			}
			i++;
		}
	}
}
