#include <iostream>
#include <set>
#include <vector>
using namespace std;


typedef pair<int, int> pii;
set<pii> lived;

bool bad(pii x){
	pii north = make_pair(x.first, x.second - 1);
	pii west = make_pair(x.first - 1 , x.second);
	return (lived.find(north) == lived.end() && lived.find(west) == lived.end());
}

bool good(pii x){
	pii north = make_pair(x.first, x.second - 1);
	pii west = make_pair(x.first - 1 , x.second);
	return (lived.find(north) != lived.end() && lived.find(west) != lived.end());
}

vector<pii> add;
	vector<pii> del;
void step(){
	add.clear(); del.clear();
	for (set<pii> :: iterator itr = lived.begin(); itr != lived.end(); itr++){
		pii cur = *itr;
		if (bad(cur)) del.push_back(cur);
		pii zzz = make_pair(cur.first + 1, cur.second); 
		if (good(zzz)) add.push_back(zzz);
		zzz = make_pair(cur.first, cur.second + 1);
		if (good(zzz)) add.push_back(zzz);
	}
	for (int i = 0; i < add.size(); i++) lived.insert(add[i]);
	for (int i = 0; i < del.size(); i++) lived.erase(del[i]);
}

void doTest(int test){
	int r;
	scanf("%d",&r);
	lived.clear();// lived[1].clear();
	for (int i = 0; i < r; i++){
		int x1,x2;
		int y1,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				lived.insert(make_pair(x,y));		
	}
	int res = 0;
	while (lived.size()){
		res++; step();
	}
	printf("Case #%d: %d\n",test,res);
	fprintf(stderr,"Case #%d: %d\n",test,res);	
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int i = 1; i <= t; i++) doTest(i);

	return 0;
}