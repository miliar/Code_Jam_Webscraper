#include<cstdio>
#include<cstring>

const int MAX=100010;
char P[]="OX";
int b[5][5];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t,tc,i,j,k;
    bool owin,xwin;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++){
		getchar();
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				b[i][j]=getchar();
			}
			getchar();
		}
		owin=xwin=0;
		for(i=1;i<=4;i++){
			for(k=0;k<2;k++){
				for(j=1;j<=4;j++){
					if(b[i][j]!=P[k]&&b[i][j]!='T'){
						break;
					}
				}
				if(j==5){
					if(k==0)owin=1;
					else xwin=1;
					goto ending;
				}
			}
		}
		for(i=1;i<=4;i++){
			for(k=0;k<2;k++){
				for(j=1;j<=4;j++){
					if(b[j][i]!=P[k]&&b[j][i]!='T'){
						break;
					}
				}
				if(j==5){
					if(k==0)owin=1;
					else xwin=1;
					goto ending;
				}
			}
		}
			for(k=0;k<2;k++){
				for(j=1;j<=4;j++){
					if(b[j][j]!=P[k]&&b[j][j]!='T'){
						break;
					}
				}
				if(j==5){
					if(k==0)owin=1;
					else xwin=1;
					goto ending;
				}
			}
			for(k=0;k<2;k++){
				for(j=1;j<=4;j++){
					if(b[5-j][j]!=P[k]&&b[5-j][j]!='T'){
						break;
					}
				}
				if(j==5){
					if(k==0)owin=1;
					else xwin=1;
					goto ending;
				}
			}
		ending:
			printf("Case #%d: ",tc);
			if(owin)printf("O won\n");
			else if(xwin)printf("X won\n");
			else{
				for(i=1;i<=4;i++){
					for(j=1;j<=4;j++){
						if(b[i][j]=='.')break;
					}
					if(j<=4)break;
				}
				if(i==5)printf("Draw\n");
				else printf("Game has not completed\n");
			}
	}
    return 0;
}
