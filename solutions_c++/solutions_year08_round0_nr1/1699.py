#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <set>
#include <iostream>
using namespace std;



int main()
{

int N;

fstream In("A-large.in", ios::in);

fstream Out("A-large.out", ios::out);

int i, j;

In >> N;

for(int h=1; h<=N; h++)
{	
	Out << "Case #" << h << ": ";

	map<string, int> queries;

	int S, Q;

	In >> S;
	string temp;
	getline(In, temp);
	
		
	for(i=0; i<S; i++)
	{
		getline(In, temp);		
		
	}


	In >> Q;
	getline(In, temp);
	int ret = 0;
	int cur = S;

	for(i=0; i<Q; i++)
	{
		getline(In, temp);
		if(queries[temp]==ret)
		{
			queries[temp]++;
			cur--;
			if(!cur)
			{
				ret++;
				queries[temp]++;
				cur = S-1;
			}
		}
	}
	Out << ret << endl;

}

In.close();
Out.close();

return 0;

}