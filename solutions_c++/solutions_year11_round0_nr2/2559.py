#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.txt","w",stdout);
	vector<int> result;
	int cases,T,C,D,N,i,counter;
	int oppose[128],combine[128][128];
	int appear[128];
	char str[102];
	cin>>T;
	for(cases=1;cases<=T;cases++)
	{
		result.clear();
		memset(combine,0,sizeof(combine));
		memset(oppose,0,sizeof(oppose));
		cin>>C;
		for(i=0;i<C;i++)
		{
			cin>>str;
			combine[str[0]][str[1]]=str[2];
			combine[str[1]][str[0]]=str[2];
		}
		cin>>D;
		for(i=0;i<D;i++)
		{
			cin>>str;
			oppose[str[0]]=str[1];
			oppose[str[1]]=str[0];
		}
		memset(appear,0,sizeof(appear));
		cin>>N;
		cin>>str;
		appear[str[0]]++;
		result.push_back(str[0]);
		for(i=1;i<N;i++)
		{
			if(result.size() && combine[str[i]][result.back()])
			{
				counter--;
				appear[str[i-1]]--;
				result.pop_back();
				result.push_back(combine[str[i]][str[i-1]]);
			}
			else
			{
				if(appear[oppose[str[i]]])
				{
					memset(appear,0,sizeof(appear));
					result.clear();
					counter=0;
				}
				else
				{
					counter++;
					appear[str[i]]++;
					result.push_back(str[i]);
				}
			}
		}
		char output;
		if(result.size()==0)
		{
			cout<<"Case #"<<cases<<": []\n";
		}
		else
		{
			output=result[0];
			cout<<"Case #"<<cases<<": [";
			cout<<output;
			for(i=1;i<result.size();i++)
			{
				output=result[i];
				cout<<", "<<output;
			}
			cout<<"]\n";
		}
	}
	return 0;
}
