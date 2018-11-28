#include <cstdio>
#include <fstream>
#include <queue>
#include<functional>
using namespace std;
struct time{
		int stime, endtime;
};
int  ta, tb;
bool operator > (const struct time &t1, const struct time &t2)
{
    return t1.stime > t2.stime;
}
struct cmp{
       bool operator ()(const int &i,const int &j){
            return i>j;
         }
};
priority_queue<struct time, vector<struct time>, greater<struct time> > atime, btime;
priority_queue< int ,vector<int>,cmp >a, b;
void Change(int & t,int  tm)
{
	
	t = (t / 100 + (t % 100 + tm) / 60)* 100 + (t % 100 + tm) % 60;
}
void Solve(int na, int nb,  int tm)
{
	struct time t1;
	struct time t2;
	while(!(atime.empty() && btime.empty())){//时刻表里atime，btime有一个非空
		if(!atime.empty()) t1 = atime.top();//取得atime最小时刻
		else t1.stime = 0xffff;
		if(!btime.empty()) t2 = btime.top(); //取得btime最小时刻
		else t2.stime = 0xffff;
		if(t1.stime < t2.stime){//如果atime小
			atime.pop();
			if(!a.empty() && a.top() <= t1.stime){a.pop(); Change(t1.endtime, tm); b.push(t1.endtime);}//查找优先队列里有没有到达时刻比atime中早的，如果有，endtime变一下，放在对方优先队列
			else{ ta++; Change(t1.endtime, tm); b.push(t1.endtime);}//如果没有，新建一个，改变最末时刻，ta++，并放到对方优先队列
		}
		else{//如果btime小
			btime.pop();
			if(!b.empty() && b.top() <= t2.stime){b.pop(); Change(t2.endtime, tm); a.push(t2.endtime);}
			else{tb++;Change(t2.endtime, tm); a.push(t2.endtime);}
		}
	}
	while(!a.empty())a.pop();
	while(!b.empty())b.pop();
}

int main()
{
	int n, na, nb, tm, a, b, c, d, e;
	char ch;
	ifstream in("B-small-attempt3.in");
	ofstream out("b.out");
	in >> n;
	
	for(int k = 1; k <= n; k++){
		ta = 0; tb = 0;
		in >> tm>> na >> nb;
		for(int i = 0; i < na; i++){
			in >> a >>ch>> b>> c >>ch>> d ;
			a = a * 100 + b; c = c * 100 + d;
			struct time t;
			//cout << a << ' '<< c<<endl;
			t.stime = a; 
			t.endtime = c;
			atime.push(t);
			//cout << atime.top().stime;
		}
		for(int i = 0; i < nb; i++){
			in >> a >>ch>> b>> c >>ch>> d ;
			a = a * 100 + b; c = c * 100 + d;
			//cout << a << ' '<< c<<endl;
			struct time t;
			t.stime = a; t.endtime = c;
			btime.push(t);
		}
		Solve(na, nb, tm);
		out << "Case #" << k << ": " << ta << ' ' << tb << endl;
		
	}
	return 0;
}
