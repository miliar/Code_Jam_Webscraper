#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	
	int n;
	//char src[10000],tar[10000],val[10000];
	int s,q;
	string temp;
	vector<string> se,que;
	
	fin>>n;
	for(int c=1; c<=n; c++)
	{
		se.clear();
		que.clear();
		
		fin>>s;
		cout<<s<<"\n";
		fin.ignore();
		for(int i=0;i<s;i++)
		{
			getline(fin,temp);
			se.push_back(temp);
			cout<<temp<<"\n";
		}
		
		fin>>q;
		cout<<q<<"\n";
		fin.ignore();
		for(int i=0;i<q;i++)
		{
			getline(fin,temp);
			que.push_back(temp);
			cout<<temp<<"\n";
		}
		cout<<s<<" "<<q<<"\n";
		vector<string> curr;
		curr=se;
		string last;
		int count=0,flag=0;
		for(int i=0;i<q;i++)
		{
			flag=0;
			for(int j=0;j<curr.size();j++)
			{
				if(curr[j]==que[i])
				{
					flag=1;
					break;
				}
			}
			if(flag)
			{
				if(curr.size()==1)
				{
					last=curr[0];
					count++;
					curr.clear();
					curr=se;
					int k=0;
					for(k=0;k<curr.size();k++)
					{
						if(curr[k]==last)
							break;
					}
					curr.erase(curr.begin()+k);
				}
				else
				{
					int k=0;
					for(k=0;k<curr.size();k++)
					{
						if(curr[k]==que[i])
							break;
					}
					curr.erase(curr.begin()+k);
				}
			}
		}
			
		fout<<"Case #"<<c<<": "<<count<<"\n";
				
			
		

	
	}
	
	return 0;
}

