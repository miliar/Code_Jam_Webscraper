#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> filter(vector<string> dict,int n,string mask)
{
	int i=0,j=0;
	vector<string> ret;
	for (i=0;i<dict.size();i++)
	{
		for (j=0;j<mask.size();j++)
			if ((dict[i])[n]==mask[j])
				ret.push_back(dict[i]);
	}
	return ret;
}

int main()
{
	unsigned int L=0, D=0, N=0, i=0,j=0,k=0;
	string temp="", mask="";
	vector<string> dict, tempdict, gooddict;
	cin >> L >> D >> N;
	for (i=0;i<D;i++)
	{
		cin >> temp;
		dict.push_back(temp);
	}
	for (i=0;i<N;i++)
	{
		cin >> temp;
		k=0;
		tempdict = dict;
		for (j=0;j<L;j++)
		{
			mask="";
			if (temp[k]=='(')
			{
				for (k++;temp[k]!=')';k++)
					mask+=temp[k];
			}
			else
				mask=temp[k];
			tempdict = filter(tempdict,j,mask);
			k++;
		}
		cout << "Case #" << i+1 << ": " << tempdict.size() << "\n";
	}
}

