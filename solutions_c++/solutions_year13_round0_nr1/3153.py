#include <iostream>
using namespace std;
int main()
{
	int t,i,incomplete=0,j,count=0;
	char check_word,won=0;
	int T;
	char map[5][5];
	cin>>t;
	T=t;
	while(t--)
	{
		cout<<"Case #"<<T-t<<": ";
		incomplete=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>map[i][j];
				if(map[i][j]=='.')
					incomplete=1;
			}
		}
		won=0;
		for(i=0;i<4;i++)
		{
				if(map[i][0]=='T')
					check_word=map[i][1];
				else
					check_word=map[i][0];
				count=0;
				for(j=0;j<4;j++)
				{
					if(check_word==map[i][j] || map[i][j]=='T')
						count++;
				}
				if(count==4)
				{
					won=check_word;
					if(won!='.')
						break;
					else
						won=0;
				}
		}
		if(won==0)
		{
			
				for(i=0;i<4;i++)
				{
					if(map[0][i]=='T')
						check_word=map[1][i];
					else
						check_word=map[0][i];
					count=0;
					for(j=0;j<4;j++)
					{
						if(check_word==map[j][i] || map[j][i]=='T')
							count++;
					}
					if(count==4)
					{
						won=check_word;
						if(won!='.')
							break;
						else
							won=0;
					}
					
				}
			
		}
		if(won==0 && map[0][0]!='.')
		{
			if(map[0][0]=='T')
					check_word=map[1][1];
				else
					check_word=map[0][0];
			count=0;
			for(i=0;i<4;i++)
			{
				if(check_word==map[i][i] || map[i][i]=='T')
						count++;
			}
			if(count==4)
					won=check_word;
			if(won=='.')
					won=0;
		}
		if(won==0 && map[0][3]!='.')
		{
			if(map[0][3]=='T')
					check_word=map[1][2];
				else
					check_word=map[0][3];
			count=0;
			for(i=0;i<4;i++)
			{
				if(check_word==map[i][3-i] || map[i][3-i]=='T')
						count++;
			}
			if(count==4)
					won=check_word;
			if(won=='.')
					won=0;
		}
		if(won==0)
			if(incomplete==1)
				cout<<"Game has not completed"<<endl;
			else
				cout<<"Draw"<<endl;
		else
			cout<<won<<" won"<<endl;

	}
	return 0;
}
