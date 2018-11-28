#include<iostream>
#include<vector>
using namespace std;

int T,N,p,c,crnt[2],TS[2],ans,pos[2],id;
char r,dumi;
vector<int> seq;
vector<int> tombol[2];

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N;
		//cout<<"N: "<<N<<endl;
		tombol[0].clear(); tombol[1].clear(); seq.clear();
		for(int i=0;i<N;i++) {
			cin>>r>>p;
			//cout<<"r,p: "<<r<<" "<<p<<endl;
			if(r=='O') c=0; else c=1;
			tombol[c].push_back(p);
			seq.push_back(c);
		}
		ans=0; crnt[0]=0; crnt[1]=0; TS[0]=0; TS[1]=0;  pos[0]=1; pos[1]=1;
		for(int i=0;i<seq.size();i++) {
			id=seq[i];
			TS[id]=TS[id]+abs(tombol[id][crnt[id]]-pos[id]);
			pos[id]=tombol[id][crnt[id]];
			crnt[id]++;
			TS[id]=max(TS[id],ans);
			TS[id]++;
			ans=TS[id];
		}
		cout<<"Case #"<<tc<<": ";
		cout<<ans<<endl;
	}
}
