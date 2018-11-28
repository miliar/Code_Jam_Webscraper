#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef struct _node{
	int stime;
	int dtime;
	int d; // 1.goto b 2. goto a
	int time;
	int type; // 1.go  2. turn
}node;

class comp {
	public:
        bool operator()(const node &l,const node &r)
        {
			if(l.time == r.time)
				return l.type < r.type;
            else return l.time > r.time;
        }
};
int returntime(int h,int m)
{
	return h*60+m;
}
int main()
{
	int n;
	int aviable_a,aviable_b;
	int t;
	int ka=1;
	cin >>t;
	while(t--){
		int turn;
		int na,nb;
		cin >> turn;
		priority_queue<node,vector<node>,comp> q;

		int sh,sm,dh,dm;
		int a,b,i;
		aviable_a = aviable_b = 0;
		node ss;
		na = nb = 0;
		
		cin >>a >>b;

		for(i=0;i<a;i++){
			scanf("%02d:%02d %02d:%02d",&sh,&sm,&dh,&dm);
			ss.stime = returntime(sh,sm);
			ss.dtime = returntime(dh,dm);
			ss.time = ss.stime;
			ss.type = 1;
			ss.d = 1;
			q.push(ss);
		}
		for(i=0;i<b;i++){
			scanf("%02d:%02d %02d:%02d",&sh,&sm,&dh,&dm);
			ss.stime = returntime(sh,sm);
			ss.dtime = returntime(dh,dm);
			ss.time = ss.stime;
			ss.type = 1;
			ss.d = 2;
			q.push(ss);
		}

		while(!q.empty()){
			node aa = q.top();
			q.pop();
			if(aa.type == 1){
				if(aa.d == 1){
					if(aviable_a ==0)
						na++;
					else aviable_a--;
					aa.time = aa.dtime+turn;
					aa.d = 1;
					aa.type = 2;
					q.push(aa);
				}
				else {
					if(aviable_b ==0)
						nb++;
					else aviable_b--;

					aa.time = aa.dtime+turn;
					aa.d = 2;
					aa.type = 2;
					q.push(aa);
				}
			}else if(aa.type == 2){
				if(aa.d == 1){
					aviable_b++;
				}
				else{
				   	aviable_a++;
				}
			}
		}
		cout <<"Case #"<<ka++<<": "<< na<<' '<<nb<<endl;
	}
	return 0;
}
