#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char num[30];

int main(){
	int TTT,testnum;
	int len;
	scanf("%d",&TTT);
	for(testnum=1;testnum<=TTT;testnum++){
		memset(num,0,sizeof(num));
		scanf("%s",num);
		len = strlen(num);
		int i,j;
		int flg = 0;
		for(i=0;num[i+1];i++){
			if(num[i] < num[i+1]){
				flg = 1;
				break;
			}
		}
		if(flg){
			/* °°Àº ÀÚ¸´¼ö */
			for(i=0;num[i];i++){
				flg = 0;
				for(j=i+1;num[j+1];j++){
					if(num[j] < num[j+1]){
						flg = 1;
						break;
					}
				}
				if(flg == 0){
					int minm=5500,vmin=-1;
					for(j=i+1;num[j];j++){
						if(num[j] > num[i]){
							if(minm > num[j]){
								minm = num[j];
								vmin = j;
							}
						}
					}
					int tmp = num[i];
					num[i] = num[vmin];
					num[vmin] = tmp;
					sort(num+i+1,num+len);
					break;
				}
			}
		}else{
			/* n+1 */
			num[len] = '0';
			len ++;
			sort(num,num+len);
			for(i=0;num[i];i++){
				if(num[i] != '0'){
					int tmp;
					tmp = num[i];
					num[i] = num[0];
					num[0] = tmp;
					break;
				}
			}
		}
		printf("Case #%d: %s\n",testnum,num);
	}
	return 0;
}
