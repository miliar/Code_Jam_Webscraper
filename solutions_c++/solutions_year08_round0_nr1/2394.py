// qa.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class SearchEng
{
public:
	string name;
	queue<int> seqList;
	SearchEng(string n) : name(n){}

	bool operator==(const SearchEng &other) const {
		return (other.name == name);
	}
};

bool bigger(SearchEng i, SearchEng j) { return i.seqList.front() < j.seqList.front(); }

int main()
{
	int N = 0;
	int S = 0;
	int Q = 0;

	scanf("%d", &N);
	//printf("N: %d\n", N);
	for(int i=0; i<N; i++)
	{
		int changed = 0;
		char temp[101];
		vector<SearchEng> seng;
		vector<string> query;

		scanf("%d", &S);
		//printf("S: %d\n", S);
		gets(temp);
		for(int j=0; j<S; j++)
		{
			gets(temp);
			seng.push_back(SearchEng(temp));
			//printf("\tseng: %s\n", seng.back().name.c_str());
		}

		scanf("%d", &Q);
		//printf("Q: %d\n", Q);
		gets(temp);
		for(int j=0; j<Q; j++)
		{
			gets(temp);
			if((query.size() == 0) || strcmp(temp, query.back().c_str())!=0)
			{
				vector<SearchEng>::iterator it = find (seng.begin(), seng.end(), SearchEng(temp));
				//if(it != seng.end())
				{
					it->seqList.push(j);
					query.push_back(temp);
					//printf("\tquery:%s(%d)\n", query.back().c_str(), j);
				}
			}
		}

		for(vector<SearchEng>::iterator it = seng.begin(); it != seng.end(); it++)
		{
			it->seqList.push(1001);
		}

		int curr = -1;
		vector<SearchEng>::iterator prevIt = seng.end();
		while(true)
		{
			for(vector<SearchEng>::iterator it = seng.begin(); it != seng.end(); it++)
			{
				while((it->seqList.size() > 0) && (it->seqList.front() < curr))
					it->seqList.pop();
			}
 			vector<SearchEng>::iterator it = max_element(seng.begin(),seng.end(), bigger);
			if(prevIt != seng.end())
				prevIt->seqList.pop();
			//printf("Using: %s\n", it->name.c_str());
			curr = it->seqList.front();
			if(curr > 1000)
				break;
			prevIt = it;
			//printf("\tChange: %s(%d)\n", it->name.c_str(), it->seqList.front());
			changed++;
		}

		printf("Case #%d: %d\n", i+1, changed);
	}
	return 0;
}
