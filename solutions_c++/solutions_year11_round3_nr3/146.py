#include <fstream>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

int freq[100];

int main()
{
	int t;
	input >> t;
	for (int z=0;z<t;++z)
	{
		int N, L, H;
		input >> N >> L >> H;		
		for (int i=0; i<N; ++i) input >> freq[i];
		int res = -1;
		for (int i=L;i<=H;++i)
		{
			int j;
			for (j=0; j<N; ++j)
				if (i%freq[j] && freq[j]%i) break;
			if (j==N) { res = i; break; }
		}
		output << "Case #" << z+1 << ": ";
		if (res!=-1) output << res << endl;
		else output << "NO" << endl;
	}
	return 0;
}