#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge
{
	int u, v;
};

int main()
{
	int nCase;
	cin >> nCase;
	for(int iCase = 1; iCase <= nCase; iCase++) {
		int m, n;

		cin >> n;

		vector<Edge> gbig(n);

		for(int i = 0; i < n - 1; i++) {
			cin >> gbig[i].u >> gbig[i].v;
		}

		cin >> m;

		vector<Edge> gsml(m);

		for(int i = 0; i < m - 1; i++) {
			cin >> gsml[i].u >> gsml[i].v;
		}

		vector<int> sigma(n);

		for(int i = 0; i < n; i++)
			sigma[i] = i + 1;

		bool okay;

		do {
			okay = true;

			for(int i = 0; i < m - 1; i++) {
				int uu = sigma[gsml[i].u - 1];
				int vv = sigma[gsml[i].v - 1];

				bool found = false;

				for(int j = 0; j < n - 1; j++) {
					if(gbig[j].u == uu && gbig[j].v == vv) {
						found = true;
						break;
					}
					if(gbig[j].u == vv && gbig[j].v == uu) {
						found = true;
						break;
					}
				}

				if(!found) {
					okay = false;
					break;
				}
			}
		}
		while(!okay && next_permutation(sigma.begin(), sigma.end()));

		cout << "Case #" << iCase << ": " << (okay ? "YES" : "NO") << endl;
	}

	return 0;
}
