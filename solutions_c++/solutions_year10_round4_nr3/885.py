#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

#define INF 999999
#define pb push_back
#define sz(x) ((int)((x).size()))
#define all(x) (x).begin(),(x).end()
#define db double
#define ll long long
#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define forn(i,a,n) for (int (i)=(a); (i)<(n); ++(i))
#define VI vector<int>
#define VB vector<bool>
#define MAXN 110

bool mas[2][MAXN][MAXN];
bool fr[MAXN][MAXN];
#define EPS 10E-5
int R;
int curr,next;
void print(){
	rep(i,15){
		rep(j,15)
			if (mas[curr][i][j])
				putchar('#');
			else
				putchar('.');
		putchar('\n');
	}
	putchar('\n');
}
int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int C;
	scanf("%d",&C);
	int tmp;
	int x1,y1,x2,y2;
	int size = sizeof(mas[1]);
	rep(qwer,C){
		scanf("%d",&R);
		curr = 0;
		next = 1;
		
		rep(c,R){
			scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
			for (int i = x1 - 1; i < x2; ++ i)
				for (int j = y1 - 1; j < y2; ++ j)
					mas[next][i][j] = mas[curr][i][j] = 1;
		}
		bool b = 1;
		int day = 0;
		while (b){
			++day;
			b = 0;
			for (int i = 1; i < MAXN; ++ i){
				if ((mas[curr][i][0] == 1) && (mas[curr][i-1][0] == 0))
					mas[next][i][0] = 0;
				if ((mas[curr][0][i] == 1) && (mas[curr][0][i-1] == 0))
					mas[next][0][i] = 0;
			}
			for (int i = 1; i < MAXN; ++ i)
				for (int j = 1; j < MAXN; ++ j){
					if (mas[curr][i][j]){
						if ((mas[curr][i-1][j] == 0) && (mas[curr][i][j-1] == 0))
							mas[next][i][j] = 0;
						else{
							b = 1;
							mas[next][i][j] = 1;
						}
					}
					if (mas[curr][i-1][j] && mas[curr][i][j-1] && (!mas[curr][i][j])){
						b = 1;
						mas[next][i][j] = 1;
					}
				}
			//print();
			memcpy(mas[curr],fr,size);
			swap(next,curr);
		}
		int ans = day;
		printf("Case #%d: %d\n",qwer+1,ans);
	}
	return 0;
}