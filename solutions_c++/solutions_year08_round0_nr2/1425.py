#include <vector>
#include <string>
#include <iostream>
#include <stdio.h>
#define min(a,b) (a<b) ? a:b

struct interval {
	int s;
	int e;
};

using namespace std;
int T,NA,NB,i,j,N,h,m,r[2],t,startfrom;
vector<interval> trip[2];
interval tmp;
vector<interval>::iterator index[2];

vector<interval>::iterator min_start(int index) {
	int min=1439;
	vector<interval>::iterator ret, k;
	ret=trip[index].end();
	for(k=trip[index].begin();k!=trip[index].end();k++) {
		if(k->s < min) {
			min = k->s;
			ret = k;
		}
	}
	return ret;
}

vector<interval>::iterator find_near(int time,int whattrip) {
	int min=1439;
	vector<interval>::iterator ret, k;
	ret=trip[whattrip].end();
	for(k=trip[whattrip].begin();k!=trip[whattrip].end();k++) {
		if((k->s >= time) && (k->s - time < min)) {
			min = k->s - time;
			ret=k;
		}
	}
	return ret;
}


int main() {
	freopen("input.in","r",stdin);
	freopen("input.out","w",stdout);
	cin >> N;
	
	for(i=0;i<N;i++) {
		cin >> T;
		cin >> NA >> NB;
		for(j=0;j<2;j++) {
			trip[j].clear();
			r[j]=0;
		}
		for(j=0;j<NA;j++) {
			scanf("%d:%d",&h,&m);
			tmp.s = h*60 + m;
			scanf("%d:%d",&h,&m);
			tmp.e = h*60 + m;
			trip[0].push_back(tmp);
		}
		for(j=0;j<NB;j++) {
			scanf("%d:%d",&h,&m);
			tmp.s = h*60 + m;
			scanf("%d:%d",&h,&m);
			tmp.e = h*60 + m;
			trip[1].push_back(tmp);
		}
		
		while(!(trip[0].empty() && trip[1].empty())) {
			for(j=0;j<2;j++) index[j] = min_start(j);
			if(index[0] == trip[0].end()) {
				startfrom = 1;
			}
			else if(index[1] == trip[1].end()) {
				startfrom = 0;
			}
			else {
				startfrom = (index[0]->s < index[1]->s) ? 0 : 1 ;
			}
			r[startfrom]++;
			while(true) {
				t = index[startfrom]->e + T;
				trip[startfrom].erase(index[startfrom]);
				startfrom = (startfrom == 1) ? 0: 1;
				index[startfrom] = find_near(t, startfrom);
				if(index[startfrom] == trip[startfrom].end()) break;
			}
		}
		cout<< "Case #"<<(i+1)<<": "<<r[0]<<" "<<r[1]<<endl;
	}
	return 0;
}
