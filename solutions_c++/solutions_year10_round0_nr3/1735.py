#include <iostream>
#include <map>
#include <set>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
	int T,g[1024];
	cin>>T;
	for(int round=1; round<=T; round++){
		int R,k,N;
		long long ans = 0;
		cin>>R>>k>>N;
		memset(g,0,sizeof(g));
		vector<int> v;
		vector< pair<vector<int>,long long> > vv;
		set<int> st;
		set<vector<int> > set_vec;
		set<vector<int> >::iterator it_setv;
		for(int i=0; i<N; i++){ int a; cin>>a; st.insert(a); v.push_back(a); }
		
		for(int r=0; r<R; r++){
			vector<int> hikae = v;
			long long sum = 0;
			int j,cnt=0;
			int n = st.size();
			
			for(j=0; j<N; j++){
				if( sum+v[j]>k )break;
				sum += v[j];
				v.push_back( v[j] );
			}
			v.erase( v.begin(), v.begin()+j );			
			
			//for(int i=0; i<v.size(); i++)cout<<v[i]<<",";
			//cout<<":"<<sum<<"___ans:"<<ans<<endl;

			it_setv = set_vec.find( hikae );
			if( it_setv != set_vec.end() ){
				int i,shuuki,amari,nokori;
				for(i=0; i<vv.size(); i++)if( vv[i].first==hikae )break;
				shuuki = vv.size() - i;
				cnt = R-r;
				amari  = cnt % shuuki;
				for(; i<vv.size() && cnt>0 ; i++){
					ans += ( vv[i].second * ( (R-r)/shuuki + ( amari>0 ? 1: 0 ) ) );
					if( amari>0 )amari--;
					cnt--;
				}
				break;
			}else{
				set_vec.insert( hikae );
				vv.push_back( make_pair(hikae,sum) );
				ans += sum;
			}
		}
		printf("Case #%d: %lld\n",round,ans);
	}
	
	return 0;
}
