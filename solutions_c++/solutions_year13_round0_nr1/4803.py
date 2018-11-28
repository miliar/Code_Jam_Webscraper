#pragma warning(disable : 4996)

#include<stdio.h>

int t,n=0;
char data[4][4];

int what(char x){
	if(x=='T') return 2;
	else if(x=='X') return 0;
	else if(x=='O') return 1;
	return 3;
}

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);

	scanf("%d\n",&t);
	while(n++<t){
		bool flag = false;
		int cnt = 0, cnt1[4] = {0,}, cnt2[4] = {0,};
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%c",&data[i][j]);
				if(data[i][j]=='.') cnt++;
			}
			scanf("\n");
		}
		for(int i=0;i<4;i++){
			int cnt3[4] = {0,}, cnt4[4] = {0,};
			cnt1[what(data[i][i])]++;
			cnt2[what(data[i][3-i])]++;
			for(int j=0;j<4;j++){
				cnt3[what(data[i][j])]++;
				cnt4[what(data[j][i])]++;
			}
			if(cnt3[0] + cnt3[2] == 4 || cnt4[0] + cnt4[2] == 4){
				flag = true;
				printf("Case #%d: X won\n",n);
				break;
			}
			else if(cnt3[1] + cnt3[2] == 4 || cnt4[1] + cnt4[2] == 4){
				flag = true;
				printf("Case #%d: O won\n",n);
				break;
			}
		}
		if(flag==false){
			if(cnt1[0] + cnt1[2] == 4 || cnt2[0] + cnt2[2]==4){
				printf("Case #%d: X won\n",n);
				continue;
			}
			if(cnt1[1] + cnt1[2] == 4 || cnt2[1] + cnt2[2]==4){
				printf("Case #%d: O won\n",n);
				continue;
			}
		}
		else continue;
		if(cnt==0){
			printf("Case #%d: Draw\n",n);
			continue;
		}
		printf("Case #%d: Game has not completed\n",n);
	}
	return 0;
}