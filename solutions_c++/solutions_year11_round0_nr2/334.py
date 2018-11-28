#include <iostream>
#include <string>
#include <list>

using namespace std;

struct combine{
public:
	bool set;
	string pair;
	string newm;
};

struct oppose{
	bool set;
	string pair;
	int charged;
};

struct combine c[26];
struct oppose d[26];

int main(){
	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		int C;
		cin>>C;

		for (int j=0;j<26;j++){
			c[j].set=false;
			c[j].pair="";
			c[j].newm="";
			d[j].set=false;
			d[j].pair="";
			d[j].charged=0;
		}


		for (int j=0;j<C;j++){
			char c1,c2,cn;
			cin>>c1>>c2>>cn;
			c[c1-'A'].set=true;
			c[c1-'A'].pair+=c2;
			c[c1-'A'].newm+=cn;
			c[c2-'A'].set=true;
			c[c2-'A'].pair+=c1;
			c[c2-'A'].newm+=cn;
		}

		int D;
		cin>>D;

		for (int j=0;j<D;j++){
			char d1,d2;
			cin>>d1>>d2;
			d[d1-'A'].set=true;
			d[d1-'A'].pair+=d2;
			d[d2-'A'].set=true;
			d[d2-'A'].pair+=d1;
		}

		int N;
		cin>>N;

		list<char> mlist;

		char m;
		cin>>m;
		mlist.push_back(m);
		if (d[m-'A'].set) d[m-'A'].charged++;

		list<char> elist;
		for (int j=1;j<N;j++){
			cin>>m;
			elist.push_back(m);
		}

		while(!elist.empty()){
			m=elist.front();
			elist.pop_front();
			if (!mlist.empty()){
				if (c[m-'A'].set){
					string::size_type pos=c[m-'A'].pair.find(mlist.back());
					if (pos!=string::npos){
						m=c[m-'A'].newm[pos];
						elist.push_front(m);
						m=mlist.back();
						mlist.pop_back();
						if (d[m-'A'].charged!=0) d[m-'A'].charged--;
						continue;
					}
				}
				if (d[m-'A'].set){
					bool clear=false;
					for (string::iterator it=d[m-'A'].pair.begin();it!=d[m-'A'].pair.end();it++){
						char cm=*it;
						if (d[cm-'A'].charged!=0) {
							clear=true;
							break;
						}
					}
					if (clear){
						mlist.clear();
						for (int j=0;j<26;j++){
							d[j].charged=0;
						}
						continue;
					}
				}
			}
			mlist.push_back(m);
			if (d[m-'A'].set) d[m-'A'].charged++;
		};

		cout<<"Case #"<<i+1<<": [";
		while(!mlist.empty()){
			cout<<mlist.front();
			mlist.pop_front();
			if(!mlist.empty()) cout<<", ";
		}
		cout<<"]"<<endl;
	}

	return 0;
}
