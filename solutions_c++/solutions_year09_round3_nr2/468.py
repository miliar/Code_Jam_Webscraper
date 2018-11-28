#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double x[500];
double y[500];
double z[500];
double vx[500];
double vy[500];
double vz[500];


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	char str[1000];
	gets(str);
	int cases;
	int num = 0;
	int i = 0;
	int j = 0;
	double t = 0.0;
	double d = 0.0;

	for(cases = 0; cases < Cases; cases++)
	{
		double sx = 0.0;
		double sy = 0.0;
		double sz = 0.0;
		double svx = 0.0;
		double svy = 0.0;
		double svz = 0.0;

		scanf("%d", &num);
		for(i = 0; i < num; i++)
		{
			scanf("%lf", &x[i]);
			scanf("%lf", &y[i]);
			scanf("%lf", &z[i]);
			scanf("%lf", &vx[i]);
			scanf("%lf", &vy[i]);
			scanf("%lf", &vz[i]);
		}
		for(j = 0; j < num; j++)
		{
			sx += x[j];
			sy += y[j];
			sz += z[j];
			svx += vx[j];
			svy += vy[j];
			svz += vz[j];
		}
		t = (-1) * (sx * svx + sy * svy + sz * svz) / ( svx * svx + svy * svy + svz * svz);
		if(t < 0.0)
			t = 0.0;
		d = sqrt((pow((sx + svx * t), 2) + pow((sy + svy * t), 2) + pow((sz + svz * t), 2)) / (num * num));
		printf("Case #%d: %.8lf %.8lf\n", cases+1, d, t);
	}
}
//typedef long long int64;

// int main()
// {
// 	freopen("A-large.in", "r", stdin);
// 	freopen("A-large.out", "w", stdout);
// 	int Cases;
// 	scanf("%d", &Cases);
// 	char str[1000];
// 
// 	gets(str);	
// 	int cases;
// 
// 	for(cases = 0; cases < Cases; cases++)
// 	{
// 		gets(str);
// 		string sss = string(str);
// 		if(sss.length()==1)
// 		{
// 			printf("Case #%d: %d\n", cases+1, 1);
// 		}else
// 		{
// 			map<char, int> number;
// 		string s="";
// 		int k,m=2;
// 		number.insert(make_pair(str[0], 1));
// 		s += string(1,str[0]);
// 		for(int f=1; f<1000; f++)
// 		{
// 			if(str[f]!=str[0])
// 				break;
// 		}
// 		number.insert(make_pair(str[f], 0));
// 		s += string(1,str[f]);
// // 		if(str[1]!=str[0])
// // 			number.insert(make_pair(str[1], 0));
// 
// 		for (k=0;str[k];k++)
// 		{
// 			if (s.find(str[k]) == -1)
// 			{
// 				number.insert(make_pair(str[k],m));
// 				m++;
// 				s += string(1,str[k]);
// 			}
// 		}
// 		int len = s.length();
// 		double  res = 0;
// 		for(int i=0;i<k;i++)
// 		{
// 			res += double(number[str[i]] * pow(len, k-i-1)); 
// 		}
// 		printf("Case #%d: %ld\n", cases+1, res);
// 		}
// 
// 	}
// 	return 0;
// }