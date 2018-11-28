#include <vector>
#include <cstdio>
#include <map>

using namespace std;

vector<int> Qs;
map<pair<int,int>, int> cache;

int free(int from, int to)
{
	if(cache.find(make_pair(from,to))!=cache.end())
		return cache[make_pair(from,to)];
	
	int res = 0;
	if(from <= to)
	{
		int min=-1;
		for(int i=0; i<Qs.size(); i++) {
			if(Qs[i]<from || Qs[i]>to)
				continue;
			int tmp = (to-from) + free(from,Qs[i]-1) + free(Qs[i]+1,to);
			if(min==-1 || tmp<min)
				min=tmp;
		}
		if(min==-1)
			res = 0;
		else
			res = min;
	}

	cache[make_pair(from,to)] = res;
	//printf("-- [%d %d] : %d\n",from,to,res);
	return res;
}


int main()
{
	FILE *f = fopen("in.txt","r");
	int tests;
	fscanf(f,"%d",&tests);
	for(int test=1; test<=tests; test++) {
		int P,Q;
		Qs.clear();
		cache.clear();
		fscanf(f,"%d%d",&P,&Q);
		for(int i=0; i<Q; i++) {
			int q;
			fscanf(f,"%d",&q);
			Qs.push_back(q);
		}

		int res = free(1,P);
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
