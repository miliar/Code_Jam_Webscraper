#include <cstdio>
#include <map>
#include <climits>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


void print(vector<string>& v)
{
	for(int i=0;i<v.size();i++)
	{
		cout<<v[i]<<" ";
	}
	cout<<endl;
}

int distance_to_swap(string s,vector<string>& queries, int index)
{
	
	
	int counter = 0;
	int size = queries.size();
	int j;
	
	
	
	for(j=index;j<size;j++)
	{
	
		
		
		if(queries[j]!=s)
		{
			counter++;
			
		}
		else
		{
			return counter;
			
		}
	}
	return INT_MAX;
	

}

int get_swaps(vector<string>& queries, map<string,int>& m)
{
	map<string,int>::iterator it;
	int d=0;
	
	
	string current;
	int maxcounter=INT_MIN;
	int j=0;
	int swaps = 0;
	int s = queries.size();
	while(j<s)
	{
		maxcounter=INT_MIN;
		for(it = m.begin();it!=m.end();it++)
		{
			
			if(it->first == queries[j])
			{
				continue;
			}
			
			d = distance_to_swap(it->first,queries,j);
			
			if(d>maxcounter)
			{
				maxcounter = d;
				current = it->first;	
			}
		}
		
		
		
		if(maxcounter != INT_MAX)
		{
			swaps++;
			j += maxcounter;
		}
		else
		{
			return swaps;
		}
	}
	
	
	return swaps;
}

int main()
{
	
	freopen("A-large.in","r",stdin);
	//freopen("a.in","r",stdin);
	int n,ss,q;
	scanf("%d ",&n);
	char * str = new char[1000];
	string s;
	map<string,int> m;
	
	
	string current;
	vector<string> queries;
	for(int i=0;i<n;i++)
	{
		
		m.clear();
		queries.clear();
		
		//read search engines
		scanf("%d ",&ss);
		for(int j=0;j<ss;j++)
		{
			
			fgets(str,1000,stdin);
			s = str;
			m[s]=0;
		}
		//read queries
		scanf("%d ",&q);
		
		current = "";
		for(int k=0;k<q;k++)
		{
			
			fgets(str,1000,stdin);
			if( (str!=current)  && (m.find(str)!=m.end()) )
			{
				current = str;
				queries.push_back(str);
			}
		}
		int r = get_swaps(queries,m);
		printf("Case #%d: %d",i+1,r);
		if(i+1<n)printf("\n");
		
	}
	

}

