#include "iostream"
#include "fstream"
#include "string"

using namespace std;

bool iscorrect(string str, int r)
{
	for(int i=r+1; i<str.length(); i++)
	{
		if(str[i] == '1')
			return false;
	}
	return true;
}
int numzero(string str)
{
	int count = 0;
	int c = 0;
	for(int i=str.length()-1; i>=0; i--)
	{
		if(str[i] == '1')
		{
			c = i;
			break;
		}
	}
	for(int i=c; i<str.length(); i++)
	{
		if(str[i] == '0')
			count++;
	}
	return count;
}
int findsmallest(string* str, int N, int r)
{
	int m = r;
	int am = numzero(str[r]);
	for(int i=r+1; i<N; i++)
	{
		int ai;
		ai = numzero(str[i]);
		if(ai > am)
		{
			m = i;
			am = ai;
			if(iscorrect(str[i], r))
				break;
		}
	}
	return m;
}
void swap(string* str, int row1, int row2)
{
	for(int i=row2; i>row1; i--)
	{
		string tmp = str[i];
		str[i] = str[i-1];
		str[i-1] = tmp;
	}
}

void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int T;
	infile >> T;
	for(int i=0; i<T; i++)
	{
		int N;
		infile >> N;
		infile.get();
		char* line = new char[N+1];
		string* str = new string[N];
		int count = 0;
		for(int j=0; j<N; j++)
		{
			infile.getline(line, 50);
			str[j] = line;
		}
		for(int j=0; j<N; j++)
		{
			int row1 = j;
			int row2 = -1;
			if(!iscorrect(str[j], j))
			{
				row2 = findsmallest(str, N, j);
				count += row2 - row1;
				swap(str, row1, row2);
			}
		}
		/*for(int j=0; j<N; j++)
		{
			if(!iscorrect(str[j], j))
				cout << "Problem " << i << endl;
		}*/
		outfile << "Case #" << i+1 << ": " << count << endl;
	}

	infile.close();
	outfile.close();
}