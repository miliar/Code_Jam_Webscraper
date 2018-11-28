
#include <fstream>
//#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
int **P;
char **C;
int T,H,W;
ifstream cin;
ofstream cout;
map<pair<int,int>,pair<int,int> > issink;
char counter;
bool inrange(int i, int j) {
	if (i<0) return false;
	if (i>H-1) return false;
	if (j<0) return false;
	if (j>W-1) return false;
	return true;
}
pair<int,int> getsink(int i,int j) {
	pair<int, pair<int,int> > zmin = make_pair(10001,make_pair(1,1));
	if (inrange(i-1,j)) { zmin = make_pair<int,pair<int,int>>(P[i-1][j],make_pair<int,int>(i-1,j)); }
	if (inrange(i,j-1)) { zmin = min(zmin,make_pair(P[i][j-1],make_pair(i,j-1))); }
	if (inrange(i,j+1)) { zmin = min(zmin,make_pair(P[i][j+1],make_pair(i,j+1))); }
	if (inrange(i+1,j)) { zmin = min(zmin,make_pair(P[i+1][j],make_pair(i+1,j))); }
	if (P[i][j] <= zmin.first) zmin = make_pair(P[i][j],make_pair(i,j));
	return zmin.second;
}
char DFS(int i,int j) {
	if (C[i][j] != '0') { return C[i][j]; }
	pair<int,int> zpair;
	zpair = issink[make_pair(i,j)];
	if (zpair.first == -1) {
	C[i][j] = counter++;
	return C[i][j];
	}
	C[i][j] = DFS(zpair.first,zpair.second);
}
int main() {
	cin.open("B-small-attempt1.in");
	cout.open("B-small-1.out");
	cin >> T;
	for (int i=0; i<T ;i++) {
		counter = 'a';
		cin >> H >> W;
		P = new int*[H];
		C = new char*[H];
		for (int k=0; k<H; k++){ 
			P[k] = new int[W];
			C[k] = new char[W];
			for (int w=0; w<W; w++) {
				P[k][w] = 10001;
				C[k][w] = '0';
			}
		}

		//load
		for (int j=0; j<H; j++) {
			for (int k=0; k<W; k++) {
				cin >> P[j][k];
			}
		}

		//process
		pair<int,int> slow;
		for (int j=0; j<H; j++) {
			for (int k=0; k<W; k++) {
				slow = getsink(j,k);
				if (slow.first == j && slow.second == k)  { issink[make_pair(j,k)] = make_pair(-1,-1); }
				else
				issink[make_pair(j,k)] = make_pair(slow.first,slow.second);
			}
		}
		//DFS
		for (int j=0; j<H; j++) {
			for (int k=0; k<W; k++) {
				if (C[j][k] == '0') { char cl = DFS(j,k); }
			}
		}
		//print
		cout << "Case #"<<i+1<<":"<<endl;
		for (int i=0; i<H; i++) {
			for (int j=0; j<W; j++) {
				cout << C[i][j] << " ";
			}
			cout << endl;
		}
		//delete
		
		for (int j=0; j<H; j++) {
			delete [] P[j];
			delete [] C[j];
		}
	}
}