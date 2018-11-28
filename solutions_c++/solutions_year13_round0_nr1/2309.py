#include <cstdio> //PROG: GCp1
#include <cstring>
#include <algorithm>
using std::sort;
int main(){
	#ifdef JACK1_NOTEBOOK
	freopen("GCp1_in.txt","r",stdin);
	freopen("GCp1_out.h","w",stdout);
	#endif
	int TN,Ti=0,i,j,k;
	char str[4][5],ans[100];
	scanf("%d",&TN);
	for (Ti=1;Ti<=TN;Ti++){
		for (i=0;i<4;i++)
			scanf("%s",str[i]);
		
		sprintf(ans,"Game has not completed");
		//check O
		for (i=0;i<4;i++){
			for (k=j=0;j<4;j++)
				if (str[i][j]=='O' || str[i][j]=='T')
					k++;
			if (k==4){sprintf(ans,"O won");goto OUTPUT;}
			for (k=j=0;j<4;j++)
				if (str[j][i]=='O' || str[j][i]=='T')
					k++;
			if (k==4){sprintf(ans,"O won");goto OUTPUT;}
		}
			for (k=j=0;j<4;j++)
				if (str[j][j]=='O' || str[j][j]=='T')
					k++;
			if (k==4){sprintf(ans,"O won");goto OUTPUT;}
			for (k=j=0;j<4;j++)
				if (str[j][3-j]=='O' || str[j][3-j]=='T')
					k++;
			if (k==4){sprintf(ans,"O won");goto OUTPUT;}
		
		//check X
		for (i=0;i<4;i++){
			for (k=j=0;j<4;j++)
				if (str[i][j]=='X' || str[i][j]=='T')
					k++;
			if (k==4){sprintf(ans,"X won");goto OUTPUT;}
			for (k=j=0;j<4;j++)
				if (str[j][i]=='X' || str[j][i]=='T')
					k++;
			if (k==4){sprintf(ans,"X won");goto OUTPUT;}
		}
			for (k=j=0;j<4;j++)
				if (str[j][j]=='X' || str[j][j]=='T')
					k++;
			if (k==4){sprintf(ans,"X won");goto OUTPUT;}
			for (k=j=0;j<4;j++)
				if (str[j][3-j]=='X' || str[j][3-j]=='T')
					k++;
			if (k==4){sprintf(ans,"X won");goto OUTPUT;}
		
		
		//check Draw
		k=0;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				if (str[i][j]=='.')
					k++;
		if (k==0)sprintf(ans,"Draw");
		
		OUTPUT:
		printf("Case #%d: %s\n",Ti,ans);
	}
}
