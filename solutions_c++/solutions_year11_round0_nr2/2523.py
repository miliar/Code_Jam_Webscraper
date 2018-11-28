#include <cstdio>
#include <string>
#include <vector>
#include <set>

using namespace std;

int C, D, N;
vector<string> combine, oppose;
string invokations;

string read_string(int len)
{
	string s;
	int ch;
	for (int i = 0; i < len; i++) {
		do {
			ch = getchar();
		} while (ch < 'A' || ch > 'Z');
		s += ch;
	}

	return s;
}

vector<string> read_vector_string(int& N, int str_len)
{
	scanf("%d", &N);
	vector<string> res(N);
	for (int i = 0; i < N; i++)
		res[i] = read_string(str_len);
	return res;
}

void normalize_pair(string &s)
{
	if (s[0] > s[1])
		swap(s[0], s[1]);
}

bool match_pair(const string& a, const string& b)
{
	return a[0] == b[0] && a[1] == b[1];
}

void read_input()
{
	combine = read_vector_string(C, 3);
	oppose = read_vector_string(D, 2);
	scanf("%d", &N);
	invokations = read_string(N);

	for (int i = 0; i < C; i++)
		normalize_pair(combine[i]);
	for (int i = 0; i < D; i++)
		normalize_pair(oppose[i]);
}

string solve()
{
	vector<char> elements;
	for (int i = 0; i < N; i++) {
		elements.push_back(invokations[i]);

		// Process combine
		bool combined = false;
		while (true) {
			if (elements.size() < 2)
				break;

			string last_pair = "";
			last_pair += *(elements.end()-2);
			last_pair += *(elements.end()-1);
			normalize_pair(last_pair);

			bool combined_now = false;
			for (int j = 0; j < C; j++) {
				if (match_pair(combine[j], last_pair)) {
					combined_now = true;
					elements.pop_back();
					elements.pop_back();
					elements.push_back(combine[j][2]);
					break;
				}
			}

			if (combined_now)
				combined = true; else
				break;
		}

		// Process opposition
		if (!combined) {
			set<char> present(elements.begin(), elements.end());
			for (int j = 0; j < D; j++)
				if (present.count( oppose[j][0] ) &&
					present.count( oppose[j][1] )) {
						elements.clear();
						break;
				}
		}
	}

	// Form output string
	string res = "[";
	for (int i = 0; i < elements.size(); i++) {
		if (i > 0)
			res += ", ";
		res += elements[i];
	}
	res += "]";

	return res;
}

int main()
{
//	freopen("B-small-attempt0.in", "rt", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "w", stdout);

//	freopen("input.txt", "rt", stdin);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++) {
		read_input();
		printf("Case #%d: %s\n", iTest+1, solve().c_str());
	}
	return 0;
}
