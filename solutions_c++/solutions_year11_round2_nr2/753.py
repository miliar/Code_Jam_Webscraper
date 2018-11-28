#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

#define min(a, b) (((a)<(b))?(a):(b))
#define max(a, b) (((a)>(b))?(a):(b))
#define abs(a) ((a)>(0)?(a):(-(a)))

using namespace std;

vector < pair < double, int > > mas;
long double d;
bool mogno(long double tmp)
{
	long double pos = mas[0].first - tmp - d;
	for(int i = 0; i < mas.size(); ++i){
		for(int j = 0; j < mas[i].second; ++j){
			long double temp = abs((pos + d - mas[i].first));
			if (mas[i].first > pos + d){
				long double temp = mas[i].first - (pos + d);
					pos = max(pos + d, mas[i].first - tmp);
			}
			else{
				long double temp = pos + d - mas[i].first;
				if (temp <= tmp + 0.000000001)
					pos += d;
				else
					return false;
			}
		}

	}

	return true;

}

long double search(long double l, long double r)
{
	long double tmp;
	while ((r - l) > 0.0000001){
		tmp = (l / 2) + (r / 2);
		if (mogno(tmp)){
			r = tmp;
		}
		else
			l = tmp;
	}
	return (l / 2) + (r / 2);
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t, n;

	cin >> t;

	for(int ii = 0; ii < t; ++ii){
		cin >> n >> d;
		mas.clear();
		for(int i = 0; i < n; ++i){
			double a;
			int b;
			cin >> a >> b;
			mas.push_back(make_pair(a, b));
		}


		sort(mas.begin(), mas.end());
		long double ans = search(0, 1e12);
		cout << "Case #" << ii + 1 << ':' << ' ' ;
		printf("%.6f\n", ans);
		

	}



	return 0;
}