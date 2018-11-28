#include <iostream>
#include <vector>
using namespace std;
const int MAX_TEAMS=1<<10;
vector<vector<int> >C;
int M[MAX_TEAMS];
int getMinimum(int p){
	int n=1<<p;
	int total=0;
	while(n>1){
		for(int i=0;i<n;i+=2){
			if((M[i]==0) || (M[i+1]==0)){
				++total;
				M[i]=0;
			}else{
				M[i]=min(M[i], M[i+1])-1;
			}
		}
		n/=2;
		for(int i=0;i<n;++i){
			M[i]=M[2*i];
		}
	}
	return total;
}

int main(){
	int T;
	cin>>T;
	for(int caseNum=1; caseNum<=T;++caseNum){
		int p,n;
		cin>>p;
		n=1<<p;
		for(int i=0;i<n;++i){
			cin>>M[i];
		}
		int q=p;
		while(q){
			vector<int> costs;
			for(int i=0;i<(1<<(q-1));++i){
				int c;
				cin>>c;
				costs.push_back(c);
			}
			C.push_back(costs);
			--q;
		}
		int sol=getMinimum(p);
		cout<<"Case #"<<caseNum<<": "<<sol<<endl;
	}
	return 0;
}
