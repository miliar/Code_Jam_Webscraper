#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
	int T,t;
	long long R,k,n,g;
	long long ans;
	long long i,j,x,y,z;
	
	cin>>T;
	t = 1;
	while(T--){
		cin>>R>>k>>n;
		vector<long long> visit(n,-1),v,vv;
		queue<long long> q;
		
		for(i=0;i<n;i++){
			cin>>g;
			q.push(i);
			v.push_back(g);
		}
		
		ans = 0;
		for(i=0;i<R;i++){
			x = q.front();
			if(visit[x] != -1)
				break;
				
			visit[x] = i;
			vector<long long> ve;
			y = 0;
			while(!q.empty()){
				x = q.front();
				x = v[x];
				if((y+x) <= k)
					y += x;
				else
					break;
				ve.push_back(q.front());
				q.pop();
			}
			ans += y;
			vv.push_back(y);
			for(j=0;j<ve.size();j++)
				q.push(ve[j]);
		}
		
		if(i<R){
			i = R-i;
			x = q.front();
			y = 0;
			vector<long long> ve;
			for(j=visit[x];j<vv.size();j++){
				y += vv[j];
				ve.push_back(y);
			}
			x = ve.size();
			z = i/x;
			ans += (z*y);
			z = i%x;
			if(z>0)
				ans += ve[z-1];
		}
		printf("Case #%d: ",t);
		cout<<ans<<endl;
		t++;
	}
	return 0;
}
	
		
			
		