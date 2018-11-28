#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <utility>
#include <functional>
#include <iterator>
#include <complex>
#include <valarray>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define f(i,n) for(int i=0; i <n;i++)
#define fi(i,s,n) for(int i=s; i<n;i++)

typedef long long ll;
#define isx(i,j) (b[i][j]=='X' || b[i][j]=='T')
#define isy(i,j) (b[i][j]=='O' || b[i][j]=='T')
int main(){
	int tc;
	scanf("%d",&tc);
	char b[4][5];
	f(i,tc){
		f(j,4){
			scanf("%s",b[j]);
		}
		
		int d1x=0,d1y=0,d2x=0,d2y=0;
		bool fx=false,fy=false;
		printf("Case #%d: ",i+1);
		int num=0;
		f(j,4){
			int rx =0,ry=0,cx=0,cy=0;
			f(k,4){
			rx+=isx(j,k);
			ry+=isy(j,k);
			cx+=isx(k,j);
			cy+=isy(k,j);
			num+=b[k][k]!='.';
			}
			if(rx==4 || cx==4){fx = true; break;}
			else if (ry==4 || cy==4){fy=true;break;}
			d1x+=isx(j,j);
			d1y+=isy(j,j);
			d2x+=isx(j,3-j);
			d2y+=isy(j,3-j);
		}
		if(d1x==4||d2x==4||fx)printf("X won\n");
		else if (d2y==4||d1y==4||fy)printf("O won\n");
		else if (num==16)printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
