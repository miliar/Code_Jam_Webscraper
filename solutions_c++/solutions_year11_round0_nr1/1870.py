#include <iostream>
#include <vector>
#include <map>
using namespace std;

struct in {
	bool color;
	int pos;
};

int sgn(int x) {
	return (x > 0) - (x < 0);
}

void d(char a) {
	//cout << a << endl;
}

int main() {
	int N; cin >> N;
	for (int I=0; I<N; ++I) {
		//read input file
		int n; cin >> n;
		in read;
		vector<in> data;
		char color;
		for (int i=0; i<n; ++i) {
			cin >> color;
			read.color=(color=='B');
			cin >> read.pos;
			data.push_back(read);
		}
		
		vector<int> pos(2,1), move(2,1000);
		for(int i=0; i<data.size(); ++i) {
			if (move[data[i].color]==1000) move[data[i].color]=i;
		}
		//cout << move[0] << " " << move[1] << endl;
		
		int sum=0;
		while(move[0]!=1000 or move[1]!=1000) {
			++sum;
			bool done=false;
			for(int i=0; i<2; ++i) {
				if (data[move[i]].pos!=pos[i]) {
					pos[i]+=sgn(data[move[i]].pos-pos[i]);
				} else if (move[i]<move[1-i] and !done) {
					done=true;
					move[i]++;
					//ugly duplicated code
					if (data.size()==move[i]) {
						move[i]=1000;
						break;
					}
					while(data[move[i]].color!=i) {
						move[i]++;
						if (data.size()==move[i]) {
							move[i]=1000;
							break;
						}
					}
				}
			}
			//cout << move[0] << " " << move[1] << endl;
			//cout << pos[0] << " " << pos[1] << endl;
		}

		cout << "Case #" << I+1 << ": " << sum << endl;
	}
}
