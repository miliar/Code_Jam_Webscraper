#include<vector>
#include<iostream>
#include<string>
using namespace std;

char check(string arr1)
{
	int count =0;int tount =0;
	for(int i=0;i<4;i++)
	{
			if(arr1[i]=='X' || arr1[i]=='T')
				count++;
			if(arr1[i]=='O' || arr1[i]=='T')
				tount++;
	}
	if(tount ==4)
		return 'O';
	if(count ==4)
		return 'X';
	else
		return 'N';
}
char checkdia(vector<string >arr)
{
	int count =0;int tount =0;
	for(int i=0;i<4;i++)
	{
			if(arr[i][i]=='X' || arr[i][i]=='T')
				count++;
			if(arr[i][i]=='O' || arr[i][i]=='T')
				tount++;
	}
	int count1 =0;int tount1 =0;
	for(int i=0;i<4;i++)
	{
			if(arr[i][3-i]=='X' || arr[i][3-i]=='T')
				count1++;
			if(arr[i][3-i]=='O' || arr[i][3-i]=='T')
				tount1++;
	}
	if(tount ==4 ||tount1==4)
		return 'O';
	if(count ==4 ||count1==4)
		return 'X';
	else
		return 'N';
}
bool full(vector<string>arr)
{
		for(int i=0;i<4;i++)
		{
				for(int j=0;j<4;j++)
					if(arr[i][j]=='.')
						return false;
		}
		return true;
}
int main()
{
	int kase=0;
	cin>>kase;
	int first =1;

	while(first<=kase)
	{
		string s;
	getline(cin,s);
		vector<string >arr(4);
		char duplicate[4][4];
			for(int i=0;i<4;i++)
			{
					string temp;
					getline(cin,temp);
					arr[i]=temp;
			}
			
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					duplicate[i][j]=arr[j][i];
			}
			
			bool yet = false;
			char temp = checkdia(arr);
					if(temp =='X')
					{
						cout<<"Case #"<<first<<": "<<"X won"<<endl;yet= true;
					}
					if(temp =='O')
					{
						cout<<"Case #"<<first<<": "<<"O won"<<endl;yet= true;
					
					}
					else
					{
						for(int i=0;i<4 && yet!=true;i++)
						{
								char temp = check(arr[i]);
								char memp = check(duplicate[i]);
								if(temp =='X' || memp == 'X')
								{
									cout<<"Case #"<<first<<": "<<"X won"<<endl;yet= true;
								}
								if(temp =='O' || memp =='O')
								{
									cout<<"Case #"<<first<<": "<<"O won"<<endl;yet= true;
								}
						}
					}
					if(full(arr) && yet == false)
						cout<<"Case #"<<first<<": "<<"Draw"<<endl;
					else if(yet ==false)
					cout<<"Case #"<<first<<": "<<"Game has not completed"<<endl;
			first++;
	}
	return 0;
}