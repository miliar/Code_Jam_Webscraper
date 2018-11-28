#include<iostream>
#include<stdio.h>
#include<list>
#define MAXC 1
#define MAXD 1
#define MAXN 10
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int c;
		char combine[MAXC][4];
		int d;
		char opp[MAXD][3];
		int n;
		char inv;
		cin>>c;
		for(int j=0;j<c;j++)
			cin>>combine[j];
		cin>>d;
		for(int j=0;j<d;j++)
			cin>>opp[j];
		cin>>n;
		list<char> e;	//element list
		getc(stdin);
		while(n>0)
		{
			//read a char to invoke
			inv=getc(stdin);
			n--;
			//get the last element in list
			char last=e.back();
			//see if they combine
			int j;
			for(j=0;j<c;j++)
			{
				if((combine[j][0]==inv && combine[j][1]==last) || (combine[j][1]==inv && combine[j][0]==last))
				{
					e.pop_back();
					e.push_back(combine[j][2]);
					break;
				}
			}
			//else see if inv is opposed by someone
			if(j==c)
			{
				for(j=0;j<d;j++)
				{
					bool oppflag=false;
					if(opp[j][0]==inv)
					{
						list<char>::iterator it;
						for(it=e.begin();it!=e.end();++it)
						{
							if(*it==opp[j][1])
							{
								e.clear();
								oppflag=true;
								break;
							}
						}
							
					}
					else if(opp[j][1]==inv)
					{
						list<char>::iterator it;
						for(it=e.begin();it!=e.end();++it)
						{
							if(*it==opp[j][0])
							{
								e.clear();
								oppflag=true;
								break;
							}
						}
					}
					if(oppflag)
						break;
				}
				if(j==d)
					e.push_back(inv);
			}
		}
		cout<<"Case #"<<i<<": [";
		do
		{
			if(!e.empty())
			{
				cout<<e.front();
				e.pop_front();
			}
			if(!e.empty())
				cout<<", ";
			else
				cout<<"]\n";
		}while(!e.empty());
	}
}
