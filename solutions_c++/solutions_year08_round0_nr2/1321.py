#include <cstdio>
#include <algorithm>
using namespace std;
#include <vector>

pair<int, int> gettime(){
	char a,b;
	int h,m,r;
	scanf("%c%c", &a,&b);
	h = (a-'0')*10+b-'0';
	scanf("%c", &a);
	scanf("%c%c", &a,&b);
	m = (a-'0')*10+b-'0';
	r = h*60+m;
	scanf("%c", &a);
	scanf("%c%c", &a,&b);
	h = (a-'0')*10+b-'0';
	scanf("%c", &a);
	scanf("%c%c", &a,&b);
	m = (a-'0')*10+b-'0';
	h = h*60+m;
	scanf("\n");
	return make_pair(r,h);
}

vector<pair<int,int> > x;//0 - arrive at 1, 1 - arrive at 2, 2 - leave from 1, 3 - leave from 2

int main(){
	freopen("time.in", "rt", stdin);
	freopen("time.out", "wt", stdout);
	int T;
	scanf("%d\n", &T);
	for (int u = 1; u <= T; u++){
		int t,a,b;
		scanf("%d\n%d %d\n", &t, &a, &b);
		x.clear();
		for (int i = 0; i < a; i++){
			pair<int, int> tmp = gettime();
			tmp.second += t;
//			printf("%d %d\n", tmp.first, tmp.second);
			x.push_back(make_pair(tmp.first,2));
			x.push_back(make_pair(tmp.second,1));
		}
		for (int i = 0; i < b; i++){
			pair<int, int> tmp = gettime();
			tmp.second += t;
//			printf("%d %d\n", tmp.first, tmp.second);
			x.push_back(make_pair(tmp.first,3));
			x.push_back(make_pair(tmp.second,0));
		}
		sort(x.begin(),x.end());
		int dx = 0;
		int dy = 0;
		int rx = 0;
		int ry = 0;
		for (int i = 0; i < x.size(); i++){
//			printf("a: %d %d\n",x[i].first,x[i].second);
			if (x[i].second==0) dx++;
			if (x[i].second==1) dy++;
			if (x[i].second==2) dx--;
			if (x[i].second==3) dy--;
//			printf("dxy: %d %d\n", dx, dy);
			if (rx > dx) rx = dx;
			if (ry > dy) ry = dy;
		}
		printf("Case #%d: %d %d\n",u,-rx,-ry);
	}
	fclose(stdin);
	fclose(stdout);
}
