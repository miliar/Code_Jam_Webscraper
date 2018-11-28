#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Char {
	int num;
	int freq;
	friend class SortByFreq;
public:
	Char(int nnum, int ffreq):num(nnum),freq(ffreq) {}
	int GetNum() const { return num; }
	int GetFreq() const { return freq; }
	class SortByFreq {
	public:
		bool operator() ( const Char &s1, const Char &s2 )
		{
			return (s1.freq > s2.freq);
		}
	};
};

int main()
{
	int n;
	int tc;
	cin >> n;
	for (int tc = 0; tc < n; tc++ )
	{
		vector<Char> freq;
		int p,k,l;
		cin >> p >> k >> l;
		for (int i=0; i<l; i++)
		{
			int j;
			cin >> j;
			Char ch(i, j);
			freq.push_back(ch);
		}
		Char::SortByFreq fq;
		sort(freq.begin(), freq.end(), fq);
		int count = 0;
		int round = 0;
		for (int i=0; i<l; i++)
		{
//			cout << freq[i].GetNum() << " " << freq[i].GetFreq() << endl;
			if (i%k == 0) round++;
			count += round * freq[i].GetFreq();
		}
		cout << "Case #" << tc+1 << ": " << count << endl;
	}
	return 0;
}

