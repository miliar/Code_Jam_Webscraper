#include <iostream>
#include <vector>
using namespace std;

int T,C,D,N;
bool opp[256][256];
char comb[256][256];
char str[256];



vector<char> exe;
void execute()
{
	for(int i=0;i<N;i++)
	{
		char curr = str[i];
		
		if(exe.size()>0 && comb[exe.back()][curr] != 0)
		{
			char last = exe.back();
			exe.pop_back();
			exe.push_back(comb[last][curr]);
		}
		else
		{
			exe.push_back(curr);
		}

		for(int j=0;j + 1 <exe.size();j++)
		{
			if(opp[exe[j]][exe.back()])
			{
				exe.clear();
			}
		}
	}
}

void display(int test)
{
	cout<<"Case #"<<test<<": [";
	for(int i=0;i<exe.size();i++)
	{
		cout<<exe[i];
		if(i+1<exe.size())
		{
			cout<<", ";
		}
	}
	cout<<"]"<<endl;
}

char tmp[5];
void solve(int test)
{
	memset(comb,0,sizeof(comb));
	memset(opp,0,sizeof(opp));
	memset(str,0,sizeof(str));
	exe.clear();

	cin>>C;
	
	for(int i=1;i<=C;i++)
	{
		cin>>tmp;
		comb[tmp[0]][tmp[1]] = tmp[2];
		comb[tmp[1]][tmp[0]] = tmp[2];
	}
	
	cin>>D;
	for(int i=1;i<=D;i++)
	{
		cin>>tmp;
		opp[tmp[0]][tmp[1]] = true;
		opp[tmp[1]][tmp[0]] = true;
	}

	cin>>N;
	cin>>str;

	execute();

	display(test);
}

int main()
{
	cin>>T;

	for(int t=1;t<=T;t++)
	{
		solve(t);
	}
}