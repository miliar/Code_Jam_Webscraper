
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Disjointsets
{
    private:
        vector<int> p, rank;
    public:
        void init(int n)
        {
            rank.assign(n, 0);
            p.resize(n);
            for (int i=0; i<n; i++)
                p[i] = i;
        }
        int find_set(int x)
        {
            if (x != p[x])
                return p[x] = find_set(p[x]);
            return x;
        }
        void unite(int x, int y)
        {
            x = find_set(x);
            y = find_set(y);
            if (rank[x] > rank[y])
                p[y] = x;
            else
            {
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y]++;
            }
        }
};

int main()
{
	int n = 1024;
	vector<int> prime(n, 1);
	vector<int> bigf(n, 1);
	prime[0] = prime[1] = 0;
	for (int i=2; i<n; i++)
	{
		if (!prime[i])
			continue;
		for (int m=i+i; m<n; m+=i)
		{
			prime[m] = 0;
			bigf[m] = i;
		}
	}
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int a, b, p;
		cin >> a >> b >> p;
		vector<int> pr;
		for (int i=p; i<=b; i++) // ??
			if (prime[i])
				pr.push_back(i);
		Disjointsets d;
		d.init(b+1);
		for (int r=a; r<=b; r++)
			for (int s=r+1; s<=b; s++)
				for (int k=0; k<(int)pr.size(); k++)
					if ((r % pr[k] == 0) && (s % pr[k] == 0))
					{
						d.unite(r, s);
						break;
					}
		set<int> s;
		for (int i=a; i<=b; i++)
			s.insert(d.find_set(i));
		cout << "Case #" << kase << ": " << s.size() << endl;
	}
	return 0;
}
