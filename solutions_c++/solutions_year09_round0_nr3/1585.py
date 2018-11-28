#include <iostream>
#include <iomanip>
using namespace std;
int M[501][501];
char text[501];
char *pattern;
int getCount(int _p, int _t){
	if(M[_p][_t]>=0){
		return M[_p][_t];
	}
	if(pattern[_p]==0){
		return M[_p][_t]=1;
	}
	if(text[_t]==0){
		return M[_p][_t]=0;
	}
	int total=0;
	int t=_t;
	int p=_p;
	while(text[t]!=0){
		while((text[t]!=0) && (text[t]!=pattern[p]))
			++t;
		if(text[t]==pattern[p]){
			total=(total+getCount(p+1,t+1))%10000;
			++t;
		}
	}
	return M[_p][_t]=total;
}


int main(int argc, char*argv[]){
	int N;
	cin>>N;
	cin.getline (text,500);
	pattern="welcome to code jam";
	for(int caseNum=1;caseNum<=N;++caseNum){
		cin.getline (text,500);
		memset(M, -1, sizeof(M));
		int sol=getCount(0,0);
		cout<<"Case #"<<caseNum<<": "<<setfill('0')<<setw(4)<<sol<<endl;
	}
	return 0;
}
