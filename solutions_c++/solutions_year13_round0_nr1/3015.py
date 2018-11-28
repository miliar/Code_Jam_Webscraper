#include <iostream>
#include <cstdio>
#include <cmath>
#include <fstream>
using namespace std;

int T,cas = 0;
char a[5][5];

int pd(){
	int x = 0,o = 0;
	bool flag= 0;
	for (int i = 0;i < 4;i++){
		if (a[i][i] == 'X' || a[i][i] == 'T')
			x++;
		if (a[i][i] == 'O' || a[i][i] == 'T')
			o++;
	}
	if (x == 4) return 1;
	if (o == 4) return 0;
	x = o =0;
	for (int i = 0;i < 4;i++){
		if (a[i][3-i] == 'X' || a[i][3-i] == 'T')
			x++;
		if (a[i][3-i] == 'O' || a[i][3-i] == 'T')
			o++;
	}
	if (x == 4) return 1;
	if (o == 4) return 0;
	
	for (int i = 0;i < 4;i++){
		x = o = 0;
		for (int j = 0;j < 4;j++){
			if (a[i][j] == 'X' || a[i][j] == 'T')
				x++;
			if (a[i][j] == 'O' || a[i][j] == 'T')
				o++;
			if (a[i][j] == '.') flag = 1;
		}
		if (x == 4) return 1;
		if (o == 4) return 0;
		x = o = 0;
		for (int j = 0;j < 4;j++){
			if (a[j][i] == 'X' || a[j][i] == 'T')
				x++;
			if (a[j][i] == 'O' || a[j][i] == 'T')
				o++;
		}
		if (x == 4) return 1;
		if (o == 4) return 0;
	}
	if(flag) return 3;
	else return 2;
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		for (int i = 0;i < 4;i++)
			scanf("%s",a[i]);
		int tem = pd();
		cas++;
		switch(tem){
		case 0:printf("Case #%d: O won\n",cas);break;
		case 1:printf("Case #%d: X won\n",cas);break;
		case 2:printf("Case #%d: Draw\n",cas);break;
		case 3:printf("Case #%d: Game has not completed\n",cas);break;
		}

	}
}