#include <iostream>
#include <string.h>

using namespace std;

int mat[4][4];


int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	cin>>T;
	for(int ca=1;ca<=T;ca++){
		char str[6];
		memset(mat,0,sizeof(mat));
		int flag = 3;
		for(int i=0;i<4;i++){
			scanf("%s",str);
			for(int j=0;j<4;j++)
				if(str[j]=='X') mat[i][j]=1;
				else if(str[j]=='O') mat[i][j]=2;
				else if(str[j]=='T') mat[i][j]=3;
				else flag = 0;
		}
//		scanf("%s",str);
		{
			//row
			for(int i=0;i<4;i++){
				int j;
				for(j=0;j<4;j++)
					if((mat[i][j]&1)==0) break;
				if(j==4){
					flag = 1;
					break;
				}
			}
			if(flag == 1){
				printf("Case #%d: X won\n",ca);
				continue;
			}
			//col
			for(int j=0;j<4;j++){
				int i=0;
				for(i=0;i<4;i++)
					if((mat[i][j]&1)==0) break;
				if(i==4){
					flag = 1;
					break;
				}
			}
			if(flag==1){
				printf("Case #%d: X won\n",ca);
				continue;
			}
			//Dig
			int i;
			for(i=0;i<4;i++)
				if((mat[i][i]&1)==0) break;
			if(i==4){
				printf("Case #%d: X won\n",ca);
				continue;
			}
			int j;
			for(i=0,j=3;i<4;i++,j--)
				if((mat[i][j]&1)==0) break;
			if(i==4){
				printf("Case #%d: X won\n",ca);
				continue;
			}

			//row
			for(int i=0;i<4;i++){
				int j;
				for(j=0;j<4;j++)
					if((mat[i][j]&2)==0) break;
				if(j==4){
					flag = 2;
					break;
				}
			}
			if(flag == 2){
				printf("Case #%d: O won\n",ca);
				continue;
			}
			//col
			for(int j=0;j<4;j++){
				int i=0;
				for(i=0;i<4;i++)
					if((mat[i][j]&2)==0) break;
				if(i==4){
					flag = 2;
					break;
				}
			}
			if(flag==2){
				printf("Case #%d: O won\n",ca);
				continue;
			}
			//Dig
			for(i=0;i<4;i++)
				if((mat[i][i]&2)==0) break;
			if(i==4){
				printf("Case #%d: O won\n",ca);
				continue;
			}
			for(i=0,j=3;i<4;i++,j--)
				if((mat[i][j]&2)==0) break;
			if(i==4){
				printf("Case #%d: O won\n",ca);
				continue;
			}

			if(flag == 3) printf("Case #%d: Draw\n",ca);
			else printf("Case #%d: Game has not completed\n",ca);
		}
	}
}