#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;


int main()
{
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("A-small.out");
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");


	int test;
	cin>>test;

	for(int j=0;j<test;j++)
	{
		vector<char> chars;
		vector<int> moves;
		int num;
		cin>>num;
		char c;
		int button;
		for(int q=0;q<num;q++)
		{
			cin>>c;
			cin>>button;
			if(c=='O')
			{
				chars.push_back('O');
				moves.push_back(button);
			}
			else
			{
				chars.push_back('B');
				moves.push_back(button);
			}
		}

		int ans=0;
		int Orange=1,Blue=1;
		for(int i=0;i<chars.size();i++)
		{
			if(chars[i]=='O')
			{
				while(Orange!=moves[i])
				{
					if(moves[i]>Orange)
						Orange++;
					else if(moves[i]<Orange)
						Orange--;

					int B= find(chars.begin(), chars.end(), 'B')-chars.begin();
					if(B!=chars.end()-chars.begin())
					{
						if(moves[B]>Blue)
							Blue++;
						else if(moves[B]<Blue)
							Blue--;
					}
					ans++;
				}
				
					int B= find(chars.begin(), chars.end(), 'B')-chars.begin();
					if(B!=chars.end()-chars.begin())
					{
						if(moves[B]>Blue)
							Blue++;
						else if(moves[B]<Blue)
							Blue--;
					}
					ans++;

					
				
			}
			else
			{
				while(Blue!=moves[i])
				{
					if(moves[i]>Blue)
						Blue++;
					else if(moves[i]<Blue)
						Blue--;

					int O= find(chars.begin(), chars.end(), 'O')-chars.begin();
					if(O!=chars.end()-chars.begin())
					{
						if(moves[O]>Orange)
							Orange++;
						else if(moves[O]<Orange)
							Orange--;
					}
					ans++;
				}
		
				int O= find(chars.begin(), chars.end(), 'O')-chars.begin();
				if(O!=chars.end()-chars.begin())
				{
					if(moves[O]>Orange)
						Orange++;
					else if(moves[O]<Orange)
						Orange--;
				}
				ans++;
			}

			chars[i]='*';
		}
		cout<<"Case #"<<(j+1)<<": "<<ans<<endl;
		


	}

	//system("pause");
	return 0;
}