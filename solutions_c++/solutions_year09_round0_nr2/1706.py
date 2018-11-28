#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cctype>
#include <climits>
#include <cassert>

using namespace std;

#define HH 101
#define WW 101

int mm[HH][WW];
char mmap[HH][WW];
int h,w;
char ch = 'a';

void fall_down(int x,int y)
{
	if (mmap[x][y] != 0){
		return ;
	}
	
	mmap[x][y] = ch;
	int nx = x,ny = y;
	if (x > 0 && mm[x-1][y] < mm[nx][ny]){
		nx = x-1;
		ny = y;
	}
	if (y > 0 && mm[x][y-1] < mm[nx][ny]){
		nx = x;
		ny = y-1;
	}
	if (y < w-1 && mm[x][y+1] < mm[nx][ny]){
		nx = x;
		ny = y+1;
	}
	if (x < h-1 && mm[x+1][y] < mm[nx][ny]){
		nx = x+1;
		ny = y;
	}
	if (nx == x && ny==y){
		ch++;
		return ;
	}
	if (mmap[nx][ny]==0){
		fall_down(nx,ny);
	}else{
		for (int i = 0;i < h ;i++){
			for (int j = 0; j < w ;j++){
				if (mmap[i][j] == ch){
					mmap[i][j] = mmap[nx][ny];
				}
			}
		}
	}
}
int main()
{
//	freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T;
	cin >> T;
	for (int i = 0;i < T ;i++){
		cin >> h >> w;
		for (int hh = 0 ;hh < h ;hh++){
			for (int ww = 0 ;ww < w ;ww++){
				cin >> mm[hh][ww];
			}
		}
		memset(mmap,0,sizeof(mmap));
		ch = 'a';
		for (int x = 0 ;x < h ;x++){
			for (int y = 0 ;y < w ;y++){
				fall_down(x,y);
			}
		}
		cout << "Case #" << i+1 << ":" << endl;
		for (int i = 0 ;i < h ;i++){
			for (int j = 0 ;j < w-1 ;j++){
				cout << mmap[i][j] << ' ';
			}
			cout << mmap[i][w-1] << endl;
		}
	}
	return 0;
}
