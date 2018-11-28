#include <fstream>
#include <string>
#include <list>

using namespace std;

int r,c;
char pics[51][51];
	
bool check()
{
	for (int i=0; i < r - 1;++i)
	{
		for (int j = 0; j < c - 1;)
		{
			if (pics[i][j] == '.' ||pics[i][j] == '\\' ||pics[i][j] == '/') j++;
			else if (pics[i][j] == '#' && pics[i+ 1][j] == '#' &&
				pics[i][j+1] == '#' && pics[i+ 1][j+1] == '#')
			{
				pics[i][j] = '/';
				pics[i+ 1][j] = '\\';
				pics[i][j+1] = '\\';
				pics[i+ 1][j+1] = '/';
				j+=2;
			} else return false;
		}
	}

	for (int i = 0; i < r; ++i)
		if (pics[i][c -1] == '#') return false;
	for (int i = 0; i < c; ++i)
		if (pics[r -1][i] == '#') return false;
	return true;
}

int main (int argc, char* argv[])
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	if (in.is_open() && out.is_open())
	{
		int case_count;
		in >> case_count;
		for (int i = 0; i < case_count; ++i)
		{
			in >> r >> c;
			for (int i = 0; i < r; ++i)
				in >> pics[i];
			out << "Case #" << i + 1 << ":\n";
			if (check()) {
				for (int i = 0; i < r; ++i)
					out << pics[i] << "\n";
			} else 
			{
				out << "Impossible\n";
			}
		}
	}

	in.close();
	out.close();
	return 0;
}