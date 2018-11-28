#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <algorithm>
#include <fstream>
#include <math.h>

using namespace std;

string itoa(int val) {stringstream ss;ss << val;return ss.str();}
typedef vector<int> vi;
typedef pair<int,int> pi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define ll long long

int n,m,A;

int area(int x1,int y1,int x2,int y2,int x3,int y3) {
	int a2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
	int b2 = (x3-x2)*(x3-x2) + (y3-y2)*(y3-y2);
	int c2 = (x3-x1)*(x3-x1) + (y3-y1)*(y3-y1);
	ll p1 = a2+b2+c2;
	p1 = p1*p1;
	ll p2 = (a2*a2+b2*b2+c2*c2)*2;
	ll s = sqrt(p1 - p2);
	return s/2;
}

void calc() {
	int x1 = 0;
	int y1 = 0;
//	for(int x1=0;x1<=n;x1++) {
//		for(int y1=0;y1<=m;y1++) {
			for(int x2=0;x2<=n;x2++) {
				for(int y2=0;y2<=m;y2++) {
					//if (x1==x2 && y1==y2) continue;
					for(int x3=0;x3<=n;x3++) {
						for(int y3=0;y3<=m;y3++) {
							//if (x2==x3 && y2==y3) continue;
							//if (x1==x3 && y1==y3) continue;
							int a = area(0,0,x2,y2,x3,y3);
							if (a==A) {
								cout << 0 << " " << 0 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
								return;
							}
						}
					}
				}
			}
//		}
//	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int testcases;
	cin >> testcases;
	for(int i=1;i<=testcases;i++) {
		cin >> n >> m >> A;
		cout << "Case #" << i << ": ";
		calc();
	}
	return 0;
}
