#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream f(argv[1]);
	
	if (!f.fail())
	//while (!f.eof())
	{
		int T;
		f >> T;
		for (int t = 0; t < T; t++) {
			int Rides, capacity, grps;
			f >> Rides;
			f >> capacity;
			f >> grps;

			vector<int> v;
			for (int i = 0; i < grps; ++i)
			{
				int x;
				f >> x;
				v.push_back(x);
			}
			
			vector<long long> M;
			M.resize(grps);
			vector<int> NEX;
			NEX.resize(grps);
			for (int i = 0; i < grps; ++i)
			{
				int rc = capacity;
				long long e = 0;
				int nx = 0;
				for (int j = 0; j < grps; ++j)
				{
					nx = (i+j)%grps;
					int s = v[nx];
					if (rc >= s)
					{
						e += s;
						rc -= s;
					}
					else
					{
						break;
					}
				}
				M[i] = e;
				NEX[i] = nx;
			}
			
			long long tot = 0;
			int c=0;
			for (int i = 0; i < Rides; ++i)
			{
				tot += M[c];
				c = NEX[c];
			}
			cout << "Case #" << t + 1 << ": " << tot << endl;
		}
	}
    return 0;
}
