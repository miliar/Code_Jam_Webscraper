#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cassert>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

const int maxw = 32;
char a[maxw][maxw];
int w;

const int maxn = 256;
char was[maxn];
string res[maxn];
char ww[maxw][maxw][maxn];

struct pp{
	int y,x,val;
	string s;
	pp(){}
	pp(int y_,int x_, int val_,const string& s_):y(y_),x(x_),val(val_),s(s_){}
	pp(int y_,int x_, int val_,char c_):y(y_),x(x_),val(val_),s(){
		s += c_;
	}
	bool operator<(const pp& t)const{
		if (s.size() != t.s.size()) return s.size() < t.s.size();
		return s < t.s;
	}
	bool operator==(const pp& t)const{
		return s == t.s;
	}
};

void work( int k){
	memset(ww,0,sizeof(ww));
	Eo(k);
	//	int tosolve = maxn;
	vector<pp> v;
	for (int i = 0; i < w; i++)
		for (int j = 0; j < w; j++)
			if (isdigit(a[i][j]))
				v.push_back(pp(i,j,a[i][j]-'0',a[i][j]));
	int iters = 0;
	while (1){
		//		Eo(tosolve);
		iters++;
		Eo(iters);
		sort(v.begin(),v.end());
		queue<pp> q;
		bool did = false;
		for (int i = 0; i < v.size(); i++){
			if (v[i].val >= 0 && v[i].val < maxn && !was[v[i].val]){
				res[v[i].val] = v[i].s;
				was[v[i].val] = 1;
			}
			if (v[i].val == k){
				return;
			}
			if (!ww[v[i].y][v[i].x][v[i].val]){
				ww[v[i].y][v[i].x][v[i].val] = 1;
				q.push(v[i]);
			}
		}
		v.clear();
		while (!q.empty()){
			pp p = q.front();
			q.pop();
			if ((((p.y > 0 && a[p.y-1][p.x] == '+') || (p.y < w-1 && a[p.y+1][p.x] == '+') || (p.x > 0 && a[p.y][p.x-1] == '+') || (p.x < w-1 && a[p.y][p.x+1] == '+')))){
				int val = p.val + a[p.y][p.x] - '0';
				if (!ww[p.y][p.x][val])
					v.push_back(pp(p.y,p.x,val,p.s+'+'+a[p.y][p.x]));
			}
			if ((((p.y > 0 && a[p.y-1][p.x] == '-') || (p.y < w-1 && a[p.y+1][p.x] == '-') || (p.x > 0 && a[p.y][p.x-1] == '-') || (p.x < w-1 && a[p.y][p.x+1] == '-')))){
				int val = p.val - (a[p.y][p.x] - '0');
				if (!ww[p.y][p.x][val])
					v.push_back(pp(p.y,p.x,val,p.s+'-'+a[p.y][p.x]));
			}
			if (p.y > 0){
				if (p.x > 0){
					if (a[p.y-1][p.x] == '+' || a[p.y][p.x-1] == '+'){
						int val = p.val + a[p.y-1][p.x-1] - '0';
						if (!ww[p.y-1][p.x-1][val])
							v.push_back(pp(p.y-1,p.x-1,val,p.s+'+'+a[p.y-1][p.x-1]));
					}
					if (a[p.y-1][p.x] == '-' || a[p.y][p.x-1] == '-'){
						int val = p.val - (a[p.y-1][p.x-1] - '0');
						if (!ww[p.y-1][p.x-1][val])
							v.push_back(pp(p.y-1,p.x-1,val,p.s+'-'+a[p.y-1][p.x-1]));
					}
				}
				if (p.x < w-1){
					if (a[p.y-1][p.x] == '+' || a[p.y][p.x+1] == '+'){
						int val = p.val + a[p.y-1][p.x+1] - '0';
						if (!ww[p.y-1][p.x+1][val])
							v.push_back(pp(p.y-1,p.x+1,val,p.s+'+'+a[p.y-1][p.x+1]));
					}
					if (a[p.y-1][p.x] == '-' || a[p.y][p.x+1] == '-'){
						int val = p.val - (a[p.y-1][p.x+1] - '0');
						if (!ww[p.y-1][p.x+1][val])
							v.push_back(pp(p.y-1,p.x+1,val,p.s+'-'+a[p.y-1][p.x+1]));
					}
				}
			}
			if (p.y < w-1){
				if (p.x > 0){
					if (a[p.y+1][p.x] == '+' || a[p.y][p.x-1] == '+'){
						int val = p.val + a[p.y+1][p.x-1] - '0';
						if (!ww[p.y+1][p.x-1][val])
							v.push_back(pp(p.y+1,p.x-1,val,p.s+'+'+a[p.y+1][p.x-1]));
					}
					if (a[p.y+1][p.x] == '-' || a[p.y][p.x-1] == '-'){
						int val = p.val - (a[p.y+1][p.x-1] - '0');
						if (!ww[p.y+1][p.x-1][val])
							v.push_back(pp(p.y+1,p.x-1,val,p.s+'-'+a[p.y+1][p.x-1]));
					}
				}
				if (p.x < w-1){
					if (a[p.y+1][p.x] == '+' || a[p.y][p.x+1] == '+'){
						int val = p.val + a[p.y+1][p.x+1] - '0';
						if (!ww[p.y+1][p.x+1][val])
							v.push_back(pp(p.y+1,p.x+1,val,p.s+'+'+a[p.y+1][p.x+1]));
					}
					if (a[p.y+1][p.x] == '-' || a[p.y][p.x+1] == '-'){
						int val = p.val - (a[p.y+1][p.x+1] - '0');
						if (!ww[p.y+1][p.x+1][val])
							v.push_back(pp(p.y+1,p.x+1,val,p.s+'-'+a[p.y+1][p.x+1]));
					}
				}
			}
			if (p.x > 1){
				if (a[p.y][p.x-1] == '+'){
					int val = p.val + a[p.y][p.x-2] - '0';
					if (!ww[p.y][p.x-2][val])
						v.push_back(pp(p.y,p.x-2,val,p.s+'+'+a[p.y][p.x-2]));
				} else {
					int val = p.val - (a[p.y][p.x-2] - '0');
					if (!ww[p.y][p.x-2][val])
						v.push_back(pp(p.y,p.x-2,val,p.s+'-'+a[p.y][p.x-2]));
				}
			}
			if (p.x < w-2){
				if (a[p.y][p.x+1] == '+'){
					int val = p.val + a[p.y][p.x+2] - '0';
					if (!ww[p.y][p.x+2][val])
						v.push_back(pp(p.y,p.x+2,val,p.s+'+'+a[p.y][p.x+2]));
				} else {
					int val = p.val - (a[p.y][p.x+2] - '0');
					if (!ww[p.y][p.x+2][val])
						v.push_back(pp(p.y,p.x+2,val,p.s+'-'+a[p.y][p.x+2]));
				}
			}
			if (p.y > 1){
				if (a[p.y-1][p.x] == '+'){
					int val = p.val + a[p.y-2][p.x] - '0';
					if (!ww[p.y-2][p.x][val])
						v.push_back(pp(p.y-2,p.x,val,p.s+'+'+a[p.y-2][p.x]));
				} else {
					int val = p.val - (a[p.y-2][p.x] - '0');
					if (!ww[p.y-2][p.x][val])
						v.push_back(pp(p.y-2,p.x,val,p.s+'-'+a[p.y-2][p.x]));
				}
			}
			if (p.y < w-2){
				if (a[p.y+1][p.x] == '+'){
					int val = p.val + a[p.y+2][p.x] - '0';
					if (!ww[p.y+2][p.x][val])
						v.push_back(pp(p.y+2,p.x,val,p.s+'+'+a[p.y+2][p.x]));
				} else {
					int val = p.val - (a[p.y+2][p.x] - '0');
					if (!ww[p.y+2][p.x][val])
						v.push_back(pp(p.y+2,p.x,val,p.s+'-'+a[p.y+2][p.x]));
				}
			}
		}
	}
}

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		assert('+' < '-');
		int q; scanf("%d%d",&w,&q);
		gets(a[0]);
		for (int i = 0; i < w; i++)
			gets(a[i]);
		printf("Case #%d:\n",_+1);
		memset(was,0,sizeof(was));
		fill(res,res+maxn,string());
		vector<int> to;
		vector<int> ss;
		for (int i = 0; i < q; i++){
			int n; scanf("%d",&n);
			to.push_back(n);
			ss.push_back(n);
		}
		sort(ss.begin(),ss.end(),greater<int>());
		for (int i = 0; i < ss.size(); i++) if (!was[ss[i]]) work(ss[i]);
		for (int i = 0; i < to.size(); i++){
			int n = to[i];
			cout << res[n] << endl;
		}
	}
	return 0;
}
