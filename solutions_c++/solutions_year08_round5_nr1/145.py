#include <iostream>
#include <cstring>
using namespace std;

const int MAX = 6000;

int sn;
char s[1000][33];
int sl[1000];
int sc[1000];

void input() {
	cin >> sn;
	for(int i=0;i<sn;i++) {
		cin >> s[i];
		sl[i] = strlen(s[i]);
		cin >> sc[i];
	}			
}

int minx, maxx;
int miny, maxy;

bool h[MAX+1][MAX+1];
bool v[MAX+1][MAX+1];

int h1[MAX+1];
int h2[MAX+1];
int v1[MAX+1];
int v2[MAX+1];


int dx[4] = {0,1,0,-1};
int dy[4] = {1, 0, -1, 0};

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		int d = 0;
		int x = MAX/2;
		int y = MAX/2;
		
		for(int i=-0;i<=MAX;i++)
			for(int j=0;j<=MAX;j++) {
				h[i][j] = false;
				v[i][j] = false;
			}
		
		for(int i=0;i<=MAX;i++) {
			v1[i] = MAX;
			v2[i] = 0;
			h1[i] = MAX;
			h2[i] = 0;
		}
		
		
		for(int i=0;i<sn;i++) {
			for(int j=0;j<sc[i];j++) {
				for(int k=0;k<sl[i];k++) {
					//cout << s[i][j] << endl;
					//cout << "P " << x << " " << y << endl;
					if(s[i][k] == 'R')
						d = (d+1)%4;
					else if(s[i][k] == 'L')
						d = (d-1+4)%4;
					else {
						if(d == 0) {
							v[x][y] = 1;
							v1[y] = min(v1[y], x);
							v2[y] = max(v2[y], x);
						}
						if(d==1) {
							h[x][y] = 1;
							h1[x] = min(y, h1[x]);
							h2[x] = max(y, h2[x]);
						}
						if(d==2) {
							v[x][y-1] = 1;
							v1[y-1] = min(v1[y-1], x);
							v2[y-1] = max(v2[y-1], x);
						}
						if(d==3) {
							h[x-1][y] = 1;
							h1[x-1] = min(y, h1[x-1]);
							h2[x-1] = max(y, h2[x-1]);
						}
						x += dx[d];
						y += dy[d];
					}
				}
			}
		}
		
		int cnt = 0;
		for(int i=0;i<MAX;i++) {
			bool in = false;
			for(int j=0;j<MAX;j++) {
				if(h[i][j])
					in = !in;
				if(!in) {
					bool up = false;
					bool down = false;
					bool left = false;
					bool right = false;
					
					if(h1[i] <= j)
						down = true;
					/*for(int k=0;k<=j;k++)
						if(h[i][k])
							down = true;*/
					if(h2[i] >= j+1)
						up = true;
					/*for(int k=j+1;k<=MAX;k++)
						if(h[i][k])
							up = true;*/
					
					if(v1[j] <= i)
						left = true;
					if(v2[j] >= i+1)
						right = true;
					/*for(int k=0;k<=i;k++)
						if(v[k][j])
							left = true;
					for(int k=i+1;k<=MAX;k++)
						if(v[k][j])
							right = true;*/
					
					if(up&&down || left&&right) {
						//cout << i << " " << j << endl;
						cnt++;
					}
				}
			}			
		}
		



		cout << "Case #" << casei << ": ";
		cout << cnt << endl;
	}
	return 0;
}
