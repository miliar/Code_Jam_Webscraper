#include <stdio.h>

int main(){
	bool turns[200];
	int orange[200];
	int blue[200];
	int numorange;
	int numblue;
	int posorange;
	int posblue;

	int missionorange;
	int missionblue;

	int cases;
	scanf("%d",&cases);
	for (int i = 1;i<=cases;i++){
		int m;
		numorange = 0;
		numblue = 0;
		scanf("%d",&m);
		missionorange = 0;
		missionblue = 0;
		for(int j = 0;j<m;j++){
			char tmpc;
			int tmpi;
			scanf(" %c %d",&tmpc,&tmpi);
			turns[j] = (tmpc == 'O');
			if(tmpc == 'O'){
				orange[numorange++] = tmpi-1;
			}else{
				blue[numblue++] = tmpi-1;
			}
		}
		posorange = 0;
		posblue = 0;
		int j = 0,count = 0;
		while(missionorange <numorange || missionblue < numblue){
			if(turns[j]){ // true = orange
				if(posblue != blue[missionblue]){
					if(posblue < blue[missionblue]){
						posblue++;
					}else{
						posblue--;
					}
				}
				if(posorange != orange[missionorange]){
					if(posorange < orange[missionorange]){
						posorange++;
					}else{
						posorange--;
					}
				}else{
					j++;
					missionorange++;
				}
			}else{
				if(posorange != orange[missionorange]){
					if(posorange < orange[missionorange]){
						posorange++;
					}else{
						posorange--;
					}
				}
				if(posblue != blue[missionblue]){
					if(posblue < blue[missionblue]){
						posblue++;
					}else{
						posblue--;
					}
				}else{
					j++;
					missionblue++;
				}

			}
			count++;
		}
		printf("Case #%d: %d\n",i,count);
	}
}
