#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int main(int c, char* v[]) {
	char ob;
	int n1;
	int T;
	cin >> T;
	for (int i=0;i<T;++i) {		
		deque<int> orange;
		deque<int> blue;
		vector<int> order;
		int N;
		cin >> N;
		int previousO = 1;
		int previousB = 1;

		for (int j=0;j<N;++j) {
			cin >> ob;
			cin >> n1;
			if (ob == 'O') {
				order.push_back(0);
				orange.push_back(abs(n1 - previousO));
				previousO = n1;
			}
			else {
				order.push_back(1);
				blue.push_back(abs(n1 - previousB));
				previousB = n1;
			}
		}
		int result = 0;
		for (int j=0;j<order.size();++j) {
			if (order[j] == 0) {
				orange[0] = max(orange[0],0);
				result += orange[0];
				if (!blue.empty())
					blue[0] -= (orange[0]+1);
				orange.pop_front();
			}
			else {
				blue[0] = max(blue[0],0);
				result += blue[0];
				if (!orange.empty())
					orange[0] -= (blue[0]+1);
				blue.pop_front();
			}
			++result;
		}
		cout << "Case #" <<i+1<<": "<< result<<'\n';
	}
}