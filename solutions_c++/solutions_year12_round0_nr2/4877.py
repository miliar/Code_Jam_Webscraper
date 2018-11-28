#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
#include <vector>
#define F(a, b) for (int a = 0; a < b; a++)

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::bind;
using std::begin;
using std::end;
using std::greater;

int main(int argc, char* argv[])
{
	int cases;
	cin >> cases;
	F(i, cases)
	{
		int score_count;
		int surprising;
		int min;
		cin >> score_count >> surprising >> min;
		vector<int> scores;
		F(j, score_count) { int v; cin >> v; scores.push_back(v); }

		min = min * 3 - 2;
		int count = std::count_if(begin(scores), end(scores), [=](int v) { return v >= min; });
		int count_s = std::count_if(begin(scores), end(scores), [=](int v) { return v >= min - 2 && v < min && v > 1; });
		cout << "Case #" << i + 1 << ": " << count + std::min(count_s, surprising) << endl;
	}
}

