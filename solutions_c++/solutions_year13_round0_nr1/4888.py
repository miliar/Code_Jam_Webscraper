#include<cstdio>

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int testcase,test,i,j,ex,t;
	bool flag;
	char a[10][10];
	char b[10];
	scanf("%d",&testcase);
	getchar();
	for (test=1;test<=testcase;test++) {
		ex=0;
		for (i=1;i<=4;i++) {
			for (j=1;j<=4;j++) {
				scanf("%c",&a[i][j]);
				if (a[i][j]=='.') ex=1;
			}
			getchar();
		}
		gets(b);
		t=0;
		for (i=1;i<=4;i++) {
			flag=true;
			for (j=1;j<=4;j++)
				if (a[i][j]!='X' && a[i][j]!='T') flag=false;
			if (flag) t=1;
		}
		for (i=1;i<=4;i++) {
			flag=true;
			for (j=1;j<=4;j++)
				if (a[j][i]!='X' && a[j][i]!='T') flag=false;
			if (flag) t=1;
		}
		flag=true;
		for (i=1;i<=4;i++) 
			if (a[i][i]!='X' && a[i][i]!='T') flag=false;
		if (flag) t=1;
		flag=true;
		for (i=1;i<=4;i++)
			if (a[i][5-i]!='X' && a[i][5-i]!='T') flag=false;

		if (flag) t=1;
			for (i=1;i<=4;i++) {
			flag=true;
			for (j=1;j<=4;j++)
				if (a[i][j]!='O' && a[i][j]!='T') flag=false;
			if (flag) t=2;
		}
		for (i=1;i<=4;i++) {
			flag=true;
			for (j=1;j<=4;j++)
				if (a[j][i]!='O' && a[j][i]!='T') flag=false;
			if (flag) t=2;
		}
		flag=true;
		for (i=1;i<=4;i++) 
			if (a[i][i]!='O' && a[i][i]!='T') flag=false;
		if (flag) t=2;
		flag=true;
		for (i=1;i<=4;i++)
			if (a[i][5-i]!='O' && a[i][5-i]!='T') flag=false;
		if (flag) t=2;
		printf("Case #%d: ",test);
		if (t==1) printf("X won\n");
		if (t==2) printf("O won\n");
		if (t==0 && ex==0) printf("Draw\n");
		if (t==0 && ex==1) printf("Game has not completed\n");
	}
}
