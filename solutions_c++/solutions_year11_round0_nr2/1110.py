#include<stdio.h>
#include<string.h>
char get(void){
	char ch;
	while(1){
		ch = getchar();
		if(ch >= 'A' && ch <= 'Z')
			return ch;
	}
}

int main(){
	int test, n;
	int ans, num;
	char map[26][26];
	int flag[26][26];
	char a, b, c;
	char stack[200];
	int top;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	scanf("%d", &test);
	for(int i=1; i<=test; i++){
		memset(map, 0, sizeof(map));
		memset(flag, 0, sizeof(flag));
		scanf("%d", &n);
		for(int j=0; j<n; j++){
			a = get();
			b = get();
			c = get();
			map[a-'A'][b-'A'] = c;
			map[b-'A'][a-'A'] = c;
		}

		scanf("%d", &n);
		for(int j=0; j<n; j++){
			a = get();
			b = get();
			flag[a-'A'][b-'A'] = 1;
			flag[b-'A'][a-'A'] = 1;
		}

		scanf("%d", &n);
		top = 0;
		for(int j=0; j<n; j++){
			a = get();
			while(top!=0 && map[a-'A'][stack[top-1]-'A']>1){
				a = map[a-'A'][stack[top-1]-'A'];
				top --;
			}
			stack[top++] = a;
			for(int k=0; k<top-1; k++){
				if(flag[a-'A'][stack[k]-'A'] == 1){
					top = 0;
					break;
				}
			}
		}
		printf("Case #%d: [", i);
		if(top != 0)
			printf("%c", stack[0]);
		for(int j=1; j<top; j++)
			printf(", %c", stack[j]);
		printf("]\n");
	}
	return 0;
}
