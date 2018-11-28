#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <set>
#include <queue>
using namespace std;

int main() {
	freopen("hz.in","r",stdin);
	freopen("hz666.out","w",stdout);
	__int64 t,n,k,r;
	cin >> t;
	for (int i=0;i<t;i++) {
		scanf("%I64d %I64d %I64d",&r,&k,&n); 
		__int64 hz,all=0;
		queue<int> q;
		vector <queue<int> > w;
		vector <__int64> v;
		set <queue<int> > s;
		for (int j=0;j<n;j++) {
			scanf("%d",&hz);
			q.push(hz);
		}
		while (s.find(q)==s.end()) {
			hz=0;
			s.insert(q);
			w.push_back(q);
		//	cout << ""
			__int64 a=0;
		//	cout << "!";
			queue<int> qq=q;
		/*	while(qq.size()) {
				cout << qq.front();
				qq.pop();
			} cout << endl;*/
			while (hz<n) {
				int f=q.front();
				if (a+f<=k) {
					a+=f; 
					//cout << a << " ";
				} else break;
				q.pop();
				q.push(f);
				hz++;
			}
		//	cout << endl;
			v.push_back(a);
		//	cout << "+";
			all+=a;
		}
		hz=0;
		int pre=0;
		while (w[hz]!=q) {
			pre+=v[hz];
			hz++;
		}
		/*if (hz) {
			hz--;
			pre-=v[hz];
		}*/
	//	cout << "PRE RESULT" << v.size() <<" " << all << "\n";
		__int64 res=0,vs=v.size()-hz;
		res+=pre;
		all-=pre;
		r-=hz;
		res+=all*(r/vs);
		int rb=r-(r/vs)*vs;
		for (int j=hz;j<hz+rb;j++) res+=v[j];
		printf("Case #%d: ",i+1); cout << res << endl;
int zzzz;
	}
}