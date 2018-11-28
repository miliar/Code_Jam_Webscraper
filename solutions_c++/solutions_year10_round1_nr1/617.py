#include <iostream>
#include <vector>
#include <string>
using namespace std;
int dRow[]={1, 0, 1, 0,  1};
int dCol[]={0, 1, 1, 1, -1};

bool isALine(char target, int K, vector<string> &B, int r, int c, int dir){
	if(B[r][c]!=target){
		return false;
	}
	int N=B.size();
	int rr=r+(K-1)*dRow[dir];
	int cc=c+(K-1)*dCol[dir];
	if(((0<=rr) && (rr<N))&&((0<=cc) && (cc<N))){
		for(int i=1;i<K;++i){
			r+=dRow[dir];
			c+=dCol[dir];
			if(B[r][c]!=target){
				return false;
			}
		}
		return true;
	}else{
		return false;
	}
}

bool isALine(char c, int K, vector<string> &B){
	int N=B.size();
	for(int dir=0;dir<5;++dir){
		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j){
				if(isALine(c,K,B,i,j,dir)){
					return true;
				}

			}
		}
		
	}
	return false;
}

int main(int argc, char *argv[]){
	int T, N, K;
	cin>>T;
	for(int caseNum=1;caseNum<=T;++caseNum){
		cin>>N>>K;
		vector<string> B;
		string sol;
		for(int i=0;i<N;++i){
			string nextLine;
			cin>>nextLine;
			B.push_back(nextLine);
		}
		int M=B[0].size();
		vector<string>BB;
		for(int i=0;i<N;++i){
			string s;
			for(int j=0;j<M;++j)if(B[i][j]!='.'){
				s+=B[i][j];
			}
			while(s.size()<B[i].size()){
				s="."+s;
			}
			BB.push_back(s);
		}
		bool rLine=isALine('R',K,BB);
		bool bLine=isALine('B',K,BB);
		if(rLine && bLine){
			sol="Both";
		}else if(rLine){
			sol="Red";
		}else if(bLine){
			sol="Blue";
		}else{
			sol="Neither";
		}
		cout<<"Case #"<<caseNum<<": "<<sol<<endl;
	}
	return 0;
}