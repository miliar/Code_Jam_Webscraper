#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>

using namespace std;


int main(int argc, char **argv) {
	int N=0;
	cin>>N;
	for(int n=1;n<=N;n++){
		int P=0,K=0,L=0;
		cin>>P>>K>>L;
		vector<int> rpt(L,0);
		for(int l=0;l<L;l++){
			cin>>rpt[l];
		}
		sort(rpt.begin(),rpt.end(),greater<int>());
//		for(int l=0;l<L;l++)cout<<rpt[l]<<" ";
		int cnt=0;
		for(int l=0;l<L;l++){
			int lev=(l)/K+1;
//			cout<<"lev "<<lev<<endl;
				cnt+=rpt[l]*lev;
		}
		if(cnt>=0)
			cout<<"Case #"<<n<<": "<<cnt<<endl;
	}
	return 0;
}
