#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;


int calc(int st, int ed, vector<int> &q, int s)
{

	double a = (ed-st)/2.0+st;
	//cout << a << endl;
	int min=ed,minn=-1,minn2=-1;
	int t=s;
	if (st==ed) return 0;
	int b=999999999;
	while(q[t]<=ed) {
		int c=calc(st,q[t]-1,q,s) + calc(q[t]+1,ed,q,t+1);
		if (c<b) {
			b=c;
		}

		t++;
	}
	if (b==999999999) return 0;
	//cout << st << "," << ed << endl;
	//cout << q[minn] << " ";
	
	b+=ed-st;
	

	return b;
}

int calc2(int st, int ed, vector<int> &q, int s)
{

	double a = (ed-st)/2.0+st;
	//cout << a << endl;
	int min=ed,minn=-1,minn2=-1;
	int t=s;
	if (st==ed) return 0;
	while(q[t]<=ed) {
		if (abs(a-q[t])<min) {
			min=abs(a-q[t]);
			minn=t;
		} else {
			if (abs(a-q[t])==min)
				minn2=t;
			break;
		}
		t++;
	}
	//cout << st << "," << ed << endl;
	if (minn<0) return 0;
	//cout << q[minn] << " ";
	
	int b=ed-st;
	
	b+=calc(st,q[minn]-1,q,s);
	b+=calc(q[minn]+1,ed,q,minn+1);

	if (minn2>=0) {
		//cout << "OK" << endl;
		int c=ed-st;
		c+=calc(st,q[minn]-1,q,s);
		c+=calc(q[minn]+1,ed,q,minn+1);
		if (c<b) b=c;
	}

	return b;
}


int main()
{
	int N,P,Q,n;
	cin >> N;
	string s;

	for (int i=0;i<N;i++) {
		cin >> P >> Q;
		vector<int> q;

		for (int j=0;j<Q;j++) {
			cin >> n;
			q.push_back(n);
		}
		q.push_back(P+1);

		int a=calc(1,P,q,0);


		cout << "Case #" << i+1 << ": "<< a << endl;
	}

	return 0;
}

