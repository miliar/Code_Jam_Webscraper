#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

bool cmpDepart(pair<int,int> train1, pair<int,int> train2);
bool cmpArrival(pair<int,int> train1, pair<int,int> train2);

int main()
{

	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int n, na, nb, turnround, hour, second, numa=0, numb=0, casenum=0;
	pair<int, int> train;
	vector< pair<int,int> > ta, tb;
	vector< pair<int,int> >::iterator itea,iteb;
	char c;
	cin>>n;
	while(n-- > 0)
	{
		++casenum;
		numa=0;
		numb=0;
		ta.clear();
		tb.clear();

		cin>>turnround;
		cin>>na>>nb;
		while(na-- > 0)
		{
			cin>>hour;
			cin>>c;
			cin>>second;
			train.first=hour*60+second;
			cin>>hour;
			cin>>c;
			cin>>second;
			train.second=hour*60+second+turnround;
			ta.push_back(train);

		}

		while(nb-- > 0)
		{
			cin>>hour;
			cin>>c;
			cin>>second;
			train.first=hour*60+second;
			cin>>hour;
			cin>>c;
			cin>>second;
			train.second=hour*60+second+turnround;
			tb.push_back(train);
			
		}

		sort(tb.begin(),tb.end(),cmpArrival);
		sort(ta.begin(),ta.end(),cmpDepart);
		for(itea = ta.begin(), iteb = tb.begin(); itea!=ta.end(); itea++)
		{
			if(iteb!=tb.end())
			{
				if(itea->first < iteb->second)
				{
					++numa;
				}
				else
				{
					iteb++;
				}
			}
			else
			{
				++numa;
			}
			
		}

		sort(tb.begin(),tb.end(),cmpDepart);
		sort(ta.begin(),ta.end(),cmpArrival);
		for(itea = ta.begin(), iteb = tb.begin(); iteb!=tb.end(); iteb++)
		{
			if(itea!=ta.end())
			{
				if(iteb->first < itea->second)
				{
					++numb;
				}
				else
				{
					itea++;
				}
			}
			else
			{
				++numb;
			}
			
		}

		cout<<"Case #"<<casenum<<": "<<numa<<' '<<numb<<endl;
		
	}
	return 0;
}

bool cmpDepart(pair<int,int> train1, pair<int,int> train2)
{

	return train1.first<train2.first;
}

bool cmpArrival(pair<int,int> train1, pair<int,int> train2)
{
	
	return train1.second<train2.second;
}