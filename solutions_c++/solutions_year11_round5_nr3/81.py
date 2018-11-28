#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;

string s[111];
int n,m,d[11][11],c;

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		int ans = 0;
		cin >> n >> m;
		for(int i=0;i<n;i++) cin >> s[i];

		for(int i=0;i< (1 << (n*m));i++){
			if(i == 73){
				i++;
				i--;
			}
			int mm = i, good = true;
			memset(d, 0, sizeof(d));

			for(int j=0;j<n && good;j++)
				for(int k=0;k<m;k++){
					int xx = j, yy = k;
					c = mm&1;
					mm >>= 1;
					if(s[j][k] == '-'){
						if(c) yy++;else yy--;							
					}
					if(s[j][k] == '|'){	
						if(c) xx++;else xx--;							
					}
					if(s[j][k] == '\\'){
						if(c){
							yy++;
							xx++;
						}else{
							yy--;							
							xx--;
						}
					}
					if(s[j][k] == '/'){
						if(c){
							yy--;
							xx++;
						}else{
							yy++;							
							xx--;
						}
					}
					if(xx < 0) xx += n;
					if(yy < 0) yy += m;
					if(xx >= n) xx -= n;
					if(yy >= m) yy -= m;
					d[xx][yy]++;

					if(d[xx][yy] > 1){
						good = 0;
						break;
					}
				}
			if(good) ans++;
		}
		
		printf("Case #%d: ",_);
		cout << ans << endl;
	}
	return 0;
}
