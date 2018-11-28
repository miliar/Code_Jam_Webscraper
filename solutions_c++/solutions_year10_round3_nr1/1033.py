// Codejam2010.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Line
{
public:
	int start, end;
	Line(int pStart=0, int pEnd=0) { start = pStart; end = pEnd; }
	bool isIntersect(const Line & p)
	{
		return ((start - p.start) < 0) != ((end - p.end) < 0);
	}

};

int main(void)
{
	fstream infile, outfile;
	infile.open("A.in", ios_base::in);
	outfile.open("A.out", ios_base::out);

	int T, N, sol;
	
	infile >> T;

	for( int l = 0; l < T; l++)
	{
		infile >> N;
		vector<Line> lines;
		int sol = 0;

		for( int i = 0; i < N; i++)
		{
			int start, end;
			infile >> start >> end;
			lines.push_back( Line( start, end ) );
		}

		for( int j = 0; j < lines.size(); j++ )
		{
			for( int k = j+1; k < lines.size(); k++ )
				if(lines[j].isIntersect(lines[k])) sol++;
		}

		outfile << "Case #" << l+1 << ": " << sol << endl;
	}
	infile.close();
	outfile.close();

	return 0;
}