#include <iostream>
#include <vector>
#include <string>
//#include <algorithm>
#include <set>
using namespace std;

int main()
{
	int t_case;
	scanf("%d", &t_case);

	int N,M;
	char cPath[1024];
	for(int t=1; t <= t_case; ++t)
	{
		int ans=0;

		vector<string> already;
		vector<string> toMake;
		set<string> madeDic;
		set<string> willMake;
		scanf("%d %d", &N, &M);

		for(int i=0; i < N; ++i){
			scanf("%s", cPath);
			already.push_back(cPath);
		}

		for(int i=0; i < M; ++i){
			scanf("%s", cPath);
			toMake.push_back(cPath);
		}

		for(int i=0; i < (int)already.size(); ++i){
			madeDic.insert(already[i]);
			for(int j=0; j < already[i].size(); ++j){
				if( j != 0 && already[i][j] =='/' )
					madeDic.insert( already[i].substr(0, j) );
			}
		}
		//for(set<string>::iterator iter = madeDic.begin(); iter != madeDic.end(); ++iter)
		//	printf("%s\n", iter->c_str());

		for(int i=0; i < (int)toMake.size(); ++i){
			willMake.insert(toMake[i]);
			for(int j=0; j < toMake[i].size(); ++j){
				if( j!= 0 && toMake[i][j] =='/' )
					willMake.insert( toMake[i].substr(0, j) );
			}
		}

		//for(set<string>::iterator iter = willMake.begin(); iter != willMake.end(); ++iter)
		//	printf("%s\n", iter->c_str());
		
		set<string>::iterator iter = willMake.begin();
		for(; iter != willMake.end(); ++iter){
			if( madeDic.find( *iter ) == madeDic.end() ){
				ans+=1;
				madeDic.insert(*iter);
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}