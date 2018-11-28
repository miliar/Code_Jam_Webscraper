#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

struct Pair{int a; int b;};

int main(){
	int T = 0;
	cin>>T;
	for(int c = 0; c < T; c++){
		int N = 0, intersections = 0;
		cin>>N;
		vector<Pair> v;
		for(int i = 0; i < N; i++){
			int first = 0, second = 0;
			cin>>first>>second;
			Pair p;
			p.a = first;
			p.b = second;
			v.push_back(p);
		}

		// once all points are collected, run brute force to check for intersection of two lines

		for(int i = 0; i < int(v.size()); i++){
			for(int j = i + 1; j < int(v.size()); j++){
				bool cond1 = v[j].a > v[i].a && v[j].b < v[i].b;
				bool cond2 = v[j].a < v[i].a && v[j].b > v[i].b;
				if(cond1 || cond2){
					intersections++;
				}
			}
		}
		cout<<"Case #"<<c + 1<<": "<<intersections<<endl;
	}
	return 0;
}
