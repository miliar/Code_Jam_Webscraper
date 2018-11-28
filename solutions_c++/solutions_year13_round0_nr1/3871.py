#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int T=0;
	int i,r,c;
	char ch;
	int con;
	int row[1010][2],col[1010][2],di[2][2];
	freopen("A-large.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;i++) {
		con=0;
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		memset(di,0,sizeof(di));
		for(r=1;r<=4;r++) {
			for (c=1;c<=4;c++) {
				cin>>ch;
				if (ch=='X') {
					row[r][0]++;
					col[c][0]++;
					if (r==c) {
						di[0][0]++;
					}
					else if ((r+c)==5) {
						di[1][0]++;
					}
				}
				else if (ch=='O') {
					row[r][1]++;
					col[c][1]++;
					if (r==c) {
						di[0][1]++;
					}
					else if ((r+c)==5) {
						di[1][1]++;
					}
				}
				else if (ch=='T') {
					row[r][0]++;
					col[c][0]++;
					row[r][1]++;
					col[c][1]++;
					if (r==c) {
						di[0][0]++;
						di[0][1]++;
					}
					else if ((r+c)==5) {
						di[1][0]++;
						di[1][1]++;
					}
				}
				else if (ch=='.') {
					con++;
				}
			}
		}
		if (di[1][0]==4 || di[0][0]==4) {printf("Case #%d: X won\n",i);}
		else if (di[1][1]==4 || di[0][1]==4) {printf("Case #%d: O won\n",i);}
		else if (row[1][0]==4 || row[2][0]==4 || row[3][0]==4 || row[4][0]==4 || col[1][0]==4 || col[2][0]==4|| col[3][0]==4 || col[4][0]==4)
			printf("Case #%d: X won\n",i);
		else if (row[1][1]==4 || row[2][1]==4 || row[3][1]==4 || row[4][1]==4 || col[1][1]==4 || col[2][1]==4|| col[3][1]==4 || col[4][1]==4)
			printf("Case #%d: O won\n",i);
		else if (con==0) {
			printf("Case #%d: Draw\n",i);
		}
		else if (con>0) printf("Case #%d: Game has not completed\n",i);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

