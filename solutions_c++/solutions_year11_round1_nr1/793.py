//Aleksander "kaalex" Kramarz

#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

const int base = 1000000000;
const int digs = 9;

class bignum
{
	public:
		vector<int> num;
		bignum(long long liczba)
		{
			num.push_back(liczba%base);
			liczba/=base;
			if(liczba)
				num.push_back(liczba);
		}
		bignum()
		{
			num.clear();
		}
		void read()
		{
			char liczba[1000000];
			scanf("%s", liczba);
			int len = strlen(liczba);
			
			num.clear();
			if(len % digs == 0)
				num.resize(len/digs, 0);
			else
				num.resize(len/digs + 1, 0);
			//printf("%d", num.size());
			
			--len;
			
			for(int i = 0; i < num.size(); i++)
			{
				for(int j = max(0, len-digs+1); j <= len; j++)
					num[i] = num[i]*10 + (liczba[j] - '0');
				len -= digs;
			}
		}
		void print()
		{
			vector<int>::iterator it = --(num.end());
			printf("%d", *it);
			while(it-- != num.begin())
				printf("%0*d", digs, *it);
			printf("\n");
		}
};

bool operator< (bignum A, bignum B)
{
	if(A.num.size() == B.num.size())
	{
		for(int i = A.num.size()-1; i >= 0; i--)
			if(A.num[i] != B.num[i])
				return A.num[i] < B.num[i];
		return A.num.size() < B.num.size();
	}
	return A.num.size() < B.num.size();
}

bool operator> (bignum A, bignum B)
{
	return B < A;
}

bool operator== (bignum A, bignum B)
{
	return !(A < B) && !(A > B);
}

bool operator!= (bignum A, bignum B)
{
	return !(A == B);
}

bool operator< (bignum A, int B)
{
	if(A.num.size() == 1)
		return A.num[0] < B;
	return false;
}

bool operator> (bignum A, int B)
{
	if(A.num.size() > 1)
		return true;
	return A.num[0] > B;
}

bool operator== (bignum A, int B)
{
	return !(A < B) && !(A > B);
}

bool operator!= (bignum A, int B)
{
	return !(A == B);
}



bignum operator+ (bignum A, bignum B)
{
	int tmp = 0;
	bignum res;
	
	while(A.num.size() < B.num.size())
		A.num.push_back(0);
	
	while(B.num.size() < A.num.size())
		B.num.push_back(0);
	
	for(int i = 0; i < A.num.size(); i++)
	{
		res.num.push_back((A.num[i] + B.num[i] + tmp) % base);
		tmp = (A.num[i] + B.num[i] + tmp) / base;
	}
	
	if(tmp > 0)
		res.num.push_back(tmp);
	return res;
}

bignum operator- (bignum A, bignum B)
{
	int tmp = 0;
	bignum res;
	
	while(B.num.size() < A.num.size())	//zakladamy, ze wynik bedzie dodatni
		B.num.push_back(0);
	
	for(int i = 0; i < A.num.size(); i++)
	{
		res.num.push_back(A.num[i] - B.num[i] + tmp);
		if(res.num.back() < 0)
		{
			res.num.back() += base;
			tmp = -1;
		}
		else
			tmp = 0;
	}
	while(res.num.back() == 0 && res.num.size() > 1)
		res.num.pop_back();
	
	return res;
}

bignum operator* (bignum A, int B)
{
	bignum res;
	long long tmp = 0;
	
	for(int i = 0; i < A.num.size(); i++)
	{
		res.num.push_back(static_cast<int>((static_cast<long long>(A.num[i]) * static_cast<long long>(B) + tmp) % static_cast<long long>(base)));
		tmp = (static_cast<long long>(A.num[i]) * static_cast<long long>(B) + tmp) / static_cast<long long>(base);
	}
	while(tmp > 0)
	{
		res.num.push_back(static_cast<int>(tmp % static_cast<long long>(base)));
		tmp /= static_cast<long long>(base);
	}
	return res;
}
	
bignum operator* (bignum A, bignum B)
{
	bignum res(0), pom;
	
	for(int i = 0; i < A.num.size(); i++)
	{
		long long tmp = 0;
		for(int j = 0; j < i; j++)
			pom.num.push_back(0);
		for(int j = 0; j < B.num.size(); j++)
		{
			pom.num.push_back(static_cast<int>((static_cast<long long>(A.num[i]) * static_cast<long long>(B.num[j]) + tmp) % static_cast<long long>(base)));
			tmp = (static_cast<long long>(A.num[i]) * static_cast<long long>(B.num[j]) + tmp) / static_cast<long long>(base);
		}
		while(tmp > 0)
		{
			pom.num.push_back(static_cast<int>(tmp % static_cast<long long>(base)));
			tmp /= static_cast<long long>(base);
		}
		res = res + pom;
		pom.num.clear();
	}
	while(res.num.back() == 0 && res.num.size() > 1)
		res.num.pop_back();
	return res;
}

bignum operator/ (bignum A, bignum B)
{
	bignum res(0), pom;
	if(A < B)
		return res;
	res.num.pop_back();
	
	int i = A.num.size();
	while(pom.num.size() < B.num.size())
		pom.num.insert(pom.num.begin(), A.num[--i]);
	
	while(i >= 0)
	{
		int x = 0, y = base-1;
		while(x < y)
		{
			int z = (x+y) / 2 + 1;
			if(B * z > pom)
				y = z-1;
			else
				x = z;
		}
		res.num.insert(res.num.begin(), x);
		pom = pom - (B * x);
		while(pom.num.back() == 0)
			pom.num.pop_back();	
		--i;
		if(i >= 0)
			pom.num.insert(pom.num.begin(), A.num[i]);
	}
	while(res.num.back() == 0 && res.num.size() > 1)
		res.num.pop_back();
	
	return res;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int z = 1; z <= t; z++)
	{
		long long n, pd, pg;
		scanf("%lld%lld%lld", &n, &pd, &pg);
		long long d1 = (100*pd)/__gcd(100LL,pd);
		if(pd)
			d1 /= pd;
		else
			d1 = 1;
		printf("Case #%d: ", z);
		long long w = pd*d1/100;
		if((w>0 && d1 <= n && pg < 100 && pg > 0) || (w==0 && pg==0) || (pd==100 && pg==100))
			printf("Possible\n");
		else
			printf("Broken\n");
	}
}
