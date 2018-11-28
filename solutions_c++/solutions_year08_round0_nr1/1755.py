#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string A_FILE_NAME = "A-large";

int fa(const string s[],const int len1, const string q[], int index,const int len2)
{
	bool *m = new bool[len1];
	for(int i=0; i<len1; ++i)
	{
		m[i] = false;
	}
	int cnt = 0;
	for(int i=index; i<len2; ++i)
	{
		for(int j=0; j<len1; ++j)
		{
			if(q[i]==s[j] && !m[j])
			{
				m[j] = true;
				++cnt;
				if(cnt == len1)
				{
					return i;
				}
			}
		}
	}
	return -1;
}

int main()
{
	string FileIn = "D:/" + A_FILE_NAME + ".in";
	string FileOut = "D:/" + A_FILE_NAME + ".out";
	ifstream infile(FileIn.c_str());
	int n;
	infile >> n;

	ofstream outfile(FileOut.c_str());
	for(int i=0; i<n; ++i)
	{
		// get input
		int len1;
		infile >> len1;
		string *s = new string[len1];
		getline(infile, s[0]); //
		for(int j=0; j<len1; ++j)
		{
			getline(infile,s[j]);
		}
		int len2;
		infile >> len2;
		if(len2 == 0)
		{
			outfile << "Case #" << (i+1) << ": " << 0 << endl;
			continue;
		}
		string *q = new string[len2];
		getline(infile, q[0]); //
		for(int j=0; j<len2; ++j)
		{
			getline(infile, q[j]);
		}
		// address input
		int res = -1;
		int index = 0;
		while(true)
		{
			index = fa(s,len1,q,index,len2);
			++res;
			if(index == -1)
			{
				break;
			}
		}
		//
		outfile << "Case #" << (i+1) << ": " << res << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
