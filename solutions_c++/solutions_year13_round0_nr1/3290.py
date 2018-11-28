#include<iostream>

#define FOR(i,n) for(i=0;i<n;i++)
using namespace std;

int i,j,n,t,temp=1;
char a[10][10];

int getWin(char c)
{
	int i,chk=0;
	// horizontal check
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if((a[i][j]==c)||(a[i][j]=='T'))
				continue;
			else
				break;
		}
		if(j==4)
			return 1;
	}

	// vertical check
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if((a[j][i]==c)||(a[j][i]=='T'))
				continue;
			else
				break;
		}
		if(j==4)
			return 1;
	}

	//diagonal check
	for(i=0;i<4;i++)
	{
		if((a[i][i]==c)||(a[i][i]=='T'))
			continue;
		else
			break;
	}
	if(i==4)
		return 1;

	//reverse diagonal check
	for(i=0;i<4;i++)
	{
		if((a[i][3-i]==c)||(a[i][3-i]=='T'))
			continue;
		else
			break;
	}
	if(i==4)
		return 1;
    return 0;
}

int getGameNotCompleted()
{
	int i;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(a[i][j]=='.')
				return 1;
	return 0;
}

int main()
{
	cin>>t;
	while(t--)
	{
		FOR(i,4)
			cin>>a[i];
		if(getWin('X'))
			cout<<"Case #"<<temp++<<": X won";
		else if(getWin('O'))
			cout<<"Case #"<<temp++<<": O won";
		else if(getGameNotCompleted())
			cout<<"Case #"<<temp++<<": Game has not completed";
		else
			cout<<"Case #"<<temp++<<": Draw";
                if(t!=0)
                        cout<<endl;
	}
	return 0;
}
