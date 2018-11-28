#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
FILE * in = fopen("B-large.in", "rt");
FILE * out = fopen("B.out", "wt");
int c, n, k, b, t,i,j,x;
int contor = 0, contor2 = 0, ok;

fscanf(in, "%i", &c);
vector<int> dist;
vector<int> speed;
vector<float> time;
vector<int> swap;
for (i = 0 ; i < c; i++)
{
	ok = 1;
	contor = 0;
	contor2 = 0;
	dist.clear();
	speed.clear();
	time.clear();
	swap.clear();
	fscanf( in, "%i %i %i %i", &n, &k, &b, &t);
	for (j = 0; j < n; j++)
	{
		fscanf(in, "%i", &x);
		dist.push_back(x);
	}

	for (j = 0; j < n; j++)
	{
		fscanf(in, "%i", &x);
		speed.push_back(x);
		swap.push_back(0);
	}
	time.resize(n);
	for (j = 0; j < n; j++)
		time[j] = ((float)(b-dist[j])) / speed[j];
	
	
	j = n-1;
	if (time[j] <= t) contor2++;
	j--;
	while (contor2 < k && j > -1 )
	{
		if (time[j] <= t && time[j] >= time[j+1]) { swap[j] = swap[j+1]; contor+= swap[j+1]; contor2++;}
		else
		if (time[j] <= time[j+1] && time[j+1] <= t) { time[j] = time[j+1]; swap[j] = swap[j+1]; contor += swap[j+1]; contor2++;}
		else
		if (time[j] <= t)
		{
			x = j+1;
			while(x < n && time[x] > t)
			{
				contor++;
				swap[j]++;
				x++;
			}
			if (x < n)
			{contor += swap[x];		
			swap[j] += swap[x];
			time[j] = time[x];
			}
			contor2++;
		}
	

		j--;
	}

		
	if (contor2 < k && ok == 1) ok = 0;
	if (ok == 1) fprintf(out, "Case #%i: %i\n", i+1, contor);
	else if (ok == 0) fprintf(out, "Case #%i: IMPOSSIBLE\n", i+1);
}

fclose(in);
fclose(out);
return 0;
}
