#include <iostream>
#include <cstdlib>
#include <cstdio>

#define T 128

using namespace std;

class Time
{
	public:
	int ini, fim;

	Time(void) { ini = fim = 0; };
	void SetIni(int h, int min) { ini = HMtoOM(h, min); };
	void SetFim(int h, int min) { fim = HMtoOM(h, min); };
	int HMtoOM(int h, int min);
};

int Time::HMtoOM(int h, int min)
{
	return 60*h + min;
}

int cmp1(const void *t1, const void *t2)
{
	return ((Time *)t1)->ini - ((Time *)t2)->ini;
}

int cmp2(const void *t1, const void *t2)
{
	return ((Time *)t1)->fim - ((Time *)t2)->fim;
}

int main(void)
{
	int x, n;
	int t;
	int i, j;
	int na, nb;
	int resA, resB;
	int h, min;
	Time a[T], b[T];

	cin >> n;
	for(x = 1; x <= n; x++)
	{
		resB = 0;
		cin >> t;
		cin >> na >> nb;
		for(i = 0; i < na; i++)
		{
			//cin >> h >> ":" >> min;
			scanf("%d:%d", &h, &min);
			a[i].SetIni(h, min);

			//cin >> h >> ":" >> min;
			scanf("%d:%d", &h, &min);
			a[i].SetFim(h, min + t);
		}

		for(i = 0; i < nb; i++)
		{
			//cin >> h >> min;
			scanf("%d:%d", &h, &min);
			b[i].SetIni(h, min);

			//cin >> h >> min;
			scanf("%d:%d", &h, &min);
			b[i].SetFim(h, min + t);
		}

		/*for(i = 0; i < na; i++)
		{
			cout << a[i].ini << " " << a[i].fim << endl;
		}

		for(i = 0; i < nb; i++)
		{
			cout << b[i].ini << " " << b[i].fim << endl;
		}*/

		qsort(a, na, sizeof(Time), cmp1);
		qsort(b, nb, sizeof(Time), cmp2);

		/*for(i = 0; i < na; i++)
		{
			cout << a[i].ini << " " << a[i].fim << endl;
		}

		for(i = 0; i < nb; i++)
		{
			cout << b[i].ini << " " << b[i].fim << endl;
		}*/

		resA = na;
		for(i = j = 0; i < na && j < nb && resA > 0; i++)
		{
			if(a[i].ini >= b[j].fim)
			{
				//cout << "!";
				resA--;
				j++;
			}
		}
		
		qsort(a, na, sizeof(Time), cmp2);
		qsort(b, nb, sizeof(Time), cmp1);

		resB = nb;
		for(i = j = 0; i < nb && j < na && resB > 0; i++)
		{
			if(b[i].ini >= a[j].fim)
			{
				//cout << "@";
				resB--;
				j++;
			}
		}
		
		cout << "Case #" << x << ": " << resA << " " << resB << endl;
	}

	return 0;
}

