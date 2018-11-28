#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& a, int from, int mid, int to)
{
	int n = to - from +1;
	vector<int> b(n);
	int i1 = from;
	int i2 = mid + 1;
	int j = 0;
	while (i1 <= mid && i2 <= to) 
	{
		if (a[i1] > a[i2])
		{
			b[j] = a[i1];
			i1++;
		}
		else
		{
			b[j] = a[i2];
			i2++;
		}
		j++;
	}
	while (i1 <= mid)
	{
		b[j] = a[i1];
		i1++;
		j++;
	}
	while (i2 <= to)
	{
		b[j] = a[i2];
		i2++;
		j++;
	}
	for (j=0;j<n;j++)
		a[from + j] = b[j];
}

void merge_sort(vector<int>& a, int from, int to)
{
	if (from == to) 
		return ;
	int mid = (from + to) / 2;
	merge_sort(a, from, mid);
	merge_sort(a, mid + 1, to);
	merge(a, from, mid, to);
}

int minkeypress(vector<int>& v, int P, int K, int L)
{
	merge_sort(v, 0, v.size() - 1);
	int sum = 0;
	for (int i=0;i<v.size();i++)
		sum +=  (i + K) / K * v[i];
	return sum;
}


int main()
{
	int N, P, K, L;
	cin>>N;
	int i, j;
	for (i=0;i<N;i++)
	{
		cin>>P>>K>>L;
		vector<int> v(L);
		for (j=0;j<L;j++) 
			cin>>v[j];
		cout<<"Case #"<<i+1<<": "<<minkeypress(v, P, K, L)<<endl;
	}
	return 0;
}