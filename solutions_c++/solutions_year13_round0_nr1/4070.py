									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

char s[11][11];

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("temp.out","w",stdout);	
	int ti,tc,i,j,t,x,o,e=0,ow=0,xw=0;
	char c;
	scanf("%d",&tc);
	rep(ti,tc){
		xw=ow=e=0;
		rep(i,4){ //row
			scanf("%s",s[i]);
			t=o=x=0;
			rep(j,4){
				c=s[i][j];
				e|=c=='.';
				t+=c=='T';
				o+=c=='O';
				x+=c=='X';
			}
			if (o==4 || (t && o==3))
				ow=1;
			if (x==4 || (t && x==3))
				xw=1;
		}
		rep(j,4){ // column
			t=o=x=0;
			rep(i,4){
				c=s[i][j];
				e|=c=='.';
				t+=c=='T';
				o+=c=='O';
				x+=c=='X';
			}
			if (o==4 || (t && o==3))
				ow=1;
			if (x==4 || (t && x==3))
				xw=1;
		}
		// diag1
		t=o=x=0; 
		rep(i,4){
			c=s[i][i];
			e|=c=='.';
			t+=c=='T';
			o+=c=='O';
			x+=c=='X';
		}
		if (o==4 || (t && o==3))
			ow=1;
		if (x==4 || (t && x==3))
			xw=1;
		// diag2
		t=o=x=0;
		rep(j,4){
			i=3-j;
			c=s[i][j];
			e|=c=='.';
			t+=c=='T';
			o+=c=='O';
			x+=c=='X';
		}
		if (o==4 || (t && o==3))
			ow=1;
		if (x==4 || (t && x==3))
			xw=1;
		
		// check
		printf("Case #%d: ",ti+1);
		if (ow && !xw)
			printf("O won");
		else if (!ow && xw)
			printf("X won");
		else if (ow && xw)
			printf("Draw");
		else{
			if (e)
				printf("Game has not completed");
			else
				printf("Draw");
		}
		printf("\n");
	}
	
	return 0;
}