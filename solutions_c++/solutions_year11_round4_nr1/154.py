#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


struct walk{
	int B,E;
	int w;
	bool friend operator <(const walk& p1,const walk& p2){
		return p1.B < p2.B;
	}
};
int R,W,X,n;
double tot;
vector<walk>ws;

double calcP(const walk& p){
	return 1.0 / ((p.w + R) * (p.w + W));
}

bool xcmp(const walk& p1,const walk& p2){
	return calcP(p1) - calcP(p2) > 1e-9;
}

void work(){
	sort(ws.begin(),ws.end());
	vector<walk>nextWs;
	walk next;
	if(ws[0].B > 0){
		next.B = 0;
		next.E = ws[0].B;
		next.w = 0;
		nextWs.push_back(next);
	}
	for(int i = 0;i<ws.size();i++){
		if(i<ws.size() - 1){
			if(ws[i].E < X && ws[i + 1].B > ws[i].E){
				next.B = ws[i].E;
				next.E = ws[i + 1].B;
				next.w = 0;
				nextWs.push_back(next);
			}		
		}else{
			if(ws[i].E < X){
				next.B = ws[i].E;
				next.E = X;
				next.w = 0;
				nextWs.push_back(next);
			}		
		}
	}
	for(int i = 0;i<nextWs.size();i++)
		ws.push_back(nextWs[i]);
	sort(ws.begin(),ws.end(),xcmp);
	/*for(int i = 0;i<ws.size();i++){
		printf("%d %d %d\n",ws[i].B,ws[i].E,ws[i].w);
	}*/
	double cost = 0.0;
	int pt;
	for(pt = 0;pt<ws.size() && tot>1e-9;pt++){
		double S = ws[pt].E - ws[pt].B,tt;
		if(S / (R + ws[pt].w) > tot){
			cost += tot + (S - tot * (R + ws[pt].w)) / (W + ws[pt].w);
			tot = 0.0;
			pt++;
			break;	
		}else{
			tt = S / (R + ws[pt].w);
			tot -= tt;
			cost += tt;
		}
	}
	for(;pt < ws.size();pt++){
		double S = ws[pt].E - ws[pt].B;
		cost += S / (W + ws[pt].w);
	}
	printf(" %lf\n",cost);
}

int main(){
	int tc;
	scanf("%d",&tc);
	for(int tt=1 ;tt<=tc;tt++){
		printf("Case #%d:",tt);
		scanf("%d%d%d%lf%d",&X,&W,&R,&tot,&n);
		ws.clear();
		for(int i = 0;i<n;i++){
			int b,e,w;
			scanf("%d%d%d",&b,&e,&w);
			walk temp;
			temp.B = b;
			temp.E = e;
			temp.w = w;
			ws.push_back(temp);
		}
		work();
	}
	return 0;
}
