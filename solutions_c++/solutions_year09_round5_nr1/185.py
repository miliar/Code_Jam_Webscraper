#include<string.h>
#include<iostream>
#include<stdio.h>
#include<string>
#include<queue>
using namespace std;
struct node{
	int x,y;
	int d;
}tem,head,tar;

char s[20][20];
bool mark[20][20][3];
int st[20][20][3];
int t[20][4][2]={
	1,0,1,1,-1,0,-1,1,
	1,0,1,1,-1,0,-1,1,
	1,1,-1,1,-1,0,-1,2,
	-1,0,1,0,-1,-1,-1,1,
	-1,1,1,0,1,1,1,2,
	-1,0,1,-1,1,0,1,1,
	
	0,1,0,-1,1,1,1,-1,
	0,1,0,-1,1,1,1,-1,
	0,1,1,1,2,1,1,-1,
	1,1,1,-1,0,-1,2,-1,
	0,-1,1,-1,0,1,2,-1,
	0,-1,0,1,-1,1,1,1,
	
	-1,0,1,-1,1,1,1,1,
	-1,0,1,-1,1,1,1,1,
	2,0,0,1,0,-1,0,-1,
	2,0,0,1,0,-1,0,-1,
	
	1,1,-1,1,0,-1,0,-1,
	1,1,-1,1,0,-1,0,-1,
	-1,0,1,0,0,2,0,2,
	-1,0,1,0,0,2,0,2	
};
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn,tx,ty,td;
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		int n,m;
		scanf("%d%d",&n,&m);
		memset(s,'#',sizeof(s));
		memset(st,0,sizeof(st));
		queue<node>q;
		memset(mark,0,sizeof(mark));
		n++;m++;
		for (int i=2;i<=n;i++) {
			scanf("%s",s[i]+2);
		}
		int cnt=0;
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) {
			if (s[i][j]=='o'||s[i][j]=='w') cnt++;
			if ((s[i][j]=='o'||s[i][j]=='w')
			&&(s[i][j+1]=='o'||s[i][j+1]=='w')) {
				tem.x=i;tem.y=j;
				tem.d=1;
			}
			if ((s[i][j]=='o'||s[i][j]=='w')
			&&(s[i+1][j]=='o'||s[i+1][j]=='w')) {
				tem.x=i;tem.y=j;
				tem.d=2;
			}
			if ((s[i][j]=='x'||s[i][j]=='w')
			&&(s[i][j+1]=='x'||s[i][j+1]=='w')) {
				tar.x=i;tar.y=j;
				tar.d=1;
			}
			if ((s[i][j]=='x'||s[i][j]=='w')
			&&(s[i+1][j]=='x'||s[i+1][j]=='w')) {
				tar.x=i;tar.y=j;
				tar.d=2;
			}
		}
		if (cnt==1) {
			int dx[]={0,0,1,-1};
			int dy[]={1,-1,0,0};
			for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) {
				if (s[i][j]=='o'||s[i][j]=='w') {tem.x=i;tem.y=j;tem.d=0;}
				if (s[i][j]=='x'||s[i][j]=='w') {tar.x=i;tar.y=j;tar.d=0;}
			}
			q.push(tem);
			if (s[tem.x][tem.y]=='w') {
				printf("Case #%d: 0\n",ii);
				continue;
			}
			int ans=-1;
			while (!q.empty()) {
				head=q.front();
				q.pop();
				
				if (s[head.x+dx[0]][head.y+dy[0]]!='#'&&s[head.x+dx[1]][head.y+dy[1]]!='#') {
					for (int i=0;i<2;i++) {
						tem.x=head.x+dx[i];tem.y=head.y+dy[i];
						if (!mark[tem.x][tem.y][0]) {
							mark[tem.x][tem.y][0]=1;
							q.push(tem);
							st[tem.x][tem.y][0]=st[head.x][head.y][0]+1;
							if (tem.x==tar.x&&tem.y==tar.y) {
								ans=st[tem.x][tem.y][0];
							}
						}
					}
				}
				if (s[head.x+dx[2]][head.y+dy[2]]!='#'&&s[head.x+dx[3]][head.y+dy[3]]!='#') {
					for (int i=2;i<4;i++) {
						tem.x=head.x+dx[i];tem.y=head.y+dy[i];
						if (!mark[tem.x][tem.y][0]) {
							mark[tem.x][tem.y][0]=1;
							q.push(tem);
							st[tem.x][tem.y][0]=st[head.x][head.y][0]+1;
							if (tem.x==tar.x&&tem.y==tar.y) {
								ans=st[tem.x][tem.y][0];
							}
						}
					}
				}
				
			}
			printf("Case #%d: %d\n",ii,ans);
			continue;
		}
		int ans=-1;
		q.push(tem);
		if (tar.x==tem.x&&tar.y==tem.y&&tar.d==tem.d) {
			printf("Case #%d: 0\n",ii);
			continue;
		}
		mark[tem.x][tem.y][tem.d]=1;
		while (!q.empty()) {
			head=q.front();
			q.pop();
			int i=0;
			if (head.d==2) i=6;
			for (;i<20;i++) {
				bool suc=1;
				for (int j=0;j<4;j++) 
					if (s[head.x+t[i][j][0]][head.y+t[i][j][1]]=='#') {suc=0;break;}
				if (!suc) continue;
				
				if (head.d==1&&i>=6&&i<=15) continue;
				if (head.d==2&&(!(i>=6&&i<=15))) continue;
				
				if (i==0) {tem.x=head.x-1;tem.y=head.y;tem.d=head.d;}
				else if (i==1) {tem.x=head.x+1;tem.y=head.y;tem.d=head.d;}
				else if (i==2) {tem.x=head.x-1;tem.y=head.y;tem.d=2;}
				else if (i==3) {tem.x=head.x-1;tem.y=head.y+1;tem.d=2;}
				else if (i==4) {tem.x=head.x;tem.y=head.y;tem.d=2;}
				else if (i==5) {tem.x=head.x;tem.y=head.y+1;tem.d=2;}
				else if (i==6) {tem.x=head.x;tem.y=head.y+1;tem.d=head.d;}
				else if (i==7) {tem.x=head.x;tem.y=head.y-1;tem.d=head.d;}
				else if (i==8) {tem.x=head.x;tem.y=head.y;tem.d=1;}
				else if (i==9) {tem.x=head.x;tem.y=head.y-1;tem.d=1;}
				else if (i==10) {tem.x=head.x+1;tem.y=head.y-1;tem.d=1;}
				else if (i==11) {tem.x=head.x+1;tem.y=head.y;tem.d=1;}
				else if (i==12) {tem.x=head.x+1;tem.y=head.y-1;tem.d=1;}
				else if (i==13) {tem.x=head.x+1;tem.y=head.y;tem.d=1;}
				else if (i==14) {tem.x=head.x;tem.y=head.y;tem.d=1;}
				else if (i==15) {tem.x=head.x;tem.y=head.y-1;tem.d=1;}
				else if (i==16) {tem.x=head.x;tem.y=head.y+1;tem.d=2;}
				else if (i==17) {tem.x=head.x-1;tem.y=head.y+1;tem.d=2;}
				else if (i==18) {tem.x=head.x-1;tem.y=head.y;tem.d=2;}
				else if (i==19) {tem.x=head.x;tem.y=head.y;tem.d=2;}
				
				//if (head.d==tem.d&&i!=0&&i!=1&&i!=6&&i!=7) continue;
				
				if (!mark[tem.x][tem.y][tem.d]) {
					q.push(tem);
					mark[tem.x][tem.y][tem.d]=1;
					st[tem.x][tem.y][tem.d]=st[head.x][head.y][head.d]+1;
					if (tem.x==tar.x&&tem.y==tar.y&&tem.d==tar.d) {
						ans=st[tem.x][tem.y][tem.d];break;}
				}
			}
			if (ans!=-1) break;
		}
		printf("Case #%d: ",ii);

		if (ans==-1) puts("-1");
		else printf("%d\n",ans*2);
	}
}
