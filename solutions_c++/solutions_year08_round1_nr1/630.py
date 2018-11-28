#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;
#define x first.first
#define y second
#define INF 1000000

vector<int> v1,v2;
int i,o,T,N;
int main(){
cin >> N;
for(i=0;i<N;i++){
	cin >> T;
	v1.resize(T);
	v2.resize(T);
	for(o=0;o<T;o++) cin >> v1[o];
	for(o=0;o<T;o++) cin >> v2[o];

	sort(v1.begin(),v1.end());
	sort(v2.begin(),v2.end());

	int res=0;
	for(o=0;o<T;o++){
		res+=v1[o]*v2[T-1-o];
	}
	cout << "Case #" << i+1 << ": " << res << endl;
}

}
