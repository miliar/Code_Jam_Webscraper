#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

class customer_t
{
	public:
		customer_t()
		: needmalted(false), satisfied(false)
		{}
		bool needmalted;
		bool satisfied;
		vector<int> malted;
		vector<int> regular;
		bool operator < (const customer_t & rhs) const
		{
			if( (!malted.empty()) && (!rhs.malted.empty()))
			{
				return regular.size() < rhs.regular.size();
			}
			if( (malted.empty()) && (rhs.malted.empty()))
			{
				return regular.size() < rhs.regular.size();
			}
			if(rhs.malted.empty())
			{
				return 1;
			}
			return 0;
		}
};

ostream & operator << (ostream & out,customer_t & rhs)
{
	out << rhs.malted.size() << ", " << rhs.regular.size();
	return out;
}

void clearcusts(vector<customer_t> & custs,int malted);
bool matchup(vector<int> & choices,vector<int> & regular);

int main()
{
	int num;
	cin >> num;
	for(int i=0;i<num;i++)
	{
		int flavors;
		cin >> flavors;
		int numcust;
		cin >> numcust;
		vector<customer_t> custs(numcust);
		for(int j=0;j<numcust;j++)
		{
			int likes;
			cin >> likes;
			for(int k=0;k<likes;k++)
			{
				int flavor,malted;
				cin >> flavor >> malted;
				flavor--;
				if(malted)
				{
					custs[j].needmalted=1;
					custs[j].malted.push_back(flavor);
				}
				else
				{
					custs[j].regular.push_back(flavor);
				}

			}
		}
		sort(custs.begin(),custs.end());
#ifdef DEBUG
		for(int j=0;j<custs.size();j++)
		{
			cout << j << ": " << custs[j] << endl;
		}
#endif
		vector<int> choices(flavors,0);

		for(int j=0;j<custs.size();j++)
		{
			if(!custs[j].malted.empty())
			{	//Need a malted
				if(custs[j].regular.empty())
				{
					//must be given a malted drink
					choices[custs[j].malted[0]]=1;
					//This customer is satisifed, now clear the remainder of the customer list
#ifdef DEBUG
					cout << "Selected malted: " << custs[j].malted[0] << endl;
#endif
					clearcusts(custs,custs[j].malted[0]);

					//start over, 
					j=-1;
				}
			}
		}

		//No malted should be left
#ifdef DEBUG
		for(int j=0;j<custs.size();j++)
		{
			cout << j << ": " << custs[j] << endl;
		}
#endif
		bool fail = false;
		for(int j=0;j<custs.size();j++)
		{
			if(!matchup(choices,custs[j].regular))
			{
				fail=true;
				j = custs.size();
			}
		}


		cout << "Case #" << i+1 << ": ";
		if(fail)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			for(int j=0;j<choices.size();j++)
			{
				cout << choices[j] << " ";
			}
		}
		cout << endl;
	}
	return 0;
}


void clearcusts(vector<customer_t> & custs,int malted)
{
	vector<customer_t>::iterator it = custs.begin();
	while(it!=custs.end())
	{
		if((*it).malted.size()>0)
		{
			//has a malted need
			if((*it).malted[0] == malted)
			{
				it = custs.erase(it);
				continue;
			}
		}

		//Can't be regular now
		for(int j=0;j<(*it).regular.size();j++)
		{
			if((*it).regular[j]==malted)
			{
				(*it).regular.erase((*it).regular.begin()+j);
				j = (*it).regular.size();
			}
		}

		it++;
	}
}

bool matchup(vector<int> & choices,vector<int> & regular)
{
	for(int i=0;i<regular.size();i++)
	{

		if(choices[regular[i]]==0)
		{
			return true;
		}
	}
	return false;
}
