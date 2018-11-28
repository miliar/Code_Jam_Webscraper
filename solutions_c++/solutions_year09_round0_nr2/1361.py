#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	size_t T;
	cin>>T;
	for(size_t ttt = 0; ttt<T; ++ttt) {
		size_t W,H;
		cin>>H>>W;
		vector<vector<int> > data;
		data.resize(H+2);
		data[0].resize(W+2, 1000000);
		data[H+1].resize(W+2, 1000000);
		for(size_t h = 1; h<=H; ++h) {
			data[h].resize(W+2, 1000000);
			for(size_t w = 1; w<=W; ++w) {
				cin>>data[h][w];
			}
		}

		vector<vector<int> > markers;
		markers.resize(H+2);
		for(size_t h = 0; h<=H+1; ++h) {
			markers[h].resize(W+2, 0);
		}

		// find the most down points
		int marker = 1;
		for(size_t h = 1; h <= H; ++h) {
			for(size_t w = 1; w <= W; ++w) {
				int ph = data[h][w];
				if(ph <= data[h-1][w] && ph<=data[h+1][w] && ph<=data[h][w-1] && ph<=data[h][w+1])
					markers[h][w] = marker++;
			}
		}

		// Go!
		int counter;
		do {
			counter = 0;
			for(size_t h = 1; h <= H; ++h) {
				for(size_t w = 1; w <= W; ++w) {
					if(markers[h][w] != 0)
						continue;

					++counter;

					if(markers[h+1][w] == 0 && markers[h-1][w] == 0 && markers[h][w+1] == 0 && markers[h][w-1] == 0) {
						++counter;
						continue;
					}

					int min_h = min(min(data[h-1][w], data[h+1][w]), min(data[h][w-1], data[h][w+1]));

					if(data[h-1][w] == min_h)
						markers[h][w] = markers[h-1][w];
					else if(data[h][w-1] == min_h)
						markers[h][w] = markers[h][w-1];
					else if(data[h][w+1] == min_h)
						markers[h][w] = markers[h][w+1];
					else if(data[h+1][w] == min_h)
						markers[h][w] = markers[h+1][w];
				}
			}

			/* // Test output
			for(size_t h = 1; h <= H; ++h) {
				for(size_t w = 1; w <= W; ++w) {
					cout<<markers[h][w]<<' ';
				}
				cout<<endl;
			}
			cout<<counter<<endl; // */

		} while(counter > 0);

		// output labels
		map<int, char> labels;
		char fl = 'a';
		cout<<"Case #"<<ttt+1<<":\n";
		for(size_t h = 1; h <= H; ++h) {
			for(size_t w = 1; w <= W; ++w) {
				char label = labels[markers[h][w]];
				if(label < 'a' || label > 'z') {
					label = fl;
					labels[markers[h][w]] = fl++;
				}
				cout<<label<<' ';
			}
			cout<<endl;
		}
	}
}

