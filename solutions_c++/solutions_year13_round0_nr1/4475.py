#include <cstdio>

using namespace std;

bool check(char **, char);
bool check(char b[][5], char p)
{
	int i,j,cnt1,cnt2;
	for(i=0;i<4;i++){
		cnt1=0,cnt2=0;
		for(j=0;j<4;j++){
			if(b[i][j] == p || b[i][j] == 'T'){
				cnt1++;
			}
			if(b[j][i] == p || b[j][i] == 'T'){
				cnt2++;
			}
		}
		if(cnt1==4 || cnt2==4){
			return true;
		}
	}
	cnt1=0,cnt2=0;
	for(i=0;i<4;i++){
		if(b[i][i]==p||b[i][i]=='T'){
			cnt1++;
		}
		if(b[3-i][i]==p||b[3-i][i]=='T'){
			cnt2++;
		}
		
	}
	if(cnt1==4 || cnt2==4){
		return true;
	}
	return false;
}


int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	/*FILE *fp = fopen("output.txt","w");*/
	int T,t;
	scanf("%d",&T);
	t=T;
	while(T--){
		int i,j,cell=0;
		char b[5][5]={0};
		for(i=0;i<4;i++){
			scanf("%s",b[i]);
			for(j=0;j<4;j++){
				if(b[i][j] == 'X' || b[i][j] == 'O' || b[i][j] == 'T') {
					cell++;
				}
			}
		}
		if(check(b,'X')){
			printf("Case #%d: X won\n",t-T);
		//	fprintf(fp, "Case #%d: X won\n",t-T);
		}
		else if (check(b,'O')){
			printf("Case #%d: O won\n",t-T);
			//fprintf(fp, "Case #%d: O won\n",t-T);
		}
		else {
			if(cell==16){
				printf("Case #%d: Draw\n",t-T);
				//fprintf(fp,"Case #%d: Draw\n",t-T);
			}
			else{
				printf("Case #%d: Game has not completed\n",t-T);
				//fprintf(fp,"Case #%d: Game has not completed\n",t-T);
			}
		}
	}
	fclose(fp);
	return 0;
}