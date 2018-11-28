#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const string in_fname="A-small-attempt0.in";
const string out_fname="a-large-out.txt";

void AssignFiles()
{
	freopen(in_fname.c_str(),"r",stdin);
	freopen(out_fname.c_str(),"w",stdout);
}

void CloseFiles()
{
	fclose(stdin);
	fclose(stdout);
}

typedef short int sint;

typedef sint key[20];

key phone[20];

int p,k,l;

vector<int> letters;

int main()
{
	AssignFiles();

	int NumCases;
	cin>>NumCases;
	for(int Case=1;Case<=NumCases;Case++)
	{
		string Shunt;
		letters.clear();
		cin>>p>>k>>l;

		for(int i=0;i<l;i++)
		{
			int buf;
			cin>>buf;
			letters.push_back(buf);
		}

		sort(letters.begin(),letters.end());

		int curPos, curDepth;
		curPos=0;
		curDepth=1;
		int res;
		res=0;
		for(int i=l-1;i>=0;--i)
		{
			curPos++;
			if(curPos>k)
			{
				curPos=1;
				curDepth++;
			}
			res+=letters[i]*(curDepth);
		}

		cout<<"Case #"<<Case<<": "<<res<<"\n";
	}

	CloseFiles();
	return 0;
}
