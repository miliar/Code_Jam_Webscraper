#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <sstream>
#include <cmath>
#include <map>

using namespace std;

int main(void){
	int T, N, M;
	cin >> T;
	for(int cas=1; cas <= T; cas++){
		cin >> N >> M;
		map<string,bool> ja;
		for(int i = 0; i < N; i++){
			string path;
			cin >> path;
			ja[path] = true;
		}
		int res = 0;
		for(int i = 0; i < M; i++){
			string path;
			cin >> path;
			if(path == "/") continue;
			for(int j = 1; j < path.size(); j++){
				if(path[j] == '/'){
					string sub = path.substr(0,j);
					if(!ja[sub]) {
						res++;
						ja[sub] = true;
					}
				}
			}
			if(!ja[path]){
				res++;
				ja[path] = true;
			}
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
