#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
vector <long long> V;
int main()
{
    int t;
    int x = 1;
    scanf("%d", &t);
    while(t--)
    {
			V.clear();
            long long r, k, n, suma = 0, wynik = 0;
			scanf("%lld %lld %lld", &r, &k, &n);
			for(int i = 0; i < n; i++)
			{
				long long b;
			  	scanf("%lld", &b);
			  	suma += b;
				V.push_back(suma);
			}
			for(int i = 0; i < r; i++)
			{
				long long poz = upper_bound(V.begin(), V.end(), k) - V.begin();
				if(poz == n)
				{
					wynik += V[poz-1];
					continue;
				}
				if(poz)
				{
					wynik += V[poz-1];
					for(int j = poz; j < V.size(); j++)
						V[j] -= V[poz-1];
					int delta = V[V.size()-1];
					V.insert(V.end(), poz, 0);
					replace_copy(V.begin(), V.begin()+poz, V.end()-poz,0,0);
					V.erase(V.begin(), V.begin()+poz);	
					for(int j = n-poz; j < V.size(); j++)
						V[j] += delta;
				}
			}
			printf("Case #%d: %lld\n",x++,wynik);
    }
    return 0;
}
