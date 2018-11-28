#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <set>
#include <ctime>
#include <numeric>
#include <fstream>

using namespace std;

int main(int argc,const char * argv[]){
	istream * _if;
	ostream * _of;
	if (argc > 1)
		_if = new ifstream(argv[1]);
	else
		_if = &cin;
	if (argc > 2)
		_of = new ofstream(argv[2]);
	else
		_of = &cout;
	istream &fin = *_if;
	ostream &fout = *_of;

	int vis[1001];
	long long time[1001];

	int TC;
	fin >> TC;
	for (int tc=1;tc<=TC;tc++){
		memset(vis,-1,sizeof(vis));
		memset(time,-1,sizeof(time));
		long long R,k,N;
		fin >> R >> k >> N;
		vector <long long> g(N);
		for (int i=0;i<N;i++)
			fin >> g[i];
		long long tot=0,ans = 0;
		for (int i=0;i<N;i++)
			tot += g[i];
		if (tot <= k)
			ans = tot * R;
		else{
			int front = 0;
			bool done = false;
			for (int i=0;i<R;i++){
				//cout << i << " " << front << " " << ans << endl;
				if (vis[front]>-1 && !done){
					done = true;
					long long len = i-vis[front];
					long long count = (R-i) / len;
					//cout << "Cycle " << len << " " << ans - time[front] << " " << count;
					ans += count * (ans - time[front]);

					i += count * (i-vis[front]);
					//cout << " " << ans << endl;
					memset(vis,-1,sizeof(vis));
					memset(time,-1,sizeof(time));
				}
				if (i==R) break;
				vis[front] = i;
				time[front] = ans;
				long long num = 0;
				int j;
				for (j=0;j<N && num+g[(front+j) % N] <= k;j++)
					num+=g[(front+j)%N];
				ans += num;
				front = (front+j)%N;
			}
		}

		fout << "Case #" << tc << ": " << ans << endl;
		if (_of != &cout)
			cout << "Case #" << tc << ": " << ans << endl;
	}



	delete _if;
	delete _of;

}