#include <iostream>
#include <map>
#include <fstream>

using namespace std;

int chess[513][513];
int n,m;

map<int, int> mm;
map<int, int>::iterator mit;

int ans[513][2];

int find(int x,int y) {
	int i, k, c;
	i = k = c = chess[x][y];
	if(c==2) return 0;
	
	k=1;
	bool t;
	while(x+k-1 <= m && y+k-1 <= n) {
		t = true;
		if(k%2 == 0) {
			c = chess[x][y]^1;
		} else {
			c = chess[x][y];
		}
		
		for(i = 0;i < k; i++) {
			if(chess[x+i][y+k-1] != c) {
				t=false;
				break;
			};
			c = c^1;
		}
		
		if(k%2 == 0) {
			c=chess[x][y]^1;
		} else {
			c=chess[x][y];
		}
		
		for(i = 0; i < k; i++) {
			if(chess[x+k-1][y+i]!=c) {
				t=false;
				break;
			}
			c=c^1;
		}
		if(!t) break;
		k++;
	}
	return k-1;
}

void clear(int x,int y,int k) {
	int i,j;
	for(i = x; i < x+k; i++) {
		for(j = y; j < y+k; j++) { 
			chess[i][j]=2;
		}
	}
}

int main(){
	ifstream in("C-small-attempt1.in");
	ofstream out("small.out");
	
	int c;
	
	in>>c;
	
	char s[10];
	int p, mmax;
	int x, y;
	int j;
	
	for(int i = 1; i <= c; i++) {
		mm.clear();
		in>>m>>n;
		for(j = 1; j <= m; j++) {
			in>>s;
			for(int k = 0; k < n/4; k++) {
				if('0' <= s[k] && s[k] <= '9') {
					p = s[k]-'0';
				} else {
					p = s[k] - 'A' + 10;
				}
				chess[j][k*4+4] = (p&1); p = (p>>1);
				chess[j][k*4+3] = (p&1); p = (p>>1);
				chess[j][k*4+2] = (p&1); p = (p>>1);
				chess[j][k*4+1] = (p&1); p = (p>>1);
			}
		}
		
		while(true) {
			mmax=0;
			for(j = 1; j <= m; j++) {
				for(int k = 1; k <= n; k++) {
					p = find(j, k);
					if(p > mmax) {
						mmax = p;
						x = j;
						y = k;
					}
				}
			}
			if(mmax == 0) break;
			mm[mmax]++;
			clear(x, y, mmax);
		}
		out<<"Case #"<<i<<": "<<mm.size()<<endl;
		
		j = 0;
		for(mit = mm.begin(); mit != mm.end(); mit++) {
			++j;
			ans[j][0] = mit->first;
			ans[j][1] = mit->second;
		}
		
		for(j = mm.size(); j > 0; j--) out<<ans[j][0]<<" "<<ans[j][1]<<endl;
	}
	return 0;
}