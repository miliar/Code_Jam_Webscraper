#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

const int M = 111;
const int A = 0x7fffffff;
int map[M][M];
char labels[M][M];

void findLetter(int i,int j,char &l) {
	vector<pair<int,int> > path;

	while (labels[i][j] == 0) {
		path.push_back(make_pair(i,j));
		int ni=i,nj=j;
		if (map[i-1][j] < map[ni][nj]) {
			ni = i-1;
			nj = j;
		}
		if (map[i][j-1] < map[ni][nj]) {
			ni = i;
			nj = j-1;
		}
		if (map[i][j+1] < map[ni][nj]) {
			ni = i;
			nj = j+1;
		}
		if (map[i+1][j] < map[ni][nj]) {
			ni = i+1;
			nj = j;
		}
		if (ni == i && nj == j) {
			labels[i][j] = l++;
		} else {
			i = ni;
			j = nj;
		}
	}
	for (size_t ip=0; ip<path.size(); ++ip) {
		labels[path[ip].first][path[ip].second] = labels[i][j];
	}
}

int main(void) {
	int t;
	
	scanf("%d",&t);

	for (int it=1; it<=t; ++it) {
		int h,w;
		scanf("%d%d",&h,&w);
		for (int ih=1; ih<=h; ++ih) {
			map[ih][0] = map[ih][w+1] = A;
			labels[ih][0] = labels[ih][w+1] = 0;
			for (int iw=1; iw<=w; ++iw) {
				scanf("%d",map[ih]+iw);
				labels[ih][iw] = 0;
			}
		}
		for (int iw=0; iw<=w+1; ++iw) {
			map[0][iw] = map[h+1][iw] = A;
			labels[0][iw] = labels[h+1][iw] = 0;
		}
		printf("Case #%d:\n",it);
		char letter = 'a';
		for (int ih=1; ih<=h; ++ih) {
			for (int iw=1; iw<=w; ++iw) {
				if (labels[ih][iw] == 0) {
					findLetter(ih,iw,letter);
				}

				printf("%c",labels[ih][iw]);
				printf(iw<w? " ":"\n"); 
			}

		}
	}

	return 0;
}
