#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<utility>
#include<fstream>
#include<cassert>
using namespace std;
void fill_table(int k,int N,const vector<int>& groups,map< int,pair<long long,int> >& table)
{
	//printf("\n k=%d, N=%d\n",k,N);
	long long sum=groups[0];
	int running_index=0;
	int counter=1;
	for(size_t i=0;i!=groups.size();i++)
	{
		if(i>0)
		{
			sum=sum-groups[i-1];
		}
		else
		{
			sum=0;
		}
		counter--;
		assert(counter>=0);
		while(sum<=k && counter<N)
		{
			sum+=groups[running_index];
			if(sum>k)
			{
				sum-=groups[running_index];
				break;
			}
			counter++;
			running_index++;
			if(running_index>=N)
			{
				running_index%=N;
			}
		}
		table[i+1]=make_pair(sum,running_index+1);
	}
}

void print_table(map<int, pair<long long,int> >& table)
{
	typedef map<int, pair<long long,int> >::iterator ITER;
	for(ITER it=table.begin();it!=table.end();it++)
	{
		cout<<"\n"<<it->first<<"  "<<it->second.first<<":"<<it->second.second<<endl;
	}
}
	
int main()
{
	//fstream in(argv[1]);
	int test_cases;
	scanf("%d",&test_cases);
	//fstream out("output.txt");
	//while(test_cases--)
	for(int counter=1;counter<=test_cases;counter++)
	{
		int R,k,N;
		map< int,pair<long long,int> > table;
		scanf("%d%d%d",&R,&k,&N);
		//printf("\n R=%d, k=%d, N=%d\n",R,k,N);
		vector<int> groups;
		groups.reserve(1000);
		for(int i=1;i<=N;i++)
		{
			int g;
			scanf("%d",&g);
			groups.push_back(g);
		}
		fill_table(k,N,groups,table);
	//	print_table(table);
		long long money=0;
		int j=1;
		for(int i=1;i<=R;i++)
		{
			money+=table[j].first;
			j=table[j].second;
		}
		//out<<"Case #"<<counter<<": "<<money<<endl;
		//cout<<"Case #"<<counter<<": "<<money<<endl;
		printf("Case #%d: %lld\n",counter,money);
	}
	return 0;
}
