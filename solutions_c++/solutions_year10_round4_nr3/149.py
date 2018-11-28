#include<algorithm>
#include<iostream>
#include<vector>
#include<cstdio>
#include<set>
using  namespace std;
typedef pair<int,int> P;
#define x first
#define y second

vector<P> next(vector<P>& a, set<P>& s){
	vector<P> sig;
	int n = a.size();
	for(int i = 0; i < n; i++){
		if(s.count(P(a[i].x, a[i].y - 1)) + s.count(P(a[i].x - 1, a[i].y)) != 0)
			sig.push_back(a[i]);
	}
	multiset<P> nace;
	
	for(int i = 0; i < n; i++){ 
		if(s.count(P(a[i].x + 1, a[i].y)) == 0)
			nace.insert(P(a[i].x + 1, a[i].y));
		if(s.count(P(a[i].x, a[i].y + 1)) == 0)
			nace.insert(P(a[i].x, a[i].y + 1));
	}
	set<P> mete;
	for(multiset<P>::iterator it = nace.begin(); it != nace.end(); it++){
		if(nace.count(*it) == 2) mete.insert(*it);
	}
	sig.insert(sig.end(), mete.begin(), mete.end());
	return sig;
}

int main(){
	int c; cin >> c;
	for(int ca = 1; ca <= c; ca++){
		int r; cin >> r;
		vector<P> a;
		for(int i = 0; i < r; i++){
	        	int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int xx = min(x1, x2); xx <= max(x1, x2); xx++)
				for(int yy = min(y1, y2); yy <= max(y1, y2); yy++)
					a.push_back(make_pair(xx, yy));
		}
		sort(a.begin(), a.end());
		a.erase(unique(a.begin(), a.end()), a.end());
		set<P> s(a.begin(), a.end());
		int t;
		for(t = 0;  ; t++){
			if(a.empty()) break;
			a = next(a, s);
			s = set<P>(a.begin(), a.end());
		}
		cout << "Case #" << ca << ": " << t << endl;
		
	}	
}
