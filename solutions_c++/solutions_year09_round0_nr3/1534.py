
//run:    cat input_file | ./preprocess_text.sh | ./count

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {


	int N;
	cin >> N;

	string line;
	getline(cin, line);
	for (int i = 0; i < N; i++) {
		getline(cin, line);
		istringstream in(line);
		vector<int> nb;
		int tmp;
		while (in >> tmp)
			nb.push_back(tmp);

		int cnt[20]; //1..19
		for (int j=0; j < 20; j++) {
			cnt[j] = 0;
		}


		cnt[0] = 1;
		for(vector<int>::iterator it = nb.begin(); it != nb.end(); it++) {
			cnt[*it] += cnt[*it - 1];
			cnt[*it] %= 10000;
		}
		cout << "Case #" << i+1 << ": ";
		printf("%04d", cnt[19]);
		cout << endl;

	}



	return 0;
}
