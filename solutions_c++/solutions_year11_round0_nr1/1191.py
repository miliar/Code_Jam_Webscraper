#include<iostream>
using namespace std;
struct node {
	char c;
	int num;
	int fin;
};
struct node nodes[103];
int bb[101],oo[101],bn,on;
int solve(int n){
	int ans = 0;
	int bs=1,os=1,bg=1,og=1;
	while(1){
		ans++;
		//for Orange
		//Move
		bool flag = false;
		if (og != on){
			if (os < nodes[oo[og]].num){
				os++;
			}
			else if (os > nodes[oo[og]].num){
				os--;
			}
			else if (os == nodes[oo[og]].num){
				//push
				if(nodes[oo[og]-1].fin == 1){
					nodes[oo[og]].fin = 1;
					og++;
					flag = true;
				}
			}
		}
		//For Blue
		//Move
		if (bg !=bn){
			if (bs < nodes[bb[bg]].num){
				bs++;
			}
			else if (bs > nodes[bb[bg]].num){
				bs--;
			}
			else if (bs == nodes[bb[bg]].num){
				//push
				if(nodes[bb[bg]-1].fin == 1 && flag == false){
					nodes[bb[bg]].fin = 1;
					bg++;
				}
			}
		}
		if (bg == bn && og == on){
			break;
		}
	}
	return ans;
}
int main(){
	int cases, i, n, num, k;
	char c;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while(scanf("%d",&cases)!=EOF){
		n = 0;
		nodes[0].fin = 1;
		for(k=1; k<=cases; k++){
			scanf("%d",&n);
			getchar();
			bn = 1;
			on = 1;
			for(i=1; i<=n; i++){
				scanf("%c%d",&c,&num);
				getchar();
				nodes[i].c = c;
				nodes[i].num = num;
				nodes[i].fin = 0;
				if (c == 'B'){
					bb[bn] = i;
					bn++;
				}
				if (c == 'O'){
					oo[on] = i;
					on++;
				}
			}
			printf("Case #%d: %d\n", k,solve(n));
		}
	}
	return 0;
}