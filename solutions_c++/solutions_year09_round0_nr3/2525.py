#include <iostream>
#include <string>  
#include <fstream>

using namespace std;

int search(string srcbuf, string destbuf)
{
	int size1 = srcbuf.size();
	int size2 = destbuf.size();
	int index = 0;

	index = srcbuf.find(destbuf.at(0), 0);
	if(index != -1)
	{
		if(size2 == 1)
		{
			string temp2 = srcbuf.erase(0, index + 1);
			return 1 + search(temp2, destbuf);
		}
		else
		{
			string temp3 = destbuf;
			string temp1 = destbuf.erase(0, 1);
			string temp2 = srcbuf.erase(0, index + 1);
			int k = search(temp2, temp1);
			int p = search(temp2, temp3);
			return k + p;
		}	
	}
	else
	{
		return 0;
	}
}

int main(int argc, char *argv[])
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("C-small-attempt0.out");
	string test = "welcome to code jam";
	string strbuf;

	int N = 0;
	int count = 0;
	infile >> N;
	int n = 1;
	getline(infile, strbuf);
 	while (N-- > 0)
 	{
		count = 0;
		string test = "welcome to code jam";
 		getline(infile, strbuf);
		count = search(strbuf, test);
		if(count > 10000)
		{
			count = count % 10000;
		}
		if(count <1000 && count > 99)
		{
			outfile << "Case #" << n << ": 0" << count <<endl;
		}
		else if(count < 100 && count > 9)
		{
			outfile << "Case #" << n << ": 00" << count <<endl;
		}
		else if(count < 10)
		{
			outfile << "Case #" << n << ": 000" << count <<endl;
		}
		else
		{
			outfile << "Case #" << n << ": " << count <<endl;
		}
		n++;
 	}
	return 0;
}