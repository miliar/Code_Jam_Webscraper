#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

const double eps=1e-6;

struct seg {
	int length;
	int speed;
	bool operator<(const seg& q) const {
		return speed<q.speed;
	}
};

int D,W,R,t; vector<seg> db;

double solve() {
	double remain=t,morelength;
	int i; double ret=0,tmp;
	for(i=0;i<db.size();i++) {
		morelength=db[i].length;
		if(remain>eps) {
			tmp=morelength/(db[i].speed+R);
			if(tmp>remain)tmp=remain;
			remain-=tmp;
			morelength-=tmp*(db[i].speed+R);
			ret+=tmp;
		}
		if(morelength>eps) {
			ret+=morelength/db[i].speed;
		}
	}
	return ret;
}

void input() {
	int n,b,e,s,now; seg tmp;
	scanf("%d%d%d%d%d",&D,&W,&R,&t,&n);
	R-=W;
	now=0;
	while(n--) {
		scanf("%d%d%d",&b,&e,&s);
		if(now!=b) {
			tmp=(seg){b-now,W};
			db.push_back(tmp);
		}
		tmp=(seg){e-b,s+W};
		db.push_back(tmp);
		now=e;
	}
	if(now!=D) {
		tmp=(seg){D-now,W};
		db.push_back(tmp);
	}
	sort(db.begin(),db.end());
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d: %.8f\n",S,solve());
		db.clear();
	}
	return 0;
}
