#include <stdio.h>
#include <hash_map.h>
#include <vector>


using namespace std;



struct eqstr
{
  bool operator()(char* s1, char* s2) const
  {
    return strcmp(s1, s2) == 0;
  }
};

typedef hash_map<char*,int,hash<char*>, eqstr> hashtype;
int bin_search(vector<int> &vec, int query)
{
	int low = 0;
	int high = vec.size()-1;
	int mid = (low+high)/2;
	while(low<=high)
	{
		if(vec[mid] == query)
			return mid;
		else if (vec[mid] > query)
			high = mid-1;
		else
			low = mid+1;
		mid = (low+high)/2;
	}
	return mid;
}
int main()
{
	int N;
	scanf("%d\n", &N);
	int caseno = 0;
	while(N--)
	{
		caseno++;
		int S,Q;
		scanf("%d\n",&S);
		vector<int> indices[120];
		char buff[1024];
		hashtype h;
		for(int counter=0; counter<S; counter++)
		{
			gets(buff);
//			printf("I got |%s|\n",buff);
			h[buff] = counter;
		}
		scanf("%d\n",&Q);
		for(int counter=0; counter<Q; counter++)
		{
			gets(buff);
//			printf("I got |%s|\n",buff);
			indices[h[buff]].push_back(counter);
		}
		for(int counter=0; counter<S; counter++)
		{
			indices[counter].push_back(5000);//higher than largest query possible
		}

		int start_ind = -1;
		int start_val = -1;
		for(int counter=0; counter<S; counter++)
		{
			if(indices[counter][0]>start_val)
			{
				start_val = indices[counter][0];
				start_ind = counter;
			}
		}
		if(start_val >=Q)
		{
			printf("Case #%d: 0\n",caseno);
			continue;
		}
		int switches = 1;
		int next_ind,next_val;
		
		while(1)
		{
			//printf("start_val %d start_ind %d\n",start_val, start_ind);
			next_ind = -1;
			next_val = -1;
			for(int counter=0; counter<S; counter++)
			{
				if(counter!=start_ind)
				{
					int ret = bin_search(indices[counter],start_val);
					if(next_val < indices[counter][ret+1])
					{
						next_val = indices[counter][ret+1];
						next_ind = counter;
					}
				}
			}
			if(next_val >=Q)
			{
				printf("Case #%d: %d\n",caseno,switches);
				break;
			}
			start_ind = next_ind;
			start_val = next_val;
			switches++;
		}

	}
	return 0;
}
