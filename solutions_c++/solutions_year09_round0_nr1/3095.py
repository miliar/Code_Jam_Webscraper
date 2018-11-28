#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

main()
{
	int L,D,N;
	vector<string> dict;
	string str;
	vector< vector<int> > truth;
	vector<int> temp(26,0);
	char ch='a';

	cin >> L>>D>>N;
	for(int i=0;i<D;i++)
	{
		cin >> str;
		dict.push_back(str);
	}
	cin.get(ch);

	for(int i=0;i<L;i++)truth.push_back(temp);


	for(int i=0;i<N;i++)
	{
		int count=0;
		while(1)
		{
			cin.get(ch);
			if(ch=='\n')break;
			else if(ch >='a' && ch<='z')
			{
				truth[count++][ch-'a']=1;
				
			}
			else if(ch=='(')
			{
				while(1)
				{
					cin >> ch;

					if(ch!=')')truth[count][ch-'a']=1;
					else 
					{
						count++;break;
					}
				}
			}
		}
		count=0;	
		for(int j=0;j<D;j++)
		{
			int flag=1;
			for(int k=0;k<L;k++)
			{
				if(truth[k][dict[j][k]-'a']!=1)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)count++;
		}
		
		cout<<"Case #"<<i+1<<": ";
		cout<<count<<'\n';	
		for(int k=0;k<L;k++)for(int j=0;j<26;j++)truth[k][j]=0;
			

	}

}
		
