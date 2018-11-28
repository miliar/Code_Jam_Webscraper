#include <iostream>
using namespace std;

#define INPUTFILENAME "B-large.in.txt"
#define OUTPUTFILENAME "output.txt"

const int maxn = 1001;

int time[maxn], kind[maxn];
//kind 
// 1: arrived at A 
// 2: arrived at B
// 3: departed from A 
// 4: departed from B
int n, m;

void init()
{
	m = 0;
	char ch;
	int na, nb, t1, t2, turnaround;
	cin >> turnaround >> na >> nb;
	for (int i = 0; i < na; i++)
	{
		cin >> t1 >> ch >> t2;
		t1 = t1 * 60 + t2;
		time[m] = t1;
		kind[m++] = 3;
		cin >> t1 >> ch >> t2;
		t1 = t1 * 60 + t2 + turnaround;
		time[m] = t1;
		kind[m++] = 2;
	}
	for (int i = 0; i < nb; i++)
	{
		cin >> t1 >> ch >> t2;
		t1 = t1 * 60 + t2;
		time[m] = t1;
		kind[m++] = 4;
		cin >> t1 >> ch >> t2;
		t1 = t1 * 60 + t2 + turnaround;
		time[m] = t1;
		kind[m++] = 1;
	}
}

void qsort(int l, int r)
{
	if (r - l <= 0) return;
	int i, j;
	i = (l + r) >> 1;
	int midt = time[i];
	int midk = kind[i];
	i = l; j = r;
	while (i < j)
	{
		while ((time[i] < midt) || (time[i] == midt && kind[i] < midk)) i++;
		while ((midt < time[j]) || (time[j] == midt && midk < kind[j])) j--;
		if (i <= j)
		{
			int tmp = time[i];
			time[i] = time[j];
			time[j] = tmp;
			tmp = kind[i];
			kind[i] = kind[j];
			kind[j] = tmp;
			i++;
			j--;
		}
	}
	if (l < j) qsort(l, j);
	if (i < r) qsort(i, r);
}

void solve(int testnumber)
{
	qsort(0, m - 1);
	int ansa, ansb, counta, countb;
	ansa = ansb = counta = countb = 0;
	for (int i = 0; i < m; i++)
	{
		switch (kind[i])
		{
			case 1 : {
						counta++;
						break;
					 }
			case 2: {
						countb++;
						break;
					}
			case 3: {
						if (counta > 0)
							counta--;
						else
							ansa++;
						break;
					}
			case 4: {
						if (countb > 0)
							countb--;
						else 
							ansb++;
						break;
					}
		}
	}
	cout << "Case #" << testnumber << ": " << ansa << ' ' << ansb << endl;
}	

int main()
{
	int n;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}