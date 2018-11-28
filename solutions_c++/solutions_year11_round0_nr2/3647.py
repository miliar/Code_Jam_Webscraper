#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main()
{
	int numTestCases;
	vector<vector<char> >outputs;
	cin>>numTestCases;
	for(int i=0;i<numTestCases;i++)
	{
		int numCombine,numOpposed,numInvoke;
		char combines[26][26];
		bool opposeds[26][26];
		int invokeNums[26];
		vector<char> invokeList;
		/* init arrays */
		for(int j=0;j<26;j++)
			for(int k=0;k<26;k++)
			{
				combines[j][k] = -1;
				opposeds[j][k] = false;
				invokeNums[k] = 0;
			}
		cin>>numCombine;
		for(int j=0;j<numCombine;j++)
		{
			char x,y,z;
			cin>>x>>y>>z;
			combines[x-'A'][y-'A']=z;
			combines[y-'A'][x-'A']=z;
		}
		cin>>numOpposed;
		for(int j=0;j<numOpposed;j++)
		{
			char x,y;
			cin>>x>>y;
			opposeds[x-'A'][y-'A'] = true;
			opposeds[y-'A'][x-'A'] = true;
		}
		cin>>numInvoke;
		for(int j=0;j<numInvoke;j++)
		{
			char x;
			/*read invoke*/
			cin>>x;
			invokeList.push_back(x);
			invokeNums[x-'A']++;
			/*check combine*/
			int size = invokeList.size();
			if(size<=1) //if size is 1 or 0, continue
				continue;
			char combine = combines[invokeList[size-1]-'A'][invokeList[size-2]-'A'];
			if(combine!=-1)
			{ //we found a combine, make combination
				invokeNums[invokeList.back()-'A']--;
				invokeList.pop_back();
				invokeNums[invokeList.back()-'A']--;
				invokeList.pop_back();
				invokeList.push_back(combine);
				invokeNums[combine-'A']++;
			}
			/*check opposed*/
			size = invokeList.size();
			if(size<=1) //if size is 1 or 0, continue
				continue;
			char lastInvoke = invokeList.back();
			for(int k=0;k<26;k++)
			{
				if(opposeds[lastInvoke-'A'][k]&&invokeNums[k]>0)
				{
					for(unsigned int l=0;l<invokeList.size();l++)
						invokeNums[invokeList[l]-'A']--;
					invokeList.clear();	
				}
			}
		}
		outputs.push_back(invokeList);
	}
	/* output results */
	for(unsigned int i=0;i<outputs.size();i++)
	{
		cout<<"Case #"<<i+1<<": [";
		for(unsigned int j=0,size=outputs[i].size();j<size;j++)
			if(j<size-1)
			 cout<<outputs[i][j]<<", ";
			else
			 cout<<outputs[i][j];
		cout<<"]"<<endl;
	}
}
