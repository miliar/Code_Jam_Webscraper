#include<iostream>
#include<vector>
using namespace std;

int T,crnt,N,C,L;
long long int t,elapsed,dist;
vector<long long int> advantage;
long long int loop[1000007];

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>L>>t>>N>>C;
		for(int i=0;i<C;i++) {
			cin>>loop[i];
		}
		elapsed=0LL;
		crnt=0;
		advantage.clear();
		for(int i=0;i<N;i++) {
			//cout<<"i: "<<i<<endl;
			dist=loop[crnt];
			if(elapsed>=t) {
				advantage.push_back(-dist);
				//cout<<"case 0, advantage: "<<dist<<endl;
			}
			else if(elapsed+2*dist>t) {
				advantage.push_back(-((elapsed+2*dist-t)/2));
				//cout<<"case 1, advantage: "<<((elapsed+2*dist-t)/2)<<endl;
			}
			elapsed+=2*dist;
			//cout<<"elapsed: "<<elapsed<<endl;
			crnt=(crnt+1)%C;
		}
		sort(advantage.begin(),advantage.end());
		//cout<<"yak"<<endl;
		for(int i=0;i<L&&i<advantage.size();i++) {
			//cout<<"i: "<<i<<endl;
			elapsed+=advantage[i];
		}
		cout<<"Case #"<<tc<<": "<<elapsed<<endl;
	}
}
