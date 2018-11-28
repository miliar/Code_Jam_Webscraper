#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int case_num;
	//ifstream ifile("A-small-attempt1.in");
	//ofstream ofile("A-small-attempt1.out");
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");
	//ifstream ifile("q.txt");
	//ofstream ofile("a.txt");
	ifile >> case_num;
	for(int ii=0;ii<case_num;++ii)
	{
		int r, c;
		ifile >> r >> c;
		vector< vector<char> > pictures;
		for(int i=0;i<r;++i)
		{
			vector<char> vtmp;
			for(int j=0;j<c;++j)
			{
				char tmp;
				ifile >> tmp;
				vtmp.push_back(tmp);
			}
			pictures.push_back(vtmp);
		}

		for(int i=0;i<r-1;++i)
		{
			for(int j=0;j<c-1;++j)
			{
				if(pictures[i][j] == '#')
				{
					if(pictures[i][j+1] != '#' || pictures[i+1][j] != '#' || pictures[i+1][j+1] != '#')
						goto impossible;
					pictures[i][j] = '/';
					pictures[i][j+1] = '\\';
					pictures[i+1][j] = '\\';
					pictures[i+1][j+1] = '/';
				}
			}
		}
		for(int i=0;i<c;++i)
			if(pictures[r-1][i] == '#')
				goto impossible;
		for(int i=0;i<r-1;++i)
			if(pictures[i][c-1] == '#')
				goto impossible;
		ofile << "Case #" << ii+1 << ":\n";
		for(int i=0;i<r;++i)
		{
			for(int j=0;j<c;++j)
				ofile << pictures[i][j];
			ofile << endl;
		}
		continue;
impossible:
		ofile << "Case #" << ii+1 << ":\nImpossible\n";
	}
	ifile.close();
	ofile.close();
	system("pause");
	return 0;
}

