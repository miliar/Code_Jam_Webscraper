#include<cstdio>

char B[5][5];
int T,cs;

bool isP1(char c) {
	return c == 'T' || c == 'X';
}
bool isP2(char c) {
	return c == 'T' || c == 'O';
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&T);
	for(cs=1;cs<=T;++cs) {
		for(int i=0;i<4;++i) scanf("%s",B[i]);
		bool p1, p2;
		for(int i=0;i<4;++i) {
			p1 = true, p2 = true;
			for(int j=0;j<4;++j)
				p1 &= isP1(B[i][j]), p2 &= isP2(B[i][j]);
			if(p1) {printf("Case #%d: X won\n",cs); goto end;}
			if(p2) {printf("Case #%d: O won\n",cs); goto end;}
		}
		for(int i=0;i<4;++i) {
			p1 = true, p2 = true;
			for(int j=0;j<4;++j)
				p1 &= isP1(B[j][i]), p2 &= isP2(B[j][i]);
			if(p1) {printf("Case #%d: X won\n",cs); goto end;}
			if(p2) {printf("Case #%d: O won\n",cs); goto end;}
		}
		p1 = p2 = true;
		for(int i=0;i<4;++i)
			p1 &= isP1(B[i][i]), p2 &= isP2(B[i][i]);
		if(p1) {printf("Case #%d: X won\n",cs); goto end;}
		if(p2) {printf("Case #%d: O won\n",cs); goto end;}
		p1 = p2 = true;
		for(int i=0;i<4;++i)
			p1 &= isP1(B[3-i][i]), p2 &= isP2(B[3-i][i]);
		if(p1) {printf("Case #%d: X won\n",cs); goto end;}
		if(p2) {printf("Case #%d: O won\n",cs); goto end;}

		bool full = true;
		for(int i=0;i<4;++i)for(int j=0;j<4;++j)
			if(B[i][j] == '.') full = false;
		if(full) printf("Case #%d: Draw\n",cs);
		else printf("Case #%d: Game has not completed\n",cs);
end:;
	}
}