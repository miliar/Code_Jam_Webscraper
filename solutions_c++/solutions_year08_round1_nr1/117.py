#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long Integer;
const int MAXDIGIT = 5000;

int nOfTest;
vector<Integer> v1, v2;
int n;

struct BigNum
{
	Integer v[MAXDIGIT];
	int nOfDigit;
	bool neg;

	void fixBig();
	BigNum(Integer a = 0):nOfDigit(1), neg(false)
	{
		v[0] = a;
		fixBig();
	}
	BigNum& operator +=(Integer a);
	
	friend ostream& operator <<(ostream&, const BigNum&);
};

void BigNum::fixBig()
{
	for(int i=0; i<nOfDigit-1; i++)
	{
		v[i+1] += v[i]/10, v[i] %= 10;
		if (v[i] < 0)
			v[i] += 10, v[i+1]--;
	}
	while (v[nOfDigit-1] > 9)
		v[nOfDigit] = v[nOfDigit-1]/10, v[(nOfDigit++)-1] %= 10;
	if (v[nOfDigit-1] < 0)
	{
		neg = !neg;
		for(int i=0; i<nOfDigit; i++)
			v[i] = -v[i];
		fixBig();
		return;
	}
	while (nOfDigit > 1 && v[nOfDigit-1] == 0)
		nOfDigit--;
}

BigNum& BigNum::operator +=(Integer a)
{
	if (neg)
		a = -a;
	v[0] += a;
	fixBig();
}

ostream& operator <<(ostream& out, const BigNum& num)
{
	if (num.neg)
		cout << '-';
	for(int i=num.nOfDigit-1; i>=0; i--)
		cout << num.v[i];
}

void read()
{
	cin >> n;
	v1 = vector<Integer>(n), v2 = vector<Integer>(n);
	for(int i=0; i<n; i++)
		cin >> v1[i];
	for(int i=0; i<n; i++)
		cin >> v2[i];
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
}

void work()
{
	read();
	BigNum res;
	for(int i=0; i<n; i++)
	{
		res += v1[i]*v2[n-i-1];
//		cout << res << ' ';
	}
	cout << res << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
