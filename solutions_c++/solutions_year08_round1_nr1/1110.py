#include "iostream"
#include "fstream"
using namespace std;
#include "vector"
#include "algorithm"

void swap(long &a, long&b)
{
	int tmp=a;
	a=b;
	b=tmp;
}
long calc(int n)
{
	long res=1;
	for(int i=2; i<=n; i++)
		res*=i;
	return res;
}
void permute(vector <long> &v)
{
	int n=v.size();
	int i=n-2;
	while(i>0 && v[i]>v[i+1])
		i--;
	if(i>=0)
	{
		int k=n-1;
		while(v[k]<v[i])
			k--;
		swap(v[k], v[i]);
		int a=i+1, b=n-1;
		while(a<b)
		{
			swap(v[a], v[b]);
			a++;
			b--;
		}
	}
}

int greater(long a, long b)
{
	return a>b;
}
int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("Input.txt");
	outfile.open("Output.txt");
	int T, n;
	vector <long> v1, v2;
	infile>>T;
	for(int i=0; i<T; i++)
	{
		v1.clear();
		v2.clear();
		infile>>n;
		long sum=0;
		long minsum=INT_MAX;
		for(int j=0; j<n; j++)
		{
			int tmp;
			infile>>tmp;
			v1.push_back(tmp);
		}
		for(int j=0; j<n; j++)
		{
			int tmp;
			infile>>tmp;
			v2.push_back(tmp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end(), greater);
//		long s=calc(n);
//		for(long j=0; j<n; j++)
//		{
//			sum=0;
			for(int k=0; k<n; k++)
			{
				sum+=v1[k] * v2[k];
			}
			if(sum<minsum)
					minsum=sum;
//			if(j<s-1)
//				permute(v1);
//		}
		outfile<<"Case #"<<i+1<<": "<<minsum<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}