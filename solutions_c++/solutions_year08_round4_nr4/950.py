#include<iostream>
#include<vector>
#include<string>

using namespace std;

main()
{
	int cases,k,min=5000;
	string str,back;

	cin >> cases;

	for(int l=0;l<cases;l++)
	{
		cin >> k;
		cin >> str;
		min=5000;

		vector<int> v;
		for(int i=0;i<k;i++)v.push_back(i);

		do
		{
			int len=str.length();
			back.clear();
			for(int i=0;i<len/k;i++)
			{
				for(int j=0;j<k;j++)
				{

					back+=str[i*k + v[j]];

				}
			}
			int count=1;
			for(int i=1;i<len;i++)
			{
				if(back[i] != back[i-1]) count++;
			}
			if(count<min) min=count;



		}
		while((next_permutation(v.begin(),v.end())!=0));

		cout<<"Case #"<<l+1<<": "<<min<<'\n';
	}
}


