/*
Language:C++
*/

#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	ofstream fout("B-large.out");
	ifstream fin("B-large.in");
	
	int t;
	fin>>t;
	
	for(int i=0;i!=t;i++)
	{
		string n;
		fin>>n;
		
		if(n.length()==1)
		{
			fout<<"Case #"<<(i+1)<<": "<<n<<"0"<<endl;
			continue;
		}
		
		int index=-1;
		for(int j=n.length()-1;j!=0;j--)
		{
			int a = (int)(n[j]-'0');
			int b = (int)(n[j-1]-'0');
			if(a>b)
			{
				index=j-1;
				//cout<<n<<","<<a<<","<<b<<endl;
				break;
			}
		}
//cout<<n<<","<<index<<endl;
		vector<int> v;
		for(int j=0;j!=n.length();j++)
		{
			v.push_back(int(n[j]-'0'));
		}
		
		if(index==-1)
		{
			v.insert(v.begin()+1,0);
			index=1;
			
			int index2=0;
			int smallest=v[0];
			for(int j=2;j!=v.size();j++)
			{
				if(v[j]<smallest&&v[j]!=0)
				{
					smallest=v[j];
					index2=j;
				}
			}
			if(index2!=0){
			int tmp=v[0];
			v[0]=v[index2];
			v[index2]=tmp;
			}
		}
		else
		{
			int index2=index+1;
			
			
			int number=v[index2];
			for(int j=index2;j!=v.size();j++)
			{
				if(v[j]<=number&&v[j]>v[index])
				{
					index2=j;
				}
			}
//cout<<n<<","<<v[index]<<","<<v[index2]<<endl;			
			int tmp=v[index];
			v[index]=v[index2];
			v[index2]=tmp;
		}
			//vector<int> v2(v.begin()+index+1,v.end());

		sort(v.begin()+index+1,v.end());
		
		fout<<"Case #"<<(i+1)<<": ";
		for(int j=0;j!=v.size();j++)
		{
			fout<<(char)(v[j]+48);
		}
			
		fout<<endl;
	}
	return 0;
}