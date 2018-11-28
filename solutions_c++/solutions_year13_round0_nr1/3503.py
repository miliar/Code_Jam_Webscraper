#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

char Map[6][6];
bool draw,winner;

void Read() {
	for (int i=1;i<=4;i++) {
		for (int j=1;j<=4;j++) {
			char c;
			cin>>c;
			Map[i][j]=c;
			if (c=='.')
				draw=false;
		}
	}
}

inline bool check_horizontaly(int i,int j,char c) {
	int p1=j-1;
	bool match=true;
	
	while (p1>=1) {
		if (Map[i][p1]!=c&&Map[i][p1]!='T')
			match=false;
		p1--;
	}
	
	p1=j+1;
	
	while (p1<=4) {
		if (Map[i][p1]!=c&&Map[i][p1]!='T') {
			match=false;
		}
		p1++;
	}
	
	return match;
}

inline bool check_verticaly(int i,int j,char c) {
	int p1=i-1;
	bool match=true;
	
	while (p1>=1) {
		if (Map[p1][j]!=c&&Map[p1][j]!='T')
			match=false;
		p1--;
	}
	
	p1=i+1;
	
	while (p1<=4) {
		if (Map[p1][j]!=c&&Map[p1][j]!='T')
			match=false;
		p1++;
	}
	
	return match;
}

inline bool diagon(int i,int j,char c) {
	bool match=true;
	
	if (i==1&&j==1) {
		for (int i=1;i<=4;i++) {
			if (Map[i][i]!=c&&Map[i][i]!='T')
				match=false;
		}
	}
	if (i==1&&j==4) {
		for (int i=1;i<=4;i++) {
			if (Map[i][5-i]!=c&&Map[i][5-i]!='T')
				match=false;
		}
	}
	if (i==4&&j==1) {
		for (int i=1;i<=4;i++) {
			if (Map[i][5-i]!=c&&Map[i][5-i]!='T')
				match=false;
		}
	}
	if (i==4&&j==4) {
		for (int i=1;i<=4;i++) {
			if (Map[i][i]!=c&&Map[i][i]!='T')
				match=false;
		}
	}
	
	return match;
}

void Solve(int kase) {
	int who=-1;
	bool winner=false;
	
	for (int i=1;i<=4&&!winner;i++) {
		for (int j=1;j<=4;j++) {
			if (Map[i][j]=='X'||Map[i][j]=='O') {
				if (check_horizontaly(i,j,Map[i][j])) {
					winner=true;
					if (Map[i][j]=='X') {
						who=0;
					}
					else
						who=1;
					break;
				}
				if (check_verticaly(i,j,Map[i][j])) {
					winner=true;
					if (Map[i][j]=='X') {
						who=0;
					}
					else
						who=1;
					break;
				}
			
				if ((i==1&&j==1)||(i==1&&j==4)||(i==4&&j==1)||(i==4&&j==4)) {
					if (diagon(i,j,Map[i][j])) {
						winner=true;
						if (Map[i][j]=='X') {
							who=0;
						}
						else {
							who=1;
						}
						break;
					}
				}
			}
		}
	}
	
	if (winner) {
		if (!who) {
			printf("Case #%d: X won\n",kase);
		}
		else {
			printf("Case #%d: O won\n",kase);
		}
	}
	else {
		if (draw) {
			printf("Case #%d: Draw\n",kase);
		}
		else {
			printf("Case #%d: Game has not completed\n",kase);
		}
	}
}

void Init() {
	
	for (int i=0;i<=5;i++) {
		for (int j=0;j<=5;j++) {
			Map[i][j]=0;
		}
	}
}

int main () {
	
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	
	for (int i=1;i<=t;i++) {
		draw=true;
		Read();
		Solve(i);
		Init();
	}
	
	return 0;
}
