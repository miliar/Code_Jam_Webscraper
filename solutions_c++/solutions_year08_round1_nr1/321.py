#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>

#define Rep(i, a, b) for(long long i = (a); i < (b); i++)
using namespace std;


long long dot(vector<long long>x, vector<long long>y, long long n){
	long long sum = 0;
	Rep(i, 0, n){
		sum += x[i]*y[i];
	}
	return sum;
}

bool fn(long long i, long long j){
	return i > j;
}

int main(){
	vector<long long>x;
	vector<long long>y;
	long long N, n, temp;
	cin >> N;
	Rep(I, 0, N){
		cout <<"Case #"<<I+1<<": ";
		cin >> n;
		x.clear();
		y.clear();
		Rep(i, 0, n){
			cin>>temp;
			x.push_back(temp);
		}

		Rep(i, 0, n){
			cin>>temp;
			y.push_back(temp);
		}
		sort(x.begin(), x.end());
		sort(y.begin(), y.end(), fn);
		bool flag = true;
		long long min = 0;
		do{
			temp = dot(x,y,n);
			if(temp < min || flag){
				flag = false;
				min = temp;
			}
		}while(next_permutation(y.begin(), y.end()));
		cout<<min<<endl;
	}
	return 0;
}
