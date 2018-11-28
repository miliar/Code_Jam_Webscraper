#include <iostream>
#include <fstream>


using namespace std;

int cas, index=1;
ifstream fin("B-small-attempt1.in");
ofstream fout("B-small-attempt1.out");

const int SIZE = 1002;
long long l, t, n, c;
int arr[SIZE];
int load[SIZE];

void read()
{
	fin >> l >> t >> n >> c;

	for (int i=0; i < c; i ++  )
	{
		fin >> arr[i];
	}

	for (int i=0; i< n; i ++)
	{
		load[i] = arr[i%c];
	}
}

long long cal0()
{
	long long sum = 0;
	for (int i=0; i < n; i ++)
	{
		sum += load[i];
	}
	return sum * 2;
}

long long cal1(int s)
{
	long long sum = 0;
	for (int i=0; i < s; i ++)
	{
		sum += load[i];
	}

	sum *= 2;

	if (sum >= t)
	{
		sum += load[s];
	}
	else if (t - sum < load[s] * 2)
	{
		sum =  t + load[s] - (t - sum)/2;
	}
	else
	{
		sum += load[s] * 2;
	}

	for (int i=s+1; i < n; i ++)
	{
		sum += load[i] * 2;
	}

	return sum;
}

long long cal2(int x, int y)
{
	long long sum = 0;

	for (int i=0; i < x; i ++)
	{
		sum += load[i];
	}
	sum *= 2;

	if (sum >= t)
	{
		sum += load[x];
	}
	else if (t - sum < load[x] * 2)
	{
		sum =  t + load[x] - (t - sum)/2;
	}
	else
	{
		sum += load[x] * 2;
	}

	for (int i= x+1; i < y; i ++)
	{
		sum += load[i] * 2;
	}

	if (sum >= t)
	{
		sum += load[y];
	}
	else if (t - sum < load[y] * 2)
	{
		sum =  t + load[y] - (t - sum)/2;
	}
	else
	{
		sum += load[y] * 2;
	}
	
	for (int i= y +1; i <n ;i ++)
	{
		sum += load[i] * 2;
	}

	return sum;
}

long long cal()
{
	long long result = 0x7fffffffffffffff;
	if(l == 0)
	{
		return cal0();
	}

	if (l == 1)
	{
		result = cal0();
		for (int i=0; i < n; i ++)
		{
			long long temp = cal1(i);
			if (result > temp)
			{
				result = temp;
			}
		}
		return result;
	}

	if (l == 2)
	{
		for (int i=0; i < n; i ++)
		{
			for (int j=i+1; j < n; j ++)
			{
				long long temp = cal2(i, j );
				if (result > temp)
				{
					result = temp;
				}//				
			}//
		}//
		return result;
	}
}

int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();		
		long long result = cal();
		fout << "Case #"<<index<<": " << result<<endl;
		index ++;
	}

	return 0;
}
