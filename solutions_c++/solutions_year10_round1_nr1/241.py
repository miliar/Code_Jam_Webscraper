#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n, kk;
string mp[maxn], mp_c[maxn];
char ch[10000];
int ax[4] = {-1,1,0,1},
	ay[4] = {1,	1,1,0};

void init_deal(){
}

void pri(){
	for(int i = 1;i<=n;i++)
		cout<<mp_c[i]<<endl;
}

void fall_down(){
	for(int i = n-1;i>=1;i--){
		for(int j = 1;j<=n;j++){
			int now = i;
			while(now+1<=n && 
				  mp_c[now+1][j] == '.' && 
				  mp_c[now][j] != '.'){
				swap(mp_c[now+1][j],mp_c[now][j]);
				now++;
			}

		}
	}
}

bool check(char ch){
	for(int i = 1;i<=n;i++)
	for(int j = 1;j<=n;j++)
	if(mp_c[i][j] == ch){
		for(int k = 0;k<4;k++){
			int tot = 1;
			int nx = i,
				ny = j;
			while(true){
				nx = nx+ax[k];
				ny = ny+ay[k];
				if(1<=nx && nx<=n &&
				   1<=ny && ny<=n &&
					mp_c[nx][ny] == ch){
					tot++;
					if(tot>=kk)return true;
				}
				else{
					break;
				}

			}
		}
	}
	return false;
	/*
	bool y1 = true, y2 = true;
	for(int i = 1;i<=n;i++){
		if(mp_c[i][i]!=ch)
			y1 = false;
		if(mp_c[i][n+1-i]!=ch)
			y2 = false;

		bool yes;
		
		yes = true;
		for(int j = 1;j<=n;j++){
			if(mp_c[i][j]!=ch){
				yes = false;
				break;
			}
		}

		if(yes)
			return true;
		
		yes = true;
		for(int j = 1;j<=n;j++){
			if(mp_c[j][i]!=ch){
				yes = false;
				break;
			}
		}

		if(yes)
			return true;
	}
	return y1 || y2;
	*/
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		init_deal();
		scanf("%d%d", &n, &kk);
		for(int i = 1;i<=n;i++){
			scanf("%s", ch);
			mp[i] = ch;
			mp[i] = " "+mp[i];
			mp_c[i] = mp[i];
		}
		for(int i = 1;i<=n;i++)
		for(int j = 1;j<=n;j++){
			mp_c[j][n+1-i] = mp[i][j];
		}

		//pri();

		fall_down();

		//pri();

		bool br,bb;

		br = check('R');
		bb = check('B');
		
		
		printf("Case #%d: ",ttt);

		int ans = 0;
		if(br)ans+=1;
		if(bb)ans+=2;

		if(ans == 3)
			printf("Both");
		else
		if(ans == 2)
			printf("Blue");
		else
		if(ans == 1)
			printf("Red");
		else
			printf("Neither");
		

		printf("\n");
	}
	

	return 0;
};

