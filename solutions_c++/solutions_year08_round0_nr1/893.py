#include <iostream>
#include <string>
#include <vector>
#include "omp.h"
using namespace std;

vector<string> query;
vector<string> searchs;
vector<int> scores;
int casenum=1;


int count(int pos,int cursearchs)
{
    if(pos==query.size())
      return 0;
    if(query[pos]==searchs[cursearchs])
    {
        int min=INT_MAX;
        for(int i=0;i<searchs.size();i++)
        {
			
            if(query[pos]==searchs[i])
              continue;
            int temp=count(pos+1,i);
            if(min>temp+1)
            {
               min=temp+1;
            }
        }
		
            return min;
    }else
    {
       return count(pos+1,cursearchs);
    }
    
}

int ta()
{
	query.clear();
	searchs.clear();
	scores.clear();
    int temp=0;
	cin>>temp;
    string stemp;
		getline(cin,stemp);
    for(int i=0;i<temp;i++)
    {
		getline(cin,stemp);
     searchs.push_back(stemp);
    }
    cin>>temp;
		getline(cin,stemp);
    for(int i=0;i<temp;i++)
    {
		getline(cin,stemp);
     query.push_back(stemp);
    }
	int minpos=0;
	if(query.size()!=0)
	{
	for(int i=0;i<searchs.size();i++)
		scores.push_back(0);
	string current=query[0];
	for(int i=0;i<query.size();i++)
	{
		int j,itemp;
		for(j=0;j<searchs.size();j++)
		{
			if(query[i]==searchs[j])
			{
				scores[j]=1;
				itemp=j;
				break;
			}
		}
		for(j=0;j<scores.size();j++)
		{
			if(scores[j]==0)
				break;
		}
		if(j==scores.size())
		{
			minpos++;
			for(j=0;j<scores.size();j++)
				scores[j]=0;
			scores[itemp]=1;
		}

	}
	}
	cout<<"Case #"<<casenum++<<": "<<minpos<<endl;

		return 1;
}

int main()
{
	int test;
	cin>>test;
	for(int i=0;i<test;i++)
		ta();
	return 0;
}
