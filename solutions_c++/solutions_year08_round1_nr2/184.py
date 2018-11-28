#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

bool my_comp(const pair<set<int>,int> &a,const pair<set<int>,int> &b){
	return a.first.size()<b.first.size();
}

int main(){
	int C; cin>>C;
	for(int num=1;num<=C;num++){
		int N,M; cin>>N>>M;
		vector<pair<set<int>,int> > m;
		for(int i=0;i<M;i++){
			int T; cin>>T;
			set<int> s;
			int m_n=-1;
			for(int j=0;j<T;j++){
				int X,Y; cin>>X>>Y;
				if(Y==1){
					m_n=X;
				}
				else{
					s.insert(X);
				}
			}
			m.push_back(make_pair(s,m_n));
		}
		
		vector<int> ans(N,0);
		bool impossible=false;
		for(;m.size()>0;){
			sort(m.begin(),m.end());
			if(m[0].first.size()>=1){
				break;
			}
			
			int m_n=m[0].second;
			if(m_n==-1){
				impossible=true;
				break;
			}
			ans[m_n-1]=1;
			
			for(int i=0;i<m.size();i++){
				m[i].first.erase(m_n);
			}
			m.erase(m.begin());
		}
		
		cout<<"Case #"<<num<<":";
		if(impossible){
			cout<<" IMPOSSIBLE"<<endl;
		}
		else{
			for(int i=0;i<ans.size();i++){
				cout<<' '<<ans[i];
			}
			cout<<endl;
		}
	}
	return 0;
}
