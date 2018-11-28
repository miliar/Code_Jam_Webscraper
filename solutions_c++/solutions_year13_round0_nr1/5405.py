#include <cstdio>
#include <cstring>
using namespace std;
int t,cnt,state;
char a[4][4];
bool chk;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i=0; i<t; i++){
		cnt=0; state=0;
		memset (a,0,sizeof a);
		for (int j=0; j<4; j++){
			for (int k=0; k<4; k++){
				while (a[j][k]!='O'&&a[j][k]!='T'&&a[j][k]!='X'&&a[j][k]!='.') scanf("%c",&a[j][k]);
				if (a[j][k]=='.') cnt++;
			}
		}
		for (int j=0; j<4; j++){
			chk=true;
			for (int k=0; k<4; k++){
				if (a[j][k]!='O'&&a[j][k]!='T') chk=false;
			}
			if (chk) state=1;
			chk=true;
			for (int k=0; k<4; k++){
				if (a[k][j]!='O'&&a[k][j]!='T') chk=false;
			}
			if (chk) state=1;
			chk=true;
			for (int k=0; k<4; k++){
				if (a[j][k]!='X'&&a[j][k]!='T') chk=false;
			}
			if (chk) state=2;
			chk=true;
			for (int k=0; k<4; k++){
				if (a[k][j]!='X'&&a[k][j]!='T') chk=false;
			}
			if (chk) state=2;
			chk=true;
		}
		for (int j=0; j<4; j++){
			if (a[j][j]!='O'&&a[j][j]!='T') chk=false;
			
		}
		if (chk) state=1;
		chk=true;
		for (int j=0; j<4; j++){
			if (a[j][j]!='X'&&a[j][j]!='T') chk=false;
		}
		if (chk) state=1;
		chk=true;
		for (int j=0; j<4; j++){
			if (a[j][3-j]!='O'&&a[j][3-j]!='T') chk=false;
			
		}
		if (chk) state=1;
		chk=true;
		for (int j=0; j<4; j++){
			if (a[j][3-j]!='X'&&a[j][3-j]!='T') chk=false;
		}
		if (chk) state=2;
		chk=true;
		printf("Case #%d: ",i+1);
		if (state==1) printf("O won\n");
		if (state==2) printf("X won\n");
		if (state==0&&cnt==0) printf("Draw\n");
		if (state==0&&cnt!=0) printf("Game has not completed\n");
	}
}