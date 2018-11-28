// dtb @ gcj'13
#include <cstdio>
#include <cstdlib>

int main () {
		
		freopen("A-small.in","r",stdin);
		freopen("A-small","w",stdout);

		int T,win,sum,emptyFound,caseNum=0;
		char b[4][5];
		
		for (scanf ("%d",&T);T;T--) {
				// input
				for (int i=0;i<4;i++) 
						scanf ("%s",b[i]);
				// process
				emptyFound=0;
				win=0;
				
				for (int i=0;i<4;i++) {
						for (int j=0;j<4;j++) {
								if (b[i][j]=='X')
										b[i][j]=1;
								else if (b[i][j]=='O')
										b[i][j]=-1;
								else if (b[i][j]=='T')
										b[i][j]=0;
								else emptyFound=1;
						}
				}

				for (int i=0;i<4;i++){
						sum=0;
						for (int j=0;j<4;j++){
								if (b[i][j]!='.')
								sum+=b[i][j];
						}
						if (sum >= 3) {
								win=1;
								break;
						}
						else if (sum <= -3) {
								win=2;
								break;
						}
				}
				
				if (!win) {
				for (int j=0;j<4;j++){
						sum=0;
						for (int i=0;i<4;i++){
								if (b[i][j]!='.')
								sum+=b[i][j];
						}
						if (sum >= 3) {
								win=1;
								break;
						}
						else if (sum <= -3) {
								win=2;
								break;
						}
				}
				}
				
		if (!win) {
				sum=0;
				for (int j=0;j<4;j++){
							if (b[j][j]!='.')
								sum+=b[j][j];
						}
						if (sum >= 3) {
								win=1;
						}
						else if (sum <= -3) {
								win=2;
						}
				}
		
		if (!win) {
				sum=0;
				for (int j=0;j<4;j++){
							if (b[3-j][j]!='.')
								sum+=b[3-j][j];
						}
						if (sum >= 3) {
								win=1;
						}
						else if (sum <= -3) {
								win=2;
						}
		}

		// output
				printf ("Case #%d: ",++caseNum);

				if (win==1)
						printf ("X won\n");
				else if (win==2)
						printf ("O won\n");
				else if (!win && !emptyFound )
						printf ("Draw\n");
				else printf ("Game has not completed\n");
		}
}

