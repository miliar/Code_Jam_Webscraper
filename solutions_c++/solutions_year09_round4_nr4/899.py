#include<iostream>
#include<math.h>

#define N 100

using namespace std;

struct point {
	int x,y,r;
};

point data[N];
int n;

void init(){
}

void input(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >>  data[i].x >> data[i].y >> data[i].r;
	}
}

double dist(int xx,int yy){
	return sqrt(double(data[xx].x - data[yy].x)*(data[xx].x - data[yy].x) + (data[xx].y - data[yy].y)*(data[xx].y - data[yy].y));
}

void process(){
	if (n==1) {
		cout << data[0].r <<endl;
		return;
	}
	if (n<=2) {
		cout << max(data[0].r,data[1].r)<<endl;
		return ;
	}
	double minn=-1;
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if (minn==-1 || minn > dist(i,j)+data[i].r+data[j].r) minn = dist(i,j)+data[i].r+data[j].r;
		}
	}
	cout << minn/2 <<endl;

}

void output(){
}

int main(){
	int t,i=0;
	cin >> t;
	while(t--){
		init();	
		input();
		i++;
		cout << "Case #"<<i<<": ";	
		process();
		
		output();			

	}

}


