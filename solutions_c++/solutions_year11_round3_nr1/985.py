#include <vector>
#include <iostream>
#include <string> 
#include <limits>

using namespace std;

int main()
{
	int T;
	cin>> T;


	for(int t = 0; t<T;++t) {
		int R;
		int C;
		cin>>R;
		cin>>C;
		vector<vector<char> > data(R, vector<char>(C,'.'));
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				char tmp;
				cin>> tmp;
				data[r][c] = tmp;
			}
		}
		for (int r = 0; r < R-1; ++r) {
			for (int c = 0; c < C-1; ++c) {
				if(data[r][c] == '#' && data[r][c+1] == '#' && data[r+1][c] == '#' && data[r+1][c+1] == '#') {
					data[r][c] = '/';
					data[r][c+1] = '\\';
					data[r+1][c] = '\\';
					data[r+1][c+1] = '/';
				}
			}
		}
		bool done = true;
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				if(data[r][c] == '#') {
					done = false;
				}
			}
		}
		cout<<"Case #"<<t+1<<":"<<endl;
		if (done) {
			for (int r = 0; r < R; ++r) {
				for (int c = 0; c < C; ++c) {
					cout<<data[r][c];
				}
				cout<<endl;
			}
		}
		else
		{
			cout<<"Impossible"<<endl;
		}
	}
}
