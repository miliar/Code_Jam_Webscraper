
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<cassert>

using namespace std;

class Line 
{
	public:
		long long int a;
		long long int b;
};

int main(int argc, char * argv[])
{
	assert(argc == 3);

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	long long int tc_count = 0;
	fin >> tc_count; // test case count;

	// Iterate from 1 to tc_count.
	for(long long int tc_ind = 1; tc_ind <= tc_count; tc_ind++)
	{
		long long int line_count = 0;
		long long int intersect = 0;
		vector<Line> line_list;

		fin >> line_count;
		line_list.reserve(line_count + 1);

		// Iterate from 1 to line_count.
		for(long long int line_ind = 1; line_ind <= line_count; line_ind++)
		{
			fin >> line_list[line_ind].a;
			fin >> line_list[line_ind].b;

			// Compare with existing lines.
			for(long long int i = 1; i <= (line_ind-1); i++)
			{
				if((line_list[i].a < line_list[line_ind].a) && 
				   (line_list[i].b < line_list[line_ind].b))
					continue; // no intersection.

				if((line_list[i].a > line_list[line_ind].a) && 
				   (line_list[i].b > line_list[line_ind].b))
					continue; // no intersection.
				
				intersect++;
			}
		}

		fout << "Case #" << tc_ind << ": " << intersect <<endl;
		intersect = 0;
			
	} // next test case.
	
	fin.close();	
	fout.close();	

	return 0;
}
