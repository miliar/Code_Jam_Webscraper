#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>

using namespace std;

#define sq(a) ((a)*(a))

struct plant{
	int x,y,r;
};

double dist(plant p1, plant p2){
	return sqrt( (double)sq(p1.x - p2.x) + sq(p1.y-p2.y));
}

int main(){
	int C, N;
	cin>> C;
	for(int c=1; c<=C; c++){
		cin >> N;
		vector< plant > p;
		for(int i=0; i<N; i++){
			plant p_;
			cin >> p_.x >> p_.y >> p_.r;
			p.push_back(p_);
		}

		double res=0.;
		if(N <=2 ){
			for(int i=0; i<N; i++)res=max(res,(double)p[i].r);
		}else{
			res=1000000;
			for(int i=0; i<N; i++)for(int j=0; j<N; j++)for(int k=0; k<N; k++){
				if(i==j || j==k || i==k)continue;
				res = min(res, max((double)p[i].r, .5*(p[j].r + p[k].r + dist(p[j],p[k]) )) );
			}
		}

		printf("Case #%d: %.6f\n", c, res);
	}
}
