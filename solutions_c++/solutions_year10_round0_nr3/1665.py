#include <cstdio>
#include <vector>
using namespace std;
vector<int> head;
vector<int> g;
vector<int> t;
int check()
{
	int l = t.size()-1;

	for(int i=0;i<l;i++)
	{
		if(head[i]==head[l] && t[i]==t[l])
		{
			return i;
		}
	}
	return -1;
}
int main()
{
	long long sum, tt;
	int test, temp, ck;
	int r, k, n, i, j;
	FILE* inf = fopen("input.txt","r");
	FILE* outf = fopen("output","w");

	fscanf(inf, "%d", &test);
	for(i=0;i<test;i++)
	{
		head.clear();
		g.clear();
		t.clear();
		fscanf(inf, "%d %d %d", &r, &k, &n);

		for(j=0;j<n;j++)
		{
			fscanf(inf, "%d", &temp);
			g.push_back(temp);			
		}
		j=1; sum =g[0];
		head.push_back(0);
		for(;;)
		{
			if(j%n == head.back())
			{
				t.push_back(sum);
				head.push_back(j%n);
				t.push_back(sum);
				ck = check();
				break;	
			}
			if(sum + g[j%n] <= k)
			{
				sum += g[j%n];	
			}
			else
			{
				t.push_back(sum);
				ck = check();
				if(ck >= 0)
					break;
				sum = g[j%n];
				head.push_back(j%n);
			}
			j++;
		}
		sum = 0;
		for(j=0;j<ck;j++)
		{
			r--;
			sum += t[j];
		}
		tt=0;
		for(j=ck;j<t.size()-1;j++)
		{
			tt += t[j];	
		}
		sum += tt*(r/(t.size()-1 -ck));
		for(j=ck;j< ck + (r % ((t.size()-1)-ck));j++)
		{
			sum += t[j];
		}
		fprintf(outf, "Case #%d: %lld\n", i+1, sum);
	}

	fclose(inf);
	fclose(outf);
	return 0;
}
