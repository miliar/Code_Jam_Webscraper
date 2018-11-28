#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;
ll M[1024 * 1024];
ll cost[1024 * 1024];

vector<int> getMatches(int id, int p){
	vector<int> result;        
	int cur_size = 0;
	int z = p + 1;
	for (int i = 0; i < z; i++){
		result.push_back(id / 2 + cur_size);
		id = id / 2;
		cur_size += (1 << p);
		p--;
	}
	return result;
}

bool Need(vector<int> & childs){
	for (int i = 0; i < childs.size(); i++)
		if (M[childs[i]]) return true;
	return false;
}

void Dec(vector<int> & childs){
	for (int i = 0; i < childs.size(); i++)
		if (M[childs[i]])
			M[childs[i]]--;// return true;
}

void doTest(int test){
	int p;
	scanf("%d",&p);
	int size = (1 << p);
	for (int i = 0; i < size; i++){
		scanf("%lld",&M[i]);
		M[i] = p - M[i];
	}
	for (int i = 0; i < size - 1; i++)
		scanf("%lld",&cost[i]);
	set<int> matches;
	vector<vector<int> > childs(size - 1);
	for (int i = 0; i < size; i++){
		vector<int> need = getMatches(i, p - 1);
		for (int j = 0; j < need.size(); j++)
			childs[need[j]].push_back(i);
	}
	ll result = 0;
	for (int i = size - 2; i >= 0; i--){
		if (Need(childs[i])){
			result += cost[i];
			Dec(childs[i]);
		}
	}
	printf("Case #%d: %lld\n",test,result);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	for (int i = 1; i <= t; i++)
 		doTest(i);	
	
	return 0;
}