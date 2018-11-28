#include <iostream>
#include <vector>
#include <map>
#include <functional>
#include <algorithm>
#include <iterator>

using namespace std;

struct rect {
	int x1,y1,x2,y2;
};

int main() {
	int N_CASES;
	cin >> N_CASES;
	for(int CASE=1;CASE<=N_CASES;CASE++) {
		int R;
		cin >> R;
		vector<rect> rs(R);
		for(int i=0;i<R;i++)
			cin >> rs[i].x1 >>rs[i].y1 >>rs[i].x2 >>rs[i].y2;
		
		vector<bool> m1(101*101,false),m2(101*101,false);
		for(int i=0;i<R;i++)
			for(int y=rs[i].y1;y<=rs[i].y2;y++)
				for(int x=rs[i].x1;x<=rs[i].x2;x++)
					m1[y*101+x]=true;
		bool h=true;
		int t;
		for(t=0;h;t++) {
			#if false
			for(int y=0;y<6;y++) {
				for(int x=0;x<6;x++)
					cerr << m1[101*y+x];
				cerr << endl;
			}
			cerr << endl;
			#endif
			
			h=false;
			for(int i=0;i<101;i++) {
				m2[101*i]=false;
				m2[i]=false;
			}
			for(int y=1;y<101;y++)
				for(int x=1;x<101;x++) {
					m2[101*y+x]=(m1[101*(y-1)+x] & m1[101*y+(x-1)])
						| (m1[101*(y-1)+x] & m1[101*y+x])
						| (m1[101*y+x] & m1[101*y+(x-1)]);
					h|=m2[101*y+x];
				}
			swap(m1,m2);		
		}
		cout << "Case #" << CASE << ": " << t << endl;
	}
}