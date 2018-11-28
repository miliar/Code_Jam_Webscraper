#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string gen_text(const string &org, const vector<int> &order)
{
	char text[org.length()];
	for (size_t i = 0; i < org.length(); ++i)
	{
		size_t offset = (i / order.size()) * order.size();
		int mod = order[i % order.size()];
		text[i] = org[offset + mod];
	}
	return string(text, org.length());
}

int count_groups(const string &text)
{
	int c = 1 << 20;
	int count = 0;
	for (size_t i = 0; i < text.length(); ++i)
	{
		count += static_cast<unsigned char>(text[i]) != c;
		c = static_cast<unsigned char>(text[i]);
	}
	return count;
}

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int K;
		cin >> K;

		string org;
		getline(cin, org);
		getline(cin, org);

		vector<int> order;
		for (int j = 0; j < K; ++j)
			order.push_back(j);

		int pattern = 1;
		for (int j = K; j > 1; --j)
			pattern *= j;

		int min_count = 1 << 20;
		for (int j = 0; j < pattern; ++j)
		{
			string text = gen_text(org, order);
			int count = count_groups(text);
			if (count < min_count)
				min_count = count;
			next_permutation(order.begin(), order.end());
		}

		cout << "Case #" << (i + 1)
			<< ": " << min_count << endl;
	}

	return 0;
}
