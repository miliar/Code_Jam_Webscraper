//////////////////////////////////////////////////////////////////////////
// Correct for small and large testsets
//////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

string tmpl = "welcome to code jam";
string text;
int num = 0;

void findchar(int start, int idx)
{
	if(idx == tmpl.length())	//found 
	{
		num++;
		return;
	}

	if(start == text.length())
		return;	//not found

	for(int i=start; i<text.length(); i++)
	{
		if(text[i]==tmpl[idx])
		{
			findchar(i+1, idx+1);	//find next
		}
	}
}


int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream out("output.txt");
	int N;
	int start=0, idx=0;
	cin>>N;
	cin.ignore();
	for(int i=1; i<=N; i++)
	{	
		getline(cin, text);
		num = 0;
		if(text.length() < 19)
		{
			out<<"Case #"<<i<<": 0000"<<endl;
			continue;
		}
		
		findchar(0,0);
		num = num%10000;

		int zeronum = 0;
		if(num < 10)
			zeronum = 3;
		else if(num < 100)
			zeronum = 2;
		else if(num < 1000)
			zeronum = 1;
		
		out<<"Case #"<<i<<": ";
		for(int i=0; i<zeronum; i++)
			out<<0;
		out<<num<<endl;
	}

	return 0;
}