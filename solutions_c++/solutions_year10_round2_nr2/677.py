#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

void iter(int ind)
{
   	int n,k,b,t;
	cin >> n >> k >> b >> t;

	vector<int> x,v;
	
	for(int i=0; i<n; ++i)
	{
		int tmp; cin >> tmp; x.push_back(tmp);
	}

	for(int i=0; i<n; ++i)
	{
		int tmp; cin >> tmp; v.push_back(tmp);
	}

	int x1,x2,v1,v2;

	vector<int> stops;
	stops.resize(n,0);
	for(int i=0; i<n; ++i)
		if ((b-x[i]) > t*v[i])
			stops[i] = 1;

	vector<int> cnt;
	cnt.resize(n,0);
	for(int i=0; i<n; ++i)
		if (stops[i])
			cnt[i] = -1;

	for(int i=0; i<n; ++i)
	{
		if (stops[i]) continue;
		
		for(int j=i+1; j<n; ++j)
		{
			if (stops[j])
				cnt[i]++;
		}
	}

	sort(cnt.begin(),cnt.end());
/*
	for(int i=0; i<n; ++i)
		cerr << cnt[i] << " ";
	cerr << endl;
*/
	int sum=0, count=0;
	for(int i=0; i<n && count!=k; ++i)
	{
		if (cnt[i]==-1) continue;
		sum += cnt[i];
		count++;
	}
	
	cout << "Case #" << ind << ": ";
	if (count==k)
		cout << sum;
	else 
		cout << "IMPOSSIBLE";
	cout << endl;	

}

int main()
{
	int c;
	cin >> c;

	for(int i=0; i<c; ++i)
		iter(i+1);

	return 0;
}
