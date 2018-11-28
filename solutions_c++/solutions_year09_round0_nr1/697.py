#include <vector>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;
int L, D, N;
string words[5000], pattern;
vector<int> data;
void make()
{
    size_t cur = 0;
    for (int i=0; i<L; ++i, ++cur)
    {
	if (pattern[cur] != '(') {
	    data[i] = 1 << (pattern[cur]-'a');
	    continue;
	}
	data[i] = 0; ++cur;
	while (pattern[cur] != ')')
	    data[i] |= 1 << (pattern[cur++]-'a');
    }
    assert(cur == pattern.size());
}
bool match(const string& word)
{
    for (int i=0; i<L; ++i)
	if ((data[i] & (1<<(word[i]-'a'))) == 0)
	    return false;
    return true;
}
int main()
{
    cin >> L >> D >> N;
    for (int i=0; i<D; ++i)
	cin >> words[i];
    data.resize(L);
    for (int i=0; i<N; ++i)
    {
	cin >> pattern;
	make();
	int count = 0;
	for (int j=0; j<D; ++j)
	    if (match(words[j]))
		++count;
	cout << "Case #" << i+1 << ": " << count << endl;
    }
}
