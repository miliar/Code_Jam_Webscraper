#include<iostream>
#include<vector>
using namespace std;

bool intersect(int x1, int y1, int x2, int y2){
	if((x1 < x2 && y1 > y2) || (x1 > x2 && y1 < y2))
		return true;
	return false;
}

long long getIntersect(vector <int> x, vector <int> y){
	int sz = x.size();
	long long count=0;
	for(int i=0;i< sz; i++){
		for(int j=i+1; j< sz;j++){
			if(intersect(x[i],y[i],x[j],y[j]))
				count++;
		}
	}
	return count;
}

int main(){
	int T;
	cin >> T;
	for(int i=0;i< T;i++){
		int N, x, y;
		cin >> N;
		vector <int> X, Y;
		for(int j = 0 ;j < N; j++){
			cin >> x >> y;
			X.push_back(x);
			Y.push_back(y);
		}
		cout << "Case #" << i+1 << ": " << getIntersect(X,Y) << endl;
	}
	return 0;
}
