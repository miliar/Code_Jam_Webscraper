

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

int main() {



	freopen("D:/GCJ2013/A-small-attempt0.in","r", stdin);
	freopen("D:/GCJ2013/A-small-attempt0.out", "w", stdout);
	int t;
	int NUM=4;
	char label[4][4];
	char tmp;
	while(scanf("%d",&t)!=EOF&&t!=0){
		for(int num=0;num<t;num++){
			scanf("%c",&tmp);
			for(int i=0;i<NUM;i++){
				for(int j=0;j<NUM;j++)
					scanf("%c",&label[i][j]);
				scanf("%c",&tmp);
			}
			bool finish = true;
			char win = 'n';
			for(int i=0;i<NUM;i++){
				for(int j=1;j<NUM;j++){
					if(label[i][j] == '.'){finish = false;break;}
					if(label[i][j] != label[i][j - 1] && label[i][j] != 'T'){break;}
					//if(j == (NUM - 1))win = (label[i][j] == 'T' ? label[i][j - 1] : label[i][j]);
					if(j == NUM - 1){
						while(label[i][j] == 'T' || label[i][j] == '.')
							j--;
						win = label[i][j];
						break;
					}
				}
				if(win != 'n'){
					break;
				}
			}
			if(win != 'n'){
				printf("Case #%d: %c won\n", num + 1, win);
				continue;
			}
			for(int j=0;j<NUM;j++){
				for(int i=1;i<NUM;i++){
					if(label[i][j] == '.'){finish = false;break;}
					if(label[i][j] != label[i - 1][j] && label[i][j] != 'T'){break;}
					//if(j == (NUM - 1))win = (label[i][j] == 'T' ? label[i][j - 1] : label[i][j]);
					if(i == NUM - 1){
						while(label[i][j] == 'T' || label[i][j] == '.')
							i--;
						win = label[i][j];
						break;
					}
				}
				if(win != 'n'){
					break;
				}
			}
			if(win != 'n'){
				printf("Case #%d: %c won\n", num + 1, win);
				continue;
			}
			for(int i = 1; i < NUM; i++){
				if(label[i][i] == '.')break;
				if(label[i][i] != label[i - 1][i - 1] && label[i][i] != 'T')break;
				if(i == NUM - 1){
					while(label[i][i] == 'T' || label[i][i] == '.')
						i--;
					win = label[i][i];
					break;
				}
			}
			if(win != 'n'){
				printf("Case #%d: %c won\n", num + 1, win);
				continue;
			}
			for(int i = 1; i < NUM; i++){
				if(label[i][NUM - 1 - i] == '.')break;
				if(label[i][NUM - 1 - i] != label[i - 1][NUM - i] && label[i][NUM - 1 - i] != 'T')break;
				if(i == NUM - 1){
					while(label[i][i] == 'T' || label[i][i] == '.')
						i--;
					win = label[i][NUM - 1 - i];
					break;
				}
			}
			if(win != 'n'){
				printf("Case #%d: %c won\n", num + 1, win);
				continue;
			}
			if(finish){
				printf("Case #%d: Draw\n", num + 1);
				continue;
			}
			printf("Case #%d: Game has not completed\n", num + 1);
			//for(int i=0;i<NUM;i++){
			//	for(int j=0;j<NUM;j++)
			//		printf("%c",label[i][j]);
			//	printf("\n");
			//}
		}
	}

    return 0;
}






