#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
vector<int> v[100];
int links[100][100];
int left_node[100];
bool u[100];
int n,m;
bool dfs(int x){
    u[x]=1;
    for(int i=0;i<n;++i)
        if(left_node[i]==-1 && links[x][i]){
            u[x]=0;
            left_node[i]=x;
            return true;
        }
    for(int i=0;i<n;++i)
        if(links[x][i] && !u[left_node[i]] && dfs(left_node[i])){
            u[x]=0;
            left_node[i]=x;
            return true;
        }
    return false;
}
int matching(){
    memset(left_node,-1,sizeof(left_node));
    int sum=0;
    for(int i=0;i<n;++i){
		memset(u,0,sizeof(u));
        if(dfs(i))
            ++sum;
    }
    return sum;
}

int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;++k){
		cin>>n>>m;
		memset(links,0,sizeof(links));
		for(int i=0;i<n;++i){
			v[i].clear();
			for(int j=0;j<m;++j){
				int t;
				cin>>t;
				v[i].push_back(t);
			}
		}
		sort(v,v+n,greater<vector<int> >());
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j){
				bool ok=true;
				for(int ll=0;ll<m;++ll)
					if(v[i][ll]<=v[j][ll]){
						ok=false;
						break;
					}
				if(ok)
					links[i][j]=true;
			}
		printf("Case #%d: %d\n",k,n-matching());
	}
	return 0;
}
