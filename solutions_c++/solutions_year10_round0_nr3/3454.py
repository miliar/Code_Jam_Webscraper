#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
	unsigned long long int T, R, k, N, temp, takenseats = 0, revenue=0;
	queue<int> waitinggroup;
	queue<int> outgroup;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in >> T;
	for (int i = 0; i < T; i++, revenue = 0) {
		in >> R >> k >> N;
		for (int j = 0; j < N; j++) {
			in >> temp;
			waitinggroup.push(temp);
		}
		for (int j = 0; j < R; j++) {
			while (!waitinggroup.empty()) {
				if (takenseats + waitinggroup.front() <= k) {
					takenseats+=waitinggroup.front();
					outgroup.push(waitinggroup.front());
					waitinggroup.pop();
				} else break;
			}
			revenue += takenseats;
			takenseats = 0;
			while (!outgroup.empty()) {
				waitinggroup.push(outgroup.front());
				outgroup.pop();
			}
		}
		out << "Case #" << i+1 << ": " << revenue << endl;
		while (!waitinggroup.empty()) waitinggroup.pop();
	}
	system("pause>null");
	return 0;
}
//---------------------------------------------------------------------------
