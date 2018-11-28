
#include <iostream>
#include <string>
using namespace std;

#define MAX 50

string combine[MAX];
string opposed[MAX];
string list;
int t,c,d,n;


void init()
{
	list.clear();
	for(int i=0;i<MAX;i++)
	{
		combine[i].clear();
		opposed[i].clear();
	}
}


char isCom(char end ,char ch)
{
	for(int i=0;i<c;i++)
	{
		if((combine[i][0]==end && combine[i][1]==ch) ||
		   (combine[i][1]==end && combine[i][0]==ch))
			return combine[i][2];
	}
	return ' ';
}

int isOpp(char ch)
{
	for(int i=0;i<list.length();i++)
	{
		for(int j=0;j<d;j++)
		{
			if((list[i] == opposed[j][0] && opposed[j][1]==ch)||
			   (list[i] == opposed[j][1] && opposed[j][0]==ch))
				return 1;
		}
	}
	return 0;
}

void invoke(char ch)
{
	if(list.length()>0)
	{
		char end=list[list.length()-1];
		char com=isCom(end,ch);
		if(com!=' ')
		{
			list[list.length()-1]=com;
		}
		else
		{
			if(isOpp(ch)==1)
			{
				list.clear();
			}
			else
				list += ch;
		}
	}
	else
		list += ch;
}


int main()
{
	freopen("l.in","r",stdin);
	freopen("l.out","w",stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		init();
		cin>>c;
		for(int j=0;j<c;j++)
			cin>>combine[j];
		cin>>d;
		for(int j=0;j<d;j++)
			cin>>opposed[j];
		char ch;
		cin>>n;
		getchar();
		for(int j=0;j<n;j++)
		{
			ch=getchar();
			invoke(ch);
		}
	
		if(list.length()!=0)
		{
				cout<<"Case #"<<i+1<<": ["; 
			int k;
			for(k=0;k<list.length()-1;k++)
			{
				cout<<list[k]<<", ";
			} 			
			cout<<list[k]<<"]"<<endl;
		}
		else
			cout<<"Case #"<<i+1<<": []"<<endl; 	
	}
	
	return 0;
}
