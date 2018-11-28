#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class line
{
	public:
		int m_y1, m_y2;	
		
	public:
		line(int y1, int y2)
		{
			m_y1 = y1;
			m_y2 = y2;
		}
		
		~line()
		{
		
		}
};

int main(int argc, char ** argv)
{
	ifstream fin("A-large.in");// A-small-attempt2.in
	ofstream fout("A-large.out");// A
	
	int T;
	fin >> T;
	
	for (int i = 1; i <= T; i++)
	{
		int N;
		fin >> N;
		
		vector<line *> lines;
		
		for (int j = 0; j < N; j++)
		{
			int y1 = 0, y2 = 0;
			
			fin >> y1 >> y2;
			
			lines.push_back(new line(y1, y2));	
		}
		
		int n = 0;
		
		vector<line *>::iterator ite_i = lines.begin(), ite_j = lines.begin();
		for (; ite_i != lines.end(); ite_i++)
		{
			for (ite_j = ite_i + (vector<line *>::difference_type)1; ite_j != lines.end(); ite_j++)
			{
				int diff_i = (*ite_i)->m_y2 - (*ite_i)->m_y1,
				    diff_j = (*ite_j)->m_y2 - (*ite_j)->m_y1,
					diff_ij = (*ite_i)->m_y1 - (*ite_j)->m_y1;
				    
				if ((diff_j - diff_i) != 0)
				{
					double k = (double)diff_ij / (double)(diff_j - diff_i);
					
					if ( k > 0.0 && k < 1.0)
					{
						n++;
					}
				}
			}
		}
		
	
		fout << "Case #" << i << ": "  << n << endl; 	
	}
	
	return 0;	
}
