#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

vector<long long> place_on_each_key;
vector<long long> freec;
long long N, P, K, L;

typedef vector<long long>::iterator VII;

long long FindPlace()
{
	long long place;
	long long ret = P+2;
	for (size_t i=0; i<place_on_each_key.size(); i++)
		if (place_on_each_key[i] < ret) {ret = place_on_each_key[i]; place = i; }
	place_on_each_key[place]++;
	return ret;
}

bool srt(const long long a, const long long b)
{
	return (a>b);
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");

	long long t, place, ans;

	in >> N;
	for (long long i=0; i<N; i++){
		ans = 0;
		freec.clear();
		place_on_each_key.clear();
		in >> P >> K >> L;
		for (int j=0; j<L; j++){
			in >> t;
			freec.push_back(t);
		}
		sort(freec.begin(), freec.end(), srt);
		for (long long j=0; j<K; j++) place_on_each_key.push_back(1);
		for (size_t j=0; j<freec.size(); j++){
			place = FindPlace();
			ans += place * freec[j];
		}
		out << "Case #" << i+1 << ": " << ans << endl;
	}

	out.close();
	in.close();

	return 0;
}