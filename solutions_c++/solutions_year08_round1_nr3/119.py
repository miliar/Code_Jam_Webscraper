#include<iostream>
#include<cmath>

using namespace std;

int t, n;

struct Mat
{
	int a1, a2, a3, a4;
} m1, m2, res;

Mat mul(Mat a, Mat b)
{
	Mat temp;
	temp.a1 = (a.a1 * b.a1 + a.a2 * b.a3) % 1000;
	temp.a2 = (a.a1 * b.a2 + a.a2 * b.a4) % 1000;
	temp.a3 = (a.a3 * b.a1 + a.a4 * b.a3) % 1000;
	temp.a4 = (a.a3 * b.a2 + a.a4 * b.a4) % 1000;
	if (temp.a1 < 0) temp.a1 += 1000;
	if (temp.a2 < 0) temp.a2 += 1000;
	if (temp.a3 < 0) temp.a3 += 1000;
	if (temp.a4 < 0) temp.a4 += 1000;
	//printf("%d %d %d %d\n", temp.a1, temp.a2, temp.a3, temp.a4);
	return temp;
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	int i;
	scanf("%d", &t);
	int caseID = 1;
	while (t--)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d", &n);
		m1.a1 = 28;
		m1.a2 = 6;
		m1.a3 = 6;
		m1.a4 = 2;
		m2.a1 = 6;
		m2.a2 = 1;
		m2.a3 = -4;
		m2.a4 = 0;
		res.a1 = 1;
		res.a2 = 0;
		res.a3 = 0;
		res.a4 = 1;
		n--;
		while (n != 0)
		{
			if (n & 1) res = mul(res, m2);
			m2 = mul(m2, m2);
			n >>= 1;
		}
		m1 = mul(m1, res);
		printf("%03d\n", m1.a2 - 1);
	}
	return 0;
}