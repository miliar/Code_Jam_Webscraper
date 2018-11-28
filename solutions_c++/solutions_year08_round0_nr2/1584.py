#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int N;

class connection {
	public:
	connection() {}
	connection(int a,int b,int c,int d):h1(a),m1(b),h2(c),m2(d) {}
	int h1,m1,h2,m2;
};

bool operator<(connection a,connection b) {
	if( a.h1 == b.h1 ) return a.m1<b.m1;
	return a.h1<b.h1;
}

bool check(int h1,int m1,int h2,int m2,int t) {
	m1 += t;
	if( m1 >= 60 ) m1-=60,h1++;
	if(h2>h1) return true;
	if(h2==h1 && m2>=m1) return true;
	return false;
}

int main() {
	cin >> N;
	for(int num=0;num<N;num++) {
		vector<connection> a,b;
		int t,na,nb,reta(0),retb(0);
		cin >> t >> na >> nb;
		//printf("%d\n",t);
		cin.ignore(100,'\n');
		for(int j=0;j<na;j++) {
			string tmp;
			getline( cin, tmp );
			for(int x=0;x<tmp.size();x++) if(tmp[x]==':') tmp[x]=' ';
			istringstream icc(tmp);
			connection c;
			icc >> c.h1 >> c.m1 >> c.h2 >> c.m2;
			a.push_back( c );
		}
		for(int j=0;j<nb;j++) {
			string tmp;
			getline( cin, tmp );
			for(int x=0;x<tmp.size();x++) if(tmp[x]==':') tmp[x]=' ';
			istringstream icc(tmp);
			connection c;
			icc >> c.h1 >> c.m1 >> c.h2 >> c.m2;
			b.push_back( c );
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		
		while( a.size() && b.size() ) {
			int pa(0),pb(0);
			vector<int> ca,cb;
			bool cur;
			if( a[0] < b[0] ) cur=true,reta++; else cur=false,retb++;
			//printf("cur=%d\n",cur);
			while(true) {
				bool ok(false);
				if(cur) {//A
					ca.push_back(pa);
					for(;pb<b.size();pb++) {
						if(check(a[pa].h2,a[pa].m2,b[pb].h1,b[pb].m1,t)) { ok=true; break; }
					}
				} else { //B
					cb.push_back(pb);
					for(;pa<a.size();pa++) {
						if(check(b[pb].h2,b[pb].m2,a[pa].h1,a[pa].m1,t)) { ok=true; break; }
					}
				}
				if(!ok) break;
				cur = !cur;
			}
			for(int i=0;i<ca.size();i++) a.erase(a.begin()+ca[i]-i);
			for(int i=0;i<cb.size();i++) b.erase(b.begin()+cb[i]-i);
		}
		
		if(!a.empty()) reta+=a.size();
		if(!b.empty()) retb+=b.size();
		
		printf("Case #%d: %d %d\n",num+1,reta,retb);
	}
	return 0;
}
