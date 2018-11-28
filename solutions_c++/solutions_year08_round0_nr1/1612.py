
#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int RunTest(ifstream &in)
{
	int s, q;
	map<string, int> used;
	int free = 0;
	int c = 0;
	
	in >> s;
	in.get();
	for(int i = 0; i < s; i++)
	{
		char buf[101];
		in.getline(buf, 101);
		//cout << "e: " << buf << endl;
		used[buf] = 0;
		free++;
	}

	in >> q;
	in.get();

	for(int i = 0; i < q; i++)
	{
		char buf[101];
		in.getline(buf, 101);		

		if(!used.find(buf)->second)
			free--;
		

		//cout << "q: " << buf << " used: " << free <<  endl;

		if(!free)
		{
			c++;
			free = used.size() - 1;
			for(map<string, int>::iterator it = used.begin(); it != used.end(); it++)
				it->second = 0;
		}
		used[buf] = 1;
	}
	


	return c;
}

int main(int argc, char* argv[])
{
	if(argc != 2)	cout << "specify input file";
	ifstream in(argv[1]);

	int n;
	in >> n;

	for(int i = 0; i < n; i++)
		cout << "Case #" << (i + 1) << ": " << RunTest(in) << endl;

	return 0;
}

