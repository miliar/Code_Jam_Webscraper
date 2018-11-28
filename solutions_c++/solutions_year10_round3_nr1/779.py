#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;
int N,K;
vector<string> rotate(vector<string > &board){
	string s1;
	vector<string> ret;
	string tmp;
	for(int i = 0; i<board.size(); i++){
		tmp = "";
		for(int j = 0; j<board[0].size(); j++)
			tmp += board[j][i];
		reverse(tmp.begin(), tmp.end());
		ret.push_back(tmp);
	}
	return ret;
}

int dx[] = {1,0,1,-1};
int dy[] = {0,1,1,-1};

string find(vector<string> &board){
	int cant = 0;
	int r=0,b=0;
	char last='.';
	for(int i = 0; i<N; i++){
		for(int j = 0; j<N; j++){
			for(int dir = 0; dir<4; dir++){
				cant = 0; last = '.';
				for(int k = 0; k<K; k++){
					int newPosr = i +dx[dir]*k;
					int newPosc = j +dy[dir]*k;
					if(newPosr < 0 || newPosr>=N || newPosc < 0 || newPosc>=N){
						cant = 0; last = '.'; break;
					}
					if(board[newPosr][newPosc] == '.') break;
					if(board[newPosr][newPosc] == last || last == '.') {cant++; last = board[newPosr][newPosc];}
					else {cant = 0; last = '.'; break;}
					if(cant == K){
						if(last == 'R') r=1;
						else if(last == 'B') b = 1;
						cant = 0;
					}
				}
			}
		}
	}
	if(b == 1 && r == 1) return "Both";
	else if(b == 1 && r == 0) return "Blue";
	else if(b == 0 && r == 1) return "Red";
	else return "Neither";
}

void gravity(vector<string> &board)
{
	for(int col = 0; col<board.size(); col++){
		for(int row = N-2; row>=0; row--){
			if((board[row][col] != '.') && (board[row+1][col] == '.')){
				swap(board[row][col], board[row+1][col]);
				row = N-1;
			}
		}
	}
}

int main(){
	ifstream in("A-large-practice.in");
	ofstream out("A-large-practice.out");
	int T;
	in >> T;
	for(int t = 0; t<T; t++){
		in >> N;
		int ret = 0;
		vector<int> A(N),B(N);
		for(int i = 0; i<N; i++){
			in >> A[i] >> B[i];
		}
		for(int i = 0; i<N; i++)
			for(int j = i+1; j<N; j++){
				if(A[i]>A[j] && B[i]<B[j]) ret++;
				if(A[i]<A[j] && B[i]>B[j]) ret++;
			}
		out << "Case #" << t+1 << ": " << ret << endl;
		cout << "Case #" << t+1 << ": " << ret << endl;
	}
}
