#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	FILE* f=fopen(argv[1],"r");

	int cases;
	fscanf(f,"%u\n",&cases);
	for(int i=0;i<cases;i++)
	{
		vector<int> v1;
		vector<int> v2;
		int n;
		fscanf(f,"%u\n",&n);
		for(int j=0;j<n;j++)
		{
			int a;
			fscanf(f,"%u",&a);
			v1.push_back(a);
		}
		for(int j=0;j<n;j++)
		{
			int a;
			fscanf(f,"%u",&a);
			v2.push_back(a);
		}
		if(n!=0)
		{
			sort(v1.begin(),v1.end());
			sort(v2.begin(),v2.end());
		}
		int ret=0;
		for(int j=0;j<n;j++)
		{
			ret+=(v1[j]*v2[n-j-1]);
		}
		printf("Case #%u: %i\n",i+1,ret);
	}

	fclose(f);
}
