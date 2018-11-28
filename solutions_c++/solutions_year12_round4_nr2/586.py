#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<sstream>
#include<fstream>

typedef long long ll;

using namespace std;

struct Person{
	int r;
	int x;
	int y;
};

int n, w, l;
vector<int> radii;
vector<Person> peeps;

int min(int a, int b){ return a < b ? a : b; }
int max(int a, int b){ return a > b ? a : b; }
int abs(int a) {return a > 0 ? a : -a; }

void initSetup(){
	int x = 0;
	int y = 0;
	int nextY = 0;
	for(int i = 0; i < radii.size(); ++i){
		int px = x == 0 ? x : x + radii[i];
		int py = y == 0 ? y : y + radii[i];
		if(px > w){
			x = 0;
			y = nextY;
			px = 0;
			py = y + radii[i];
		}
		if(py > l){
			x = 0;
			y = 0;
			nextY = 0;
			px = 0;
			py = 0;
		}
		Person p = {radii[i], px, py};
		peeps.push_back(p);
		//fprintf(stderr, "%d: %d %d %d\n", i, radii[i], px, py);

		if(x == 0) x-= radii[i];
		x += 2 * radii[i];
		if(py + radii[i] > nextY) nextY = py + radii[i];
	}
}

int dist(Person p1, Person p2){
	int dx = p1.x - p2.x;
	int dy = p1.y - p2.y;
	return dx * dx + dy * dy;
}

string makeString(){
	stringstream ss;
	for(int i = 0; i < peeps.size(); ++i){
		ss << peeps[i].x << " " << peeps[i].y << " ";
	}
	string s;
	getline(ss, s);
	return s;
}

string genArr(){
	initSetup();
	return makeString();
}

int main(){
	int T;
	scanf("%d\n", &T);
	ofstream of("blg.out");
	for(int q = 1; q <= T; q++){
		cin >> n >> w >> l;
		for(int i = 0; i < n; i++){
			int r;
			cin >> r;
			radii.push_back(r);
		}
		printf("Case #%d: %s\n", q, genArr().c_str()); 
		of << "Case #" << q << ": " << makeString() << endl;
		radii.clear();
		peeps.clear();
		cerr << q << endl;
	}
}
