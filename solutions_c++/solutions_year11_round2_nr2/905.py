#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;
int c,d;
vector<pair<int,int> > pos;
bool check(double x){
	double bef=pos[0].F-x;
	FOR(i,0,pos.size()){
		bef=max(pos[i].F-x,bef);
		bef+=d*pos[i].S;
		if(bef>pos[i].F+x+d)return false;
	}
	return true;
}
int main(){
	int packs;
	scanf("%d",&packs);
	FORQ(lololol,1,packs){
		scanf("%d%d",&c,&d);
		FOR(i,0,c){
			int x,y;
			scanf("%d%d",&x,&y);pos.PB(MP(x,y));
		}
		sort(pos.begin(),pos.end());
		double p=0,q=10000000000000.0;
		while(q-p>0.00000001){
			double s = (p+q)/2.0;
			if(check(s))q=s;
			else p=s;
		}
		printf("Case #%d: %Lf\n",lololol,(p+q)/2.0);
		pos.clear();
	}
	return 0;
}