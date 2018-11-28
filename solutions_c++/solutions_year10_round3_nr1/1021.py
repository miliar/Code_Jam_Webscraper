#include <iostream>
#include <cstdlib>

using namespace std;

const int MAXN = 1000;

class NUMBER
{
	public:
		int a,b;
}nums[MAXN+1];


int cmp(const void *a,const void *b)
{
	int left = ((const NUMBER *)a)->a;
	int right = ((const NUMBER *)b)->a;
	return left-right;
}

int t,n;
int main()
{
	cin >> t;
	for (int kk = 1; kk <= t;kk++)
	{
		cin >> n;
		for (int i = 1; i<= n;i++)
			cin >> nums[i-1].a >> nums[i-1].b;
		for (int i=0;i<n;i++)
			for (int j=i+1;j<n;j++)
				if (nums[i].a > nums[j].a) swap(nums[i],nums[j]);
		int count = 0;
		for (int i=0;i<n;i++)
			for (int j=i+1;j<n;j++)
			{
				if (nums[i].b > nums[j].b) count++;
			}
		cout << "Case #" << kk << ": " << count << endl;
	}
}
