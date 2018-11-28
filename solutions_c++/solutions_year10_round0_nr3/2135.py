#include <iostream>

using namespace std;
long r, k, n;
long g[100];
int main()
{
	freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
	int Test;
	cin>>Test;
	
	for (int cas = 1; cas <= Test; ++cas) {
		cout <<"Case #"<<cas<<": ";
		cin>>r>>k>>n;
		for (int i = 0; i < n; ++i) {
			cin>>g[i];
		}
		long total = 0;
		long current;
		long index = 0;
		long start;
		while (r--) {
			start = index;
			current = 0;
			//
			while (1) {
				if ((current+g[index]) > k)
					break;
				current += g[index];
				++index;
				index = index % n;
				if (index == start)
					break;
			}
			total += current;
		}
		
		cout<<total <<endl;
	}
	return 0;
}	
