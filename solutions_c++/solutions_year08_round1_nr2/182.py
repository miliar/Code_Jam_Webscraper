#include<iostream>
#include<vector>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,m;
		cin>>n>>m;
		vector<int> ans(n+1,-1);
		vector<int> c(m+1,0);
		vector<vector<int> > s(n+1);
		vector<int> q;
		vector<int> y(m+1,0);
		bool res=false;
		for(int j=1;j<=m;j++){
			int f;
			cin>>f;
			for(int k=0;k<f;k++){
				int x,t;
				cin>>x>>t;
				if(t==1)
					y[j]=x;
				else{
					c[j]++;
					s[x].push_back(j);
				}
			}
		}
		for(int j=1;j<=m;j++)
			if(c[j]==0)
				q.push_back(j);
		for(int qs=0;qs<q.size();qs++){
			int x=y[q[qs]];
			if(ans[x]==0){
				res=true;
				break;
			}
			else if(ans[x]==-1){
				ans[x]=1;
				for(vector<int>::iterator j=s[x].begin();j!=s[x].end();j++)
					if(!--c[*j])
						if(y[*j]==0){
							res=true;
							break;
						}
						else
							q.push_back(*j);
			}
			if(res)
				break;
		}
		if(res)
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else{
			cout<<"Case #"<<i<<":";
			for(int j=1;j<=n;j++)
				cout<<" "<<(int)(ans[j]==1);
			cout<<endl;
		}
	}
}
