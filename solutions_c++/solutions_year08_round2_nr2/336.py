#include <iostream>
#include <vector>
using namespace std;

typedef long long LL;

int TESTS, A, B, P, ans;
vector<int> v[2000];
bool prime[2000];

void Read()
{
	cin >> A >> B >> P;
}

bool is_prime(int n)
{
	if(n <= 1) return false;
	
	if(n == 2) return true;
	
	for(int i = 2; i * i <= n; i ++)
	{
		if(n % i == 0) return false;
	}
	
	return true;
}

void Solve()
{
	ans = 0;
	
	for(int i = 0; i < 2000; i ++) v[i].clear();
	
	for(int i = 2; i <= B; i ++)
	{
		prime[i] = is_prime(i);
	}
	
	for(int i = A; i <= B; i ++)
	{
		v[i].push_back(i);
	}
	
	for(int i = A; i <= B; i ++)
	{
		for(int j = i + 1; j <= B; j ++)
		{
			for(int p = P; p <= B; p ++)
			{
				if(i == 10 && j == 15)
				{
					int afasfaspf = 23135121;
				}
				
				if(prime[p])
				{
					bool ok_i = false, ok_j = false;
					
					for(int k = 0; k < v[i].size(); k ++)
					{
						if(v[i][k] % p == 0)
						{
							ok_i = true;
							
							break;
						}
					}
					
					for(int k = 0; k < v[j].size(); k ++)
					{
						if(v[j][k] % p == 0)
						{
							ok_j = true;
							
							break;
						}
					}
					
					if(ok_i && ok_j)
					{
						for(int k = 0; k < v[i].size(); k ++)
						{
							v[j].push_back(v[i][k]);
						}
						
						goto next_i;
					}
				}
			}
		}
		
		ans ++;
		
//		for(int k = 0; k < v[i].size(); k ++)
//		{
//			cout << v[i][k] << "  ";
//		}
//		cout << "\n";
//		system("pause");
		
		next_i:;
	}
}

void Write(const int test)
{
	cout << "Case #" << test << ": " << ans << "\n";
}

int main()
{
	cin >> TESTS;
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
//	system("pause");
	
	return 0;
}
/*
1
6 2 0 2 1 1 2 11
*/
