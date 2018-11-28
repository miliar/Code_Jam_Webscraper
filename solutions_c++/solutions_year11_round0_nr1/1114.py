#include<stdio.h>
int fabs(int a){
	return a>0 ? a : -a;
}

char get(void){
	char ch;
	while(1){
		ch = getchar();
		if(ch == 'O' || ch == 'B')
			return ch;
	}
}

int main(){
	int test, n;
	int ta, tb;
	int pa, pb;
	char c;
	int p;
	int ans;
	int move;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	scanf("%d", &test);

	for(int i=1; i<=test; i++){
		scanf("%d", &n);
		pa = pb = 1;
		ta = tb = 0;
		ans = 0;
		for(int j=0; j<n; j++){
			c = get();
			scanf("%d", &p);
			if(c == 'O'){
				move = fabs(p - pa);

				if(move > ta){
					tb += move - ta;
					ans += move - ta;
					ta = 0;
				}
				else{
					ta = tb = 0;
				}
				tb ++;
				ans ++;
				pa = p;
			}
			else{
				move = fabs(p - pb);
				if(move > tb){
					ta += move - tb;
					ans += move - tb;
					tb = 0;
				}
				else{
					ta = tb = 0;
				}
				ta ++;
				ans ++;
				pb = p;
			}
		}
		printf("Case #%d: %d\n",i, ans);
	}
	return 0;
}
