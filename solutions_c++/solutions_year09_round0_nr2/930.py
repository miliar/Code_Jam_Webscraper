#include<iostream>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<algorithm>
#include<iterator>
#include<stack>
#include<sstream>
#include<numeric>
#include<cctype>
#include<cmath>
#include<cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a ; i<b ; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define VI vector<int>
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
#define mi 10001

int found;
int countN;

void colorAll(int y,int x,vector<vector<int> > &v,vector<vector<int> > &m) {
	//start with x & y color all nodes.
	int arr[]= {0,1,-1};
	int H=v.size(),W=v[0].size();
	int miX=-1,miY=-1,minN=mi;
	FOR(i,0,3) {
		FOR(j,0,3) {
			if(abs(arr[i]+arr[j]) == 1) { // check a neighbour
				if(y+arr[i] >=0 && y+arr[i] < H && x+arr[j]>=0 && x+arr[j] < W) {
					if(v[y+arr[i]][x+arr[j]] < v[y][x]) {
						if(v[y+arr[i]][x+arr[j]]< minN) {
							miX = x+arr[j];
							miY = y+arr[i];
							minN = v[y+arr[i]][x+arr[j]];
						}
						else if(v[y+arr[i]][x+arr[j]] == minN) {
							if(y+arr[i] < miY || (y+arr[i] == miY && x+arr[j] < miX)) {
								miX = x+arr[j];
								miY = y+arr[i];
								minN = v[y+arr[i]][x+arr[j]];
							}
						}
					}
				}

			}
		}
	}
	if(miX == -1) {
		//its a sink
		m[y][x] = countN++;
		found = m[y][x];
	}
	else {
		//color it and call the function
		if(m[miY][miX] == -1) {
			colorAll(miY,miX,v,m);
			m[y][x] = found;
		}
		else { 
			m[y][x] = m[miY][miX];
			found = m[y][x];
		}
	}
	
	

}

int main() {
	int N,caseN=0;
	for(cin >> N ; caseN<N ; caseN++) {
		found=0; countN=0;
		int H,W;
		cin >> H >> W;
		vector<vector<int> > v(H,vector<int> (W,-1));
		FOR(i,0,H) {
			FOR(j,0,W) {
				cin >> v[i][j];
			}
		}

		vector<vector<int> > m(H,vector<int> (W,-1));
		FOR(i,0,H) {
			FOR(j,0,W) {
				if(m[i][j] == -1) {
					colorAll(i,j,v,m);
				}	
			}
		}
		cout << "Case #"<<caseN+1<<":" << endl;
		FOR(i,0,H) {
			FOR(j,0,W) {
				cout << (char)(m[i][j]+'a') << " ";
			}
			cout << endl;
		}

	
		
	}
	return 0;
}
