#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
#define cin fin


ofstream fout("output.txt");
#define cout fout

int N, P, L, K;

int Compare(const void* a, const void* b)
{
	int x = *(int*)a;
	int y = *(int*)b;
	return y - x;
}

int main()
{
	cin>>N;
	int i, j, jj, k, arr[1010];
	for(i=0; i<N; i++)
	{
		cin>>P>>K>>L;
		for(j=0; j<L; j++)
		{
			cin>>arr[j];
		}
		qsort(arr, L, sizeof(arr[0]), Compare);
		int ret = 0;
		k = 0;
		for(j=0; j<P; j++)
		{
			for(jj=0; jj<K; jj++)
			{
				ret += (j+1) * (arr[k]);
				k++;
				if(k == L)
					break;
			}
			if(k == L)
				break;
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}