#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");

	int T;
	string buf;
	char a[100];
	int len;
	ifs >> T;
	for(int caseNo = 1; caseNo <= T; ++caseNo)
	{
		ifs >> buf;
		len = buf.length();
		strcpy(a, buf.c_str());
		ofs << "Case #" << caseNo << ": ";
		if(next_permutation(a, a + len))
		{
			ofs << a << endl;
		}
		else
		{
			int count = 0;
			for(int i = 0; i <len; ++i)
			{
				if(a[i] == '0')
				{
					++count;
				}
				else break;
			}
			ofs << a[count];
			for(int i = 0; i < count+1; ++i)
				ofs << '0';
			for(int i = count+1; a[i] != 0; ++i)
				ofs << a[i];
			ofs << endl;
		}
	}

	ifs.close();
	ofs.close();
	
	return 0;
}