#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> queries;
vector<string> searches;

int _find(vector<string> q, unsigned int begin,string pattern)
{
	unsigned int p;

	for(p=begin;p<q.size();p++)
	{
	 if(q[p] == pattern)
		 return p;
	}
	return -1;

}



int get_switch(vector<string> s, vector<string>q)
{
	int j=0 ;
	unsigned int pos;
	int loc=0;
	unsigned int begin=0;
	//unsigned int g;
	int help;
	for(begin=0;begin<q.size();)
	{
		for(pos =0; pos < s.size();pos++)
		{
			help = _find(q,begin,s[pos]);
			if(help==-1)
				return j;
			if(loc<help)
				loc=help;
		}

		j++;
		begin =loc;
	}

	return j;
	
}


int main()
{
	int N;
	int S;
	int Q;
	char  temp[105] ;
	int i;
	int k;
	int result;
	scanf("%d",&N);

	for(k=0;k<N;k++)
	{
		searches.clear();
		queries.clear();
		scanf("%d",&S);
		gets(temp);
		for(i=0;i<S;i++)
		{
			gets(temp);
			searches.push_back((string)temp);
		}
		scanf("%d",&Q);
		gets(temp);
		for(i=0;i<Q;i++)
		{
			gets(temp);
			queries.push_back(temp);
		}

		result = get_switch(searches,queries);
		printf("Case #%d: %d\n",k+1,result);
		
	}


	return 0;
}