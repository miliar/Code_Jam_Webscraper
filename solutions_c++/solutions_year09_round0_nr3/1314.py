#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int N;
	cin >> N;
	cin.ignore(1);

	string target = "welcome to code jam";

	for(int i=0;i<N;i++)
	{
		string temp;
		getline(cin,temp);
		int poss = 0;

		string letters = " acdejlmotw";
		for(int j=0;j<temp.size();j++)
		{
			if(letters.find(temp[j])==string::npos)
			{
				temp.erase(temp.begin()+j);
				j--;
			}
		}

		while(!temp.empty() && temp[0]!='w')
		{
			temp.erase(temp.begin());
		}
		while(!temp.empty() && *(temp.end()-1)!='m')
		{
			temp.erase(temp.end()-1);
		}

//		cout << "Case: " << i+1 << ": " << temp << endl;

		if(temp.size() < target.size())
		{
			cout << "Case #" << i+1 << ": 0000" << endl;
			continue;
		}

		vector<vector<int> > dp(target.size(),vector<int>(temp.size(),0));
		for(int j=0;j<temp.size();j++)
		{
			if(target[0] == temp[j])
			{
				dp[0][j] = 1;
			}
		}
		for(int j=1;j<target.size();j++)
		{
			for(int k=0;k<temp.size();k++)
			{
				if(target[j] == temp[k])
				{
					for(int m=0;m<k;m++)
					{
						if(target[j-1] == temp[m])
						{
							dp[j][k]+=dp[j-1][m];
							dp[j][k]%=10000;
						}
					}
				}
			}
		}

		for(int j=0;j<temp.size();j++)
		{
			poss+=dp.back()[j];
		}
		poss %= 10000;

//		cout << temp << "\t";
		cout << "Case #" << i+1 << ": ";
		if(poss<1000)
		{
			cout << "0";
		}
		if(poss<100)
		{
			cout << "0";
		}
		if(poss<10)
		{
			cout << "0";
		}
		cout << poss << endl;
	}
	return 0;
}
