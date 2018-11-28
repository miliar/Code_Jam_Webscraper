#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int count = 1;
	cin>>T;
	while ( T-- ){
		vector<char> result;
		char comb[100][100];
		char oppo[100][26];
		int oppo_count[100];
		int ahead = 0,has = 0;
		memset( comb, 0, sizeof(comb));
		memset( oppo, 0, sizeof(oppo));
		memset( oppo_count, 0, sizeof(oppo_count));
		int C,D,N;
		int i;
		char x,y;
		int a,b;
		cin>>C;
		for ( i = 0; i < C; i++ ){
			cin>>x>>y;
			a = x;
			b = y;
			cin>>comb[a][b];
			comb[b][a] = comb[a][b];
		}
		cin>>D;
		for ( i = 0; i < D; i++ ){
			cin>>x>>y;
			a = x;
			b = y;
			oppo[a][ oppo_count[a] ] = y;
			oppo[b][ oppo_count[b] ] = x;
			oppo_count[a]++;
			oppo_count[b]++;
		}
		cin>>N;
		for ( i = 0; i < N; i++ ){
			cin>>x;
			a = x; 
			if ( result.empty()){
				result.push_back(x);
			}
			else{
				b = result[result.size()-1];
				if ( comb[a][b] != 0 ){
					result.pop_back();
					result.push_back(comb[a][b]);
					ahead = 1;
				}
				if ( ahead == 0){
					for ( int j = 0; j < oppo_count[a]; j++ ){
						vector<char>::iterator iter = find( result.begin(),result.end(),oppo[a][j]);
						if (  iter != result.end() ){
							has = 1;
							break;
						}
					}
				    if ( has == 1 ){
						result.clear();
					}
					else{
						result.push_back(x);
					}
				}
				ahead = 0;
				has = 0;
			}
		}
		cout<<"Case #"<<count<<": ["<<flush;
		for ( i = 0; i < result.size(); i++ ){
			if ( i < result.size()-1 )cout<<result[i]<<", "<<flush;
			else cout<<result[i]<<flush;
		}
		cout<<"]"<<endl;
		count++;
	}
	return 0;
}