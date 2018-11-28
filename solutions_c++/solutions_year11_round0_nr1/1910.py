#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int,int> >ve;
int ans, n, ret;
int O, B;
int _abs(int t){
	if(t > 0) return t;
	return -t;
}
int next(int k,int t){
	for(int i = k+1;i < ve.size(); ++i)
		if(ve[i].first == t) return i;
	return -1;
}
void move(int k,int cost){
	if(k == -1) return;
	pair<int,int> t = ve[k];
	if(t.first == 0 && t.second == O) return;
	if(t.first == 1 && t.second == B) return;
	int cc;
	if(t.first == 0){
		cc = _abs(O - t.second);
		if(cc <= cost){
			O = t.second;
			return;
		}else{
			if(O > t.second) O -= cost;
			else O += cost;
			return;
		}
	}
	else{
		cc = _abs(B - t.second);
		if(cc <= cost){
			B = t.second;
			return;
		}else{
			if(B > t.second) B -= cost;
			else B += cost;
			return;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int T, t;
	char ch[2];
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%d",&n);
		ve.clear();
		ans = 0;
		for(int i = 1;i <= n; ++i){
			scanf("%s%d",ch,&t);
			if(ch[0] == 'O') ve.push_back(make_pair(0,t));
			else ve.push_back(make_pair(1,t));
		}
		O = B = 1;
		for(int i= 0;i < ve.size(); ++i){
			pair<int,int> t;
			t = ve[i];
			int rt = next(i,!t.first);
			int cost;
			if(t.first == 0){ cost = _abs(O - t.second) + 1; O = t.second;}
			else            { cost = _abs(B - t.second) + 1; B = t.second;}
			move(rt,cost);
			ans += cost;
		}
		printf("Case #%d: %d\n",it,ans);
	}
}
