#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <iostream>
#include <stack>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#define FOR(x,b,e) for(long long x=b;x<e;x++)
#define FORD(x,b,e) for(int x=b-1;x>=e;x--)
typedef int LL;
void wczytaj(LL *z)
{
		register char c=0;
		while(c<33) c=getc_unlocked(stdin);
		(*z)=0;
		while(c>32) {(*z)=(*z) *10LL+(c-'0');c=getc_unlocked(stdin);}
}
using namespace std;
struct ulamek{
	LL licznik;
	LL mianownik;
};
	LL znaki[5][5];
	LL pre[5][5];
	LL pre2[5][5];
int main()
{
	LL t;

	LL foo=0;
	wczytaj(&t);
	FOR(i,1,t+1)
	{
		foo=0;
		FOR(x,1,5)
		{
			FOR(y,1,5)
			{
				znaki[x][y]=getchar();
				if(znaki[x][y]=='.')foo=1;
			}
			getchar();
		}
		getchar();		
		FOR(x,1,5)
		{
			FOR(y,1,5)
			{
				if(znaki[x][y]=='X') znaki[x][y]=1000;
				else if(znaki[x][y]=='O') znaki[x][y]=50;
				else if(znaki[x][y]== 'T') znaki[x][y]=5000;
				else if(znaki[x][y]=='.') znaki[x][y]=0;
			}
		}
		
		FOR(x,1,5)
		{
			FOR(y,1,5)
			{
				pre[x][y]=pre[x][y-1]+znaki[x][y];
			}
		}
		FOR(x,1,5)
		{
			FOR(y,1,5)
			{
				pre2[y][x]=pre2[y-1][x]+znaki[y][x];
			}
		}
		int p=0,d=0;
		FOR(x,1,5) 
		{
			if(pre2[4][x] == 4000 || pre2[4][x]==8000) p=1;
			if(pre[x][4]== 4000 || pre[x][4]==8000) p=1;
			
			if(pre2[4][x]==200  || pre2[4][x]==5150) d=1;
			if(pre[x][4]==200 || pre[x][4] == 5150) d=1;
		}
		if(znaki[1][1]+ znaki[2][2]+znaki[3][3]+znaki[4][4]== 4000 || znaki[1][1]+ znaki[2][2]+znaki[3][3]+znaki[4][4]==8000) p=1;
		if(znaki[1][1]+ znaki[2][2]+znaki[3][3]+znaki[4][4]==200 || znaki[1][1]+ znaki[2][2]+znaki[3][3]+znaki[4][4]==5150) d=1;
		if(znaki[1][4]+znaki[2][3]+znaki[3][2]+znaki[4][1] == 4000||znaki[1][4]+znaki[2][3]+znaki[3][2]+znaki[4][1] == 8000) p=1;
		if(znaki[1][4]+znaki[2][3]+znaki[3][2]+znaki[4][1] == 200 || znaki[1][4]+znaki[2][3]+znaki[3][2]+znaki[4][1] == 5150) d=1;
		if(d==0 && p==0 && foo ==1) printf("Case #%d: Game has not completed\n",i);
		else if(d==0 && p==0 && foo==0) printf("Case #%d: Draw\n",i);
		else if(d==1) printf("Case #%d: O won\n",i);
		else if(p==1) printf("Case #%d: X won\n",i);
	}
	
	
	
    return 0;
}
     
