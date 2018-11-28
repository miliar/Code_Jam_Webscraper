#include <vector>
#include <iostream>
#include <string>

using namespace std;

struct TestCase
{
	int size;
	int surprising;
	int value;
	vector<int> scores;
};

int up(int n)
{
	if(n < 0)
		n = 0;
	return n;
}

int resolved(TestCase t)
{
	int s;
	int val = t.value;
	int minNormal = val + up((val-1) * 2);
	int minSurprising = val + up((val - 2) * 2);
	int count = 0;
	for(int i = 0 ; i < t.size ; ++i)
	{
		s = t.scores[i];
		if(s >= minNormal)
			count++;
		else if(s >= minSurprising && t.surprising > 0)
		{
			t.surprising--;
			count++;
		}
	}
	return count;
}

int main(int argc, char *argv[])
{
	int numberOfTestCase;

	cin >> numberOfTestCase;

	for(int i = 0 ; i < numberOfTestCase ; ++i)
	{
		TestCase t;
		cin >> t.size;
		cin >> t.surprising;
		cin >> t.value;

		for(int k = 0 ; k < t.size ; ++k)
		{
			int n;
			cin >> n;
			t.scores.push_back(n);
		}

		cout << "Case #" << (i+1) << ": " << resolved(t) << endl;
	}

	return 0;
}

