#include <iostream>
#include <fstream>
#include <queue>
#include <map>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	fstream fp;
	int n, s, q;
	int count;
	queue<int> *order;
	map<string, int> strs;
	string srcheng;
	int i,j;

	fp.open(argv[1], fstream::in);

	fp>>n;

	for (i=0; i<n; ++i)
	{

		fp>>s;
			getline(fp, srcheng);
		for (j=0; j<s; ++j)
		{
			getline(fp, srcheng);
			strs[srcheng] = j;
			
		}
		order = new queue<int>[s];


		fp>>q;
		getline(fp, srcheng);

		for (j = 0; j<q; ++j)
		{
			getline(fp, srcheng);
			order[strs[srcheng]].push(j);
		}

		for (; j<q+s; ++j)
		{
			order[j-q].push(j);
			order[j-q].push(j+s);
		}

		// Main Processing Begins

		int big = -1;
		count = 0;

		while (big < q)
		{
			++count;
			for (j=0; j<s; ++j)
			{
				if (order[j].front() > big)
				{
					big = order[j].front();
				}
			}

			for (j=0; j<s; ++j)
			{
				while (order[j].front() < big)
				{
					order[j].pop();
				}
			}
		}

		cout<<"Case #"<<i+1<<": "<<count-1<<endl;


		// Main Processing Ends

		delete[] order;

	} // i
	fp.close();

	return 0;
}