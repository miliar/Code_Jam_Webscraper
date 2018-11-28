#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

string calc()
{
	int N, K;
	cin >> N >> K;

	int m = (1<<N)-1;
	return (K&m) == m ? "ON" : "OFF";
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

