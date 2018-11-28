#include <iostream>
#include <string>
using namespace std;

const int MAXN = 200;

inline int toMinute(string timeStr)
{
	int h, m;
	sscanf(timeStr.c_str(), "%d:%d", &h, &m);
	return h*60+m;
}

struct TrainData
{
	int minute, city;
	bool isArr;

	TrainData(int iminute = 0, int icity = 0, bool iisArr = false):minute(iminute), city(icity), isArr(iisArr){};
};

int nOfTest;
int nOfA, nOfB, n, T;
TrainData data[MAXN*2];
int cnt[2];

inline int cmp(const void *a, const void *b)
{
	TrainData ra = *(TrainData*)a, rb = *(TrainData*)b;
	int res =  ra.minute-rb.minute;
	if (res == 0)
		res = -(ra.isArr-rb.isArr);
	return res;
}

void read()
{
	cin >> T;
	cin >> nOfA >> nOfB;
	n = 0;
	string temp;
	for(int i=0; i<nOfA; i++)
	{
		cin >> temp;
		data[n++] = TrainData(toMinute(temp), 0, false);
		cin >> temp;
		data[n++] = TrainData(toMinute(temp)+T, 1, true);
	}
	for(int i=0; i<nOfB; i++)
	{
		cin >> temp;
		data[n++] = TrainData(toMinute(temp), 1, false);
		cin >> temp;
		data[n++] = TrainData(toMinute(temp)+T, 0, true);
	}

	qsort(data, n, sizeof(TrainData), cmp);
}

void work()
{
	read();
	cnt[0] = cnt[1] = 0;
	int ans[2] = {0, 0};
	for(int i=0; i<n; i++)
		if (data[i].isArr)
			cnt[data[i].city]++;
		else if (cnt[data[i].city])
			cnt[data[i].city]--;
		else
			ans[data[i].city]++;
	cout << ans[0] << ' ' << ans[1] << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
