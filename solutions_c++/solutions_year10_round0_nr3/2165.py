#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
int strToInt(string str){
	int num;
	istringstream is(str);
	is >> num;
	return num;
}
string intToStr(int num){
	ostringstream os;
	os << num;
	return os.str();
}

ifstream fin("c://C-small-attempt0.in");
ofstream fout("c://C.out");
int T,R,k,N;
vector<int> gV,nV,nextV;
int preCircleLen,circleLen,circleStartIndex,preCircleE,circleE;
string ss;

void init(){
	getline(fin,ss);
	T = strToInt(ss);
}

void solveInput(){
	gV.clear();
	nV.clear();
	nextV.clear();

	getline(fin,ss);
	istringstream is(ss);
	is>>R>>k>>N;
	getline(fin,ss);
	istringstream is2(ss);
	int g;
	for(int i=0;i<N;i++){
		is2>>g;
		gV.push_back(g);
	}
	for(i=0;i<N;i++){
		int num = gV[i];
		int j = i;
		int nk = 1;
		while(num<=k && ++nk<=N+1){
			j = (j+1)%N;
			num += gV[j];
		}
		num -= gV[j];
		nV.push_back(num);
		nextV.push_back(j);
	}
}

void proccess(){
	vector<int> pathWays(N,0);
	int index = 0;
	int k = 1;
	while (pathWays[index]==0){
		pathWays[index] = k++;
		index = nextV[index];
	}
	preCircleLen = pathWays[index]-1;
	circleStartIndex = index;
	circleLen = k-pathWays[index];

	preCircleE = 0;
	index = 0;
	for(int i=0;i<preCircleLen;i++){
		preCircleE += nV[index];
		index = nextV[index];
	}
	circleE = 0;
	index = circleStartIndex;
	for(i=0;i<circleLen;i++){
		circleE += nV[index];
		index = nextV[index];
	}
}

int count(){
	int rt = 0;
	int index = 0;
	if(R<=preCircleLen){
		for(int i=0;i<R;i++){
			rt += nV[index];
			index = nextV[index];
		}
	}else{
		int n = (R-preCircleLen)/circleLen;
		int r = (R-preCircleLen)%circleLen;
		rt += preCircleE;
		rt += n*circleE;
		index = circleStartIndex;
		for(int i=0;i<r;i++){
			rt += nV[index];
			index = nextV[index];
		}
	}
	return rt;
}

int main(){
	init();
	for(int t=1;t<=T;t++){
		solveInput();
		proccess();
		int rt = count();
		fout<<"Case #"<<t<<": "<<rt<<endl;
	}
	return 0;
}