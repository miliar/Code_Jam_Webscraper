#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> a;
vector<int> speed;
vector<int> number;

int main()
{
	int test_cases;
	ofstream out("out.txt");
	ifstream in("C.in");
	in >> test_cases;
	for(int i = 1; i <= test_cases; i++)
	{
		int n, m;
		long long x, y, z;
		in >> n >> m >> x >> y >> z;
		x %= z;
		y %= z;
		for(int j = 0; j < m; j++)
		{
			int s;
			in >> s;
			a.push_back(s);
		}
		for(int j = 0; j < n; j++)
		{
			speed.push_back(a[j % m]);
			//cout << a[j % m] << endl;
			a[j % m] = (x * a[j % m] + y * (j + 1)) % z;
		}
		number.push_back(1);
		for(int j = 1; j < n; j++)
		{
			int answer = 1;
			for(int k = 0; k < j; k++)
				if(speed[k] < speed[j])
				{
					answer += number[k];
					answer %= 1000000007;
				}
			number.push_back(answer);
		}
		int answer = 0;
		for(int j = 0; j < n; j++)
		{
			answer += number[j];
			answer %= 1000000007;
		}
		out << "Case #" << i << ": " << answer << endl;
		a.clear();
		speed.clear();
		number.clear();
	}
	return 0;
}