#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<queue>

typedef long long ll;

using namespace std;

struct Vine{
	int d;
	int l;
	int i;
	int reach;
};

int min(int a, int b){ return a < b ? a : b; }

/*bool canReach(vector<Vine> vines, int dtot){
	int ind = 0;
	Vine cv = vines[ind];
	int reach = cv.d;
	while(cv.d + reach < dtot){
		int bestVine = -1;
		int bestReach = -1;
		int bestDisp = -1;
		for(int i = ind+1; i < vines.size(); ++i){
			int dd = vines[i].d - cv.d;
			if(dd > reach) break;
			int thisReach = min(dd, vines[i].l);
			if(thisReach + dd > bestDisp){
				bestVine = i;
				bestReach = thisReach;
				bestDisp = thisReach + dd;
			}
		}
		if(bestVine == -1) return false;
		ind = bestVine;
		cv = vines[bestVine];
		reach = bestReach;
	}
	return true;
}*/

bool canReach(vector<Vine> & vines, int dtot, Vine cv) {
	queue<Vine> q;
	q.push(cv);
	while(!q.empty()){
		Vine v = q.front();
		q.pop();
		if(v.d + v.reach >= dtot) return true;
		for(int i = v.i+1; i < vines.size(); ++i){
			int dd = vines[i].d - v.d;
			if(dd > v.reach) break;
			Vine nv = vines[i];
			nv.reach = min(dd, vines[i].l);
			q.push(nv);
		}
	}
	return false;
}

int main(){
	int T;
	scanf("%d\n", &T);
	for(int q = 1; q <= T; q++){
		int n;
		cin >> n;
		vector<Vine> vines;
		for(int i = 0; i < n; i++){
			int d, l;
			cin >> d >> l;
			Vine v = {d, l, i, -1};
			vines.push_back(v);
		}
		int dtot;
		cin >> dtot;
		vines[0].reach = vines[0].d;
		printf("Case #%d: %s\n", q, 
			canReach(vines, dtot, vines[0]) ? "YES" : "NO");
	}
}
