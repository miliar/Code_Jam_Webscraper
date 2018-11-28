#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

map<string, int> cnt;

void work()
{
	cnt.clear();
	int N, M;
	cin >> N >> M;
	string path;
	getline(cin, path);
	for(int i=0; i<N; i++){
		getline(cin, path);
		while (true){
			cnt[path]++;
			int pos = path.find_last_of('/');
			if (pos == string::npos || pos == 0)
				break;
			path = path.substr(0, pos);
		}
	}
	int res = 0;
	for(int i=0; i<M; i++){
		getline(cin, path);
		while (true){
			if (cnt.find(path) == cnt.end()){
				//cerr << "Add: " << path << endl;
				res++;
			}
			cnt[path]++;
			int pos = path.find_last_of('/');
			if (pos == string::npos || pos == 0)
				break;
			path = path.substr(0, pos);
		}
	}
	cout << res << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int i=0; i<T; i++){
		printf("Case #%d: ", i+1);
		work();
	}
}

