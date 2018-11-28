#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

#define SZ(A) A.size()
#define ALL(A) A.begin(), A.end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define INF INT_MAX
#define PB push_back

int movi[4] = {-1,0,0,1};
int movj[4] = {0,-1,1,0};

int drains(int i, int j, vector<vector<int> > &map, int H, int W){

	int mi = map[i][j];
	int ret = -1;
	for(int k=0 ; k<4 ; k++)
		if((i+movi[k] >= 0) && (j+movj[k] >= 0) && (i+movi[k] < H) && (j+movj[k] < W) )		
			if(map[i+movi[k]][j+movj[k]] < mi){
				ret = k;
				mi = map[i+movi[k]][j+movj[k]];
			}

	return ret;
}


int main(){

	int T;
	cin >> T;
	for(int t=0; t<T ; t++){
		vector<vector<int> > map(102, vector<int>(102,0));
		vector<vector<int> > label(102, vector<int>(102,0));
		vector<vector<int> > todo; 
		int H, W;
		cin >> H >> W;
		for(int i=0 ; i<H ; i++)
			for(int j=0 ; j<W ; j++)
				cin >> map[i][j];

		int last = 1;
		for(int i=0 ; i<H ; i++){
			for(int j=0 ; j<W ; j++){
				if(label[i][j] != 0) continue;
				bool sink = false;
				int wi = i, wj = j;
				while(label[wi][wj] == 0){
					label[wi][wj] = last;
					int d = drains(wi,wj, map, H, W);
					if(d < 0) {
						sink = true;
						break;
					}
					wi += movi[d];
					wj += movj[d];
				}
				if(!sink){
					for(int ii=0 ; ii<H ; ii++)
					for(int jj=0 ; jj<W ; jj++)
						if(label[ii][jj] == last) label[ii][jj] = label[wi][wj];
				}else last++;
				
			}
		}


		cout << "Case #" << t+1 << ": " << endl;
		for(int i=0 ; i<H ; i++){
			for(int j=0 ; j<W-1 ; j++){
				cout << (char)(label[i][j]-1+'a') << " ";
			}
			cout << (char)(label[i][W-1]-1+'a')<< endl;
		}
	}

	return 0;
}
