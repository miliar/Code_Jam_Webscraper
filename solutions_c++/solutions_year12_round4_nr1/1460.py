#define _SECURE_SCL 0

#include <iostream>
#include <math.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#ifdef _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
#else// _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
//#define	Assert(E)		do { if (!(E)) { } } while (false)
#endif//_DEBUG

typedef unsigned long DWORD;
typedef unsigned char BYTE;
typedef unsigned __int64 QWORD;

//--------------------------------------------------------------------------------------------------
struct vine
{
	int d;
	int l;
	bool operator <(const vine &in_a) const
	{
		return d < in_a.d;
	}
};

struct cs
{
	int d;
	int len;

	bool operator <(const cs &in_a) const
	{
		if (d < in_a.d) return true;
		if (d > in_a.d) return false;
		return len < in_a.len;
	}
};

std::set<cs> m;
vector<vine> vines;

bool Test(int in_d, int in_len, int in_de)
{
	Assert(in_len > 0);
	if (in_d + in_len >= in_de) return true;

	cs cc;
	cc.d = in_d;
	cc.len = in_len;
	if (m.find(cc) != m.end()) return false;
	m.insert(cc);

	int b = 0, e = int(vines.size());
	for(;;)
	{
		int m = (b + e) / 2;
		if (m == b) break;
		if (m >= int(vines.size())) break;
		if (vines[m].d <= in_d - in_len)
			b = m;
		else
			e = m;
	}

	Assert(!b || (vines[b-1].d <= in_d - in_len));

	for(int i = b; i < int(vines.size()); ++i)
	{
		if (vines[i].d <= in_d - in_len) continue;
		if (vines[i].d > in_d + in_len) break;

		int tlen = abs(vines[i].d - in_d);
		if (tlen == 0) continue;
		Assert(tlen <= in_len);

		if (vines[i].l < tlen)
		{
			tlen = vines[i].l;
		}

		if (Test(vines[i].d, tlen, in_de)) return true;
	}

	return false;
}

//--------------------------------------------------------------------------------------------------
void ProcessTask(int in_id)
{
	int n;
	cin >> n;

	vines.resize(n);
	for(int i = 0; i < n; ++i)
	{
		cin >> vines[i].d;
		cin >> vines[i].l;
	}

	int d0 = vines[0].d;
	int de;
	cin >> de;

	m.clear();
	std::sort(vines.begin(), vines.end());

	if (Test(d0, d0, de))
	{
		printf("Case #%d: YES\n", in_id + 1);
	}
	else
	{
		printf("Case #%d: NO\n", in_id + 1);
	}
}

//--------------------------------------------------------------------------------------------------

//--------------------------------------------------------------------------------------------------
int main()
{
	int numb;
	cin >> numb;
	cin.get();

	for(int i = 0; i < numb; ++i)
	{
		ProcessTask(i);
	}

	return 0;
}
