#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

class SnapperChain
{
	int N;
	long long K;
	int testcaseNum;
	ifstream& input;
	ofstream& output;
public:
	SnapperChain(ifstream& input, ofstream& output) : input(input), output(output) {}
	void runtc()
	{
		string line;
		input >> testcaseNum;
		getline(input, line);	// skip new line character of first line
		for (int i = 0; i < testcaseNum; i++)
		{
			input >> N >> K;
			getline(input, line);
			long long num = (long long) pow(2.0, N);
			bool on = (K % num == num - 1);
			output << "Case #" << i + 1 << ": " << ((on) ? "ON" : "OFF") << endl;
		}
	}
};

int main(int argc, char* argv[])
{
	ifstream input(argv[1]);
	ofstream output(argv[2]);
	SnapperChain s(input, output);
	s.runtc();
}
