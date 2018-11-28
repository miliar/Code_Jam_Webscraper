#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

class Snapper
{
public:
	Snapper* next;
	int on, power;
	Snapper();
};

Snapper::Snapper()
{
	on=-1;
	power=-1;
}

void makeChain(int n, Snapper* s)
{
	s->on=-1;
	s->power=1;
	Snapper* current;
	current=s;
	n=n-1;
	for(int a=0; a<n; a++)
	{
		Snapper* x=new Snapper();
		current->next=x;
		current=x;
	}
}
		
int runChain(int n, int k, Snapper* first)
{
	Snapper* current;
	int u=n-1;
	
	for(int a=0; a<k; a++)
	{
		current=first;
		current->power=1;
		current->on*=-1;

		for(int b=0; b<u; b++)
		{	
			current=current->next;
			if(current->power==1)
				current->on*=-1;
			else
				break;
		}
		current=first;
		for(int b=0; b<u; b++)
		{	
			if(current->on==1 && current->power==1)
			{
				current->next->power=1;
			}
			else
				current->next->power=-1;

			current=current->next;
		}
	}

	current=first;
	for(int z=0; z<u; z++)
	{
		current=current->next;
	}

	if(current->on==1 && current->power==1)
		return 1;
	else 
		return 0;
}
		
void main()
{
	string str;
	ifstream file;
	int t;
	vector<string> final;

	file.open("input.txt", ios::in);
	if (!file) 
	{
        cout << "file could not be opened."<< endl;
        exit(1);
    }
	else
	{
		file>>t;
		for(int i=0; i<t; i++)
		{
			int n, k;
			file>>n>>k;
			Snapper* first=new Snapper();
			makeChain(n, first);
			int result=runChain(n, k, first);
			if(result==1)
			{
				string s="ON";
				cout<<s<<endl;
				final.push_back(s);
			}
			else if(result==0)
			{
				string s="OFF";
				cout<<s<<endl;
				final.push_back(s);
			}
		}
		file.close();
		ofstream outfile("result.txt");
		for(int m=0; m<final.size(); m++)
		{
			outfile<<"Case #"<<m+1<<": "<<final[m]<<endl;
		}
		outfile.close();
	}
		


}