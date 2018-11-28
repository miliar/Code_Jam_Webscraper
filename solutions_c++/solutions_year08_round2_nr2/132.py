#include <iostream>
#include <vector>
#include <set>
using namespace std;
typedef long long LL;

bool pr[100000];
void init(int t = 100000)
{
	for(int i = 0; i < t; ++i)
		pr[i] = true;
	pr[0] = pr[1] = false;
	for(int i = 2; i * i <= t; ++i) if(pr[i])
		for(int j = i + i; j < t; j += i)
			pr[j] = false;
	

}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	init();
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{	
		LL a, b, p;
		cin >> a >> b >> p;
		int cnt = 0;
		vector<int> u(b + 1, 0);
		for(int i = a; i <= b; ++i)
			u[i] = i;
		bool fl = true;
		while(fl)
		{
			fl = false;
			for(int i = a; i <= b; ++i)
				for(int j = i + 1; j <= b; ++j) if(u[i] != u[j])
				{
					for(int k = p; k <= min(i, j); ++k)
						if(pr[k] && i % k == 0 && j % k == 0)
						{
							for(int r = a; r <= b; ++r)
								if(u[r] == u[j])								
									u[r] = u[i];
							fl = true;
							break;
						}			
				}
		}
		set<int> yy;
		for(int i = a; i <= b; ++i)
			yy.insert(u[i]);
		cout << "Case #" << z << ": " << yy.size() << endl;
	}

	return 0;
}