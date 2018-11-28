#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream f(argv[1]);
	
		int T;
		f >> T;
		for (int t = 0; t < T; t++) {
			int N;
			f >> N;
			vector<int> from;
			vector<int> to;
			for (int i = 0; i < N; ++i)
			{
				int a,b;
				f >> a;
				f >> b;
				from.push_back(a);
				to.push_back(b);
			}
			int inter = 0;
			for (int i=0; i < N; ++i)
			{
				for (int j=i+1; j < N; ++j) 
				{
					if (from[i] < from[j])
					{
						if (to[i] > to[j])
						{
							inter++;
						}
					}
					else
					{
						if (to[i] < to[j])
						{
							inter++;
						}
					}
				}
			}
			
			cout << "Case #" << t + 1 << ": " << inter << endl;
		}
	
    return 0;
}
