#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <queue>
#include <map>
#include <stack>
using namespace std;

struct node{
	char name;
	int num;
}N[300];

int num_o[300];
int num_b[300];

int chang(int cnt, int s, char name, int pos){
	if (cnt == s)
		return pos;

	if (name == 'O'){
		if (num_b[s] > pos){
			pos += 1;
			return pos;
		}
		if (num_b[s] == pos)
			return pos;
		if (num_b[s] < pos){
			pos -= 1;
			return pos;
		}
	}

	else{
		if (num_o[s] > pos){
			 pos += 1;
			 return pos;
		}
		if (num_o[s] == pos)
			return pos;
		if (num_o[s] < pos){
			pos -= 1;
			return pos;
		}
	}
}

int main(){
	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	int n;
	int cas = 1;

	scanf("%d", &T);
	while (T--){

		scanf("%d", &n);
		int cnt_o = 0;
		int cnt_b = 0;

		for (int i = 0; i < n; i++){
			getchar();
			scanf("%c", &N[i].name);
			scanf("%d", &N[i].num);
			if (N[i].name == 'O')
				num_o[cnt_o ++] = N[i].num;
			else
				num_b[cnt_b ++] = N[i].num;
		}

		int s_o = 0;
		int s_b = 0;
		int ans = 0;
		int pos_o = 1;
		int pos_b = 1;

		for (int i = 0; i < n; i++){

			while (true){
				ans++;
				if (N[i].name == 'O'){
					if (pos_o == N[i].num){
						pos_b = chang(cnt_b, s_b, N[i].name, pos_b);
						//s_o++;
						break;
					}
					else if (pos_o < N[i].num){
							pos_o += 1;
							pos_b = chang(cnt_b, s_b, N[i].name, pos_b);
					}
					else{
						pos_b = chang(cnt_b, s_b, N[i].name, pos_b);
						pos_o -= 1;
					}
				}
				else{
					if (pos_b == N[i].num){
						pos_o = chang(cnt_o, s_o, N[i].name, pos_o);
						//s_b++;
						break;
					}
					else if (pos_b < N[i].num){
						pos_o = chang(cnt_o, s_o, N[i].name, pos_o);
						pos_b += 1;
					}
					else{
						pos_o = chang(cnt_o, s_o, N[i].name, pos_o);
						pos_b -= 1;
					}
				}
			}
			if (N[i].name == 'O')
				s_o += 1;
			else
				s_b += 1;
		}

		printf("Case #%d: %d\n", cas++, ans);

	}
	return  0;
}
