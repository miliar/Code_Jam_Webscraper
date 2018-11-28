#include <stdio.h>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <math.h>

using namespace std;

typedef pair< unsigned, unsigned > btn_t;

typedef vector< pair<unsigned, unsigned > > sequence_t;

typedef map< string, char > base_t;
typedef map<char, char> opposed_t;

//#define KDEBUG
#ifdef KDEBUG
#define DPRINT(x) printf("%s", x )
#define VAL(x) cout << "value " << #x << " = " << x << endl;
#else
#define DPRINT(x) ;
#define VAL(x) ;
#endif
/*

5 + 4 = 1
7 + 9 = 14
50 + 10 = 56

*/
class qint
{
	public:
	int value;
	qint(int v) : value(v) {};
	qint &operator + (const qint &q)
	{
		this->value = value ^ q.value;
		return *this;
	};
	qint &operator= (int x)
	{
		this->value = x;
		return *this;
	};
	qint(const qint &q)
	{
		this->value = q.value;
	};
};


void solve( unsigned case_no, vector<int> &candies )
{
	bool solved = false;
	int result = 0xfafad;
//	qint a = 5;
//	qint b = 4;
//	a = a+b;
//	printf("%d\n", a.value);
	unsigned mx = pow(2,candies.size());
	long long set1 = 0;
	long long set2 = 0;
	long long set1r = 0;
	long long set2r = 0;
	long long  max = -1;

	for (unsigned i = 1; i < mx-1; ++i)
	{
		set1 = 0;
		set2 =0;
		set1r = 0;
		set2r = 0;
		for (int j = 0;j < candies.size();++j)
		{
			if ((i >> j) & 1)
			{
				set1 ^=candies[j];
				set1r +=candies[j];
			}
			else
			{
				set2 ^=candies[j];
				set2r +=candies[j];
			}
		}
		if (set1 == set2)
		{
			int localmax = set1r;
			if (set2r > set1r) localmax = set2r;
			if (localmax > max) max = localmax;
		}
	}

	printf("Case #%d: ", case_no);
	if ( max > 0 ) printf("%lld\n", max);
	else printf("NO\n");
}

int main()
{
	unsigned _tc;
	scanf("%d", &_tc );
	for (unsigned _tc_it= 0; _tc_it < _tc; ++_tc_it)
	{
		vector<int> data;
		int q;
		int x;
		scanf("%d", &x);
		for (int i = 0;i < x;++i)
		{
			scanf("%d", &q);
			data.push_back(q);

		}
		solve( _tc_it + 1, data);
	}
};
