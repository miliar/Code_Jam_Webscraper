#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define ALL(A) A.begin(),A.end()
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

char brd[4][4];

int calWinner()
{
	bool X,O,E=0;
	FOR(rw,0,4){
		X=1,O=1;
		FOR(cl,0,4){
			X&=(brd[rw][cl]=='X' || brd[rw][cl]=='T');
			O&=(brd[rw][cl]=='O' || brd[rw][cl]=='T');
			E|=(brd[rw][cl]=='.');
		}
		if(X==1)	return 1;
		if(O==1)	return -1;
	}

	FOR(cl,0,4){
		X=1,O=1;
		FOR(rw,0,4){
			X&=(brd[rw][cl]=='X' || brd[rw][cl]=='T');
			O&=(brd[rw][cl]=='O' || brd[rw][cl]=='T');
			E|=(brd[rw][cl]=='.');
		}
		if(X==1)	return 1;
		if(O==1)	return -1;
	}

	X=1,O=1;
	FOR(dg,0,4){
		X&=(brd[dg][dg]=='X' || brd[dg][dg]=='T');
		O&=(brd[dg][dg]=='O' || brd[dg][dg]=='T');
		E|=(brd[dg][dg]=='.');
	}
	if(X==1)	return 1;
	if(O==1)	return -1;

	X=1,O=1;
	FOR(dg,0,4){
		X&=(brd[dg][3-dg]=='X' || brd[dg][3-dg]=='T');
		O&=(brd[dg][3-dg]=='O' || brd[dg][3-dg]=='T');
		E|=(brd[dg][3-dg]=='.');
	}
	if(X==1)	return 1;
	if(O==1)	return -1;

	return (E==1)?0:999;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d",&T);

	EFOR(cs,1,T){
		FOR(rw,0,4)
			scanf("%s",&brd[rw]);

		printf("Case #%d: ",cs);

		int res=calWinner();
		if(res==999)
			printf("Draw\n");
		else if(res==0)
			printf("Game has not completed\n");
		else
			printf("%c won\n",(res==1)?'X':'O');
	}

	return 0;
}
