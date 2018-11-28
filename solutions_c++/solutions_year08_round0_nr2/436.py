#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
using namespace std;

#define forV(va,ve) for(int va=0;va < ve.size();++va)
#define V(t) vector< t >
#define Vall(t) t.begin(),t.end()
#define MP make_pair
vector<string> es;
vector<string> q;

int memo[1000][1000];

int dp(int at,int se)
{
	if(at == q.size()){return 0;}
	int &ret = memo[at][se];
	if(ret != -1){return ret;}
	if(q[at] == es[se]){return 100000;}
	ret = 1000000;
	for(int i=0;i<es.size();++i)
	{
		ret <?= dp(at+1,i) + ((i == se)?(0):(1));
	}
	return ret;
}

vector<pair<pair<int,int>,int> > events;
vector<pair<pair<int,int>,int> > v;
pair<int,int> proc(string x,int inc=0)
{
	pair<int,int> p;
	sscanf(x.c_str(),"%d:%d",&p.first,&p.second);
	p.second += inc;
	while(p.second >= 60){p.second -= 60;++p.first;}
	return p;
}

int main(void)
{
	int N;
	cin >> N;
	for(int cn=1;cn <= N;++cn)
	{
		string ss;
		events.clear();
		int T;
		cin >> T;
		int NA,NB;
		cin >> NA >> NB;
		for(int i=0;i<NA;++i)
		{
			string a,b;
			cin >> a >> b;
			events.push_back(MP(proc(a),0));
			events.push_back(MP(proc(b,T),-1));

		}
		for(int i=0;i<NB;++i)
		{
			string a,b;
			cin >> a >> b;
			events.push_back(MP(proc(a),2));
			events.push_back(MP(proc(b,T),-3));
		}
		v.assign(events.begin(),events.end());
		sort(v.begin(),v.end());
		int a,b,ansa,ansb;
		for(a=0;;++a)
		{
			bool win = false;
			for(b=0;b<1000;++b)
			{
				bool bwin = true;
				int ia = a,ib = b;
			//	cerr << endl;
				forV(i,v)
				{
					//simulate
					int ev = v[i].second;
				//	cerr << ev << " " << ia << " " << ib << endl;
					switch(ev)
					{
						case(0):
							//a leave
							if(ia == 0){bwin = false;}
							else{--ia;}
							break;
						case(-1):
							++ib;
							break;
						case(2):
							if(ib == 0){bwin = false;}
							else{--ib;}
							break;
						case(-3):
							++ia;
							break;
					};
					if(bwin == false){break;}

				}
				if(bwin){win = true;break;}
			}
			if(win){break;}
		}
		ansa = a;
		for(b=0;;++b)
		{
			bool win = false;
			for(a=0;a<1000;++a)
			{
				bool bwin = true;
				int ia = a,ib = b;
			//	cerr << endl;
				forV(i,v)
				{
					//simulate
					int ev = v[i].second;
				//	cerr << ev << " " << ia << " " << ib << endl;
					switch(ev)
					{
						case(0):
							//a leave
							if(ia == 0){bwin = false;}
							else{--ia;}
							break;
						case(-1):
							++ib;
							break;
						case(2):
							if(ib == 0){bwin = false;}
							else{--ib;}
							break;
						case(-3):
							++ia;
							break;
					};
					if(bwin == false){break;}

				}
				if(bwin){win = true;break;}
			}
			if(win){break;}
		}

		cout << "Case #" << cn << ": " << ansa << " " << b << endl;
	}
	return 0;
}
