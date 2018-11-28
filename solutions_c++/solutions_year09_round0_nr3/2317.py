#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <sstream>
using namespace std;

char dst[] = "welcome to code jam";
char input[511];
bool used[511];

void dfs(const vector<vector<int> >& v, int nth, int res[19], long long& ans)
{
    if(nth == 19){	
	//cout<<nth<<endl;
	//for(int j = 0; j < 19; j++){
	    //cout<<input[res[j]];
	//}
	//cout<<endl;
	//cout<<input[res[18]]<<endl;
	ans++;
	return;
    }
    for(int j = 0; j < v[nth].size(); j++){
	if((nth == 0 || res[nth - 1] < v[nth][j]) && !used[v[nth][j]]){
	    used[v[nth][j]] = true;
	    res[nth] = v[nth][j];
	    dfs(v, nth + 1, res,  ans);
	    used[v[nth][j]] = false;
	}
    }
}

int solve(void)
{
    int ll = strlen(input), j, k, res[19];
    long long ans;
    vector<vector<int> > v;
    v.resize(19);
    for(j = 0; j < 19; j++){
	for(k = 0; k < ll; k++){
	    if(input[k] == dst[j]){
		v[j].push_back(k);
	    }
	}
    }
    memset(res, 0, sizeof(res));
    memset(used, false, sizeof(used));
    ans = 0LL;
    dfs(v, 0, res, ans);
    return ans % 1000;
}

int main()
{
    int N, j, ret;
    scanf("%d", &N);
    getchar();
    for(j = 1; j <= N; j++){
	memset(input, 0, sizeof(input));
	gets(input);
	ret = solve();
	printf("Case #%d: %04d\n", j, ret);
    }
    return 0;
}
