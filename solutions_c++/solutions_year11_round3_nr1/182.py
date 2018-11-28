#include <stdio.h>

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		int r,c;
		char pic[100][100];
		bool possible=true;
		scanf("%d %d\n",&r,&c);
		for (int i=0;i<r;i++){
			for (int j=0;j<c;j++) scanf("%c",&pic[i][j]);
			scanf("\n");
		}
		for (int i=0;i<r-1;i++)
			for (int j=0;j<c-1;j++)
				if (pic[i][j]=='#')
					if ((pic[i+1][j]=='#')&&(pic[i][j+1]=='#')&&(pic[i+1][j+1]=='#')){
						pic[i][j]='/';
						pic[i+1][j]='\\';
						pic[i][j+1]='\\';
						pic[i+1][j+1]='/';
					}
		for (int i=0;i<r;i++) for (int j=0;j<c;j++) if(pic[i][j]=='#') possible=false;
		printf("Case #%d:\n",tc);
		if (possible==true)
			for (int i=0;i<r;i++){
				for (int j=0;j<c;j++) printf("%c",pic[i][j]);
				printf("\n");
			}
		else printf("Impossible\n");
	}
	fclose(stdin);
	fclose(stdout);
}