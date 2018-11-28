#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string cal(vector<string> base,vector<string> opposite,string test,int n);

int main()
{
	
	ifstream fin("..\\B-large.in");
	ofstream fout("..\\B-large.out");

	int testNum;
	fin>>testNum;
	for(int i=1;i<=testNum;i++)
	{
		int c,d,n;
		fin>>c;
		vector<string> base;
		for(int j=0;j<c;j++)
		{
			string temp;
			fin>>temp;
			base.push_back(temp);
		}
		fin>>d;
		vector<string> opposite;
		for(int j=0;j<d;j++)
		{
			string temp;
			fin>>temp;
			opposite.push_back(temp);
		}
		fin>>n;
		string test;
		fin>>test;
		
		string r=cal(base,opposite,test,n);
		cout<<"Case #"<<i<<": [";
		fout<<"Case #"<<i<<": [";
		if(r.size()==0 || r=="")
		{
			cout<<"]"<<endl;
			fout<<"]"<<endl;
		}
		else
		{
			for(int j=0;j<r.size();j++)
			{
				cout<<r[j];
				fout<<r[j];
				if(j!=r.size()-1)
				{
					cout<<", ";
					fout<<", ";
				}
			}

			cout<<"]"<<endl;
			fout<<"]"<<endl;
		}
	}

	return 0;
}

string cal(vector<string> base,vector<string> opposite,string test,int n)
{
	string result="";
	int resultSize=0;
	for(int i=0;i<n;i++)
	{
		result=result+test[i];
		resultSize++;
		bool isCombine=false;
		if(result.size()<=1)
			continue;
		for(int j=0;j<base.size();j++)
		{
			//cout<<(int)( (result[resultSize-2]=base[j][0] && result[resultSize-1]==base[j][1]) )<<endl;
			if((result[resultSize-1]==base[j][0] && result[resultSize-2]==base[j][1]) || (result[resultSize-2]==base[j][0] && result[resultSize-1]==base[j][1]))
			{
				result[resultSize-2]=base[j][2];
				result.erase(result.end());
				string temp="";
				for(int k=0;k<resultSize-1;k++)
					temp=temp+result[k];
				result=temp;
				isCombine=true;
				resultSize--;
				break;
			}
		}
		if(isCombine)
			continue;

		for(int j=0;j<opposite.size();j++)
		{
			string temp=opposite[j];
			for(int m=0;m<result.size();m++)
			{
				for(int n=m+1;n<result.size();n++)
				{
					if((result[m]==temp[0] && result[n]==temp[1]) || (result[n]==temp[0] && result[m]==temp[1]))
					{
						result="";
						resultSize=0;
					}
				}
			}
		}
	}

	return result;
}