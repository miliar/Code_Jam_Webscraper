#include <sstream>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

void put_into_vector( ifstream& ifs, vector<int>& v )
{
  string s;
  getline( ifs, s );
  istringstream iss( s );
  copy( istream_iterator<int>( iss ), istream_iterator<int>(), back_inserter( v ) );
}

int main()
{
  
  ifstream ifs("input.txt");
  ofstream ofs("output.txt");

  string line;
  getline(ifs, line);
  istringstream ss(line);
  int cases;
  ss >> cases;
  
  for(int i = 0; i < cases; i++)
  {
	int res = 0;
	getline(ifs, line);
	istringstream ss2(line);
	int count, p, sup;
	ss2 >> count;
	ss2 >> sup;
	ss2 >> p;
	for(int j = 0; j < count; j++)
	{
		int sum;
		ss2 >> sum;
		int rem = sum % 3;
		int x = sum / 3;
		if(0 == rem)
		{
			if(x >= p)
			{
				++res;
				continue;
			}
			if((x+1 >= p) && (x <= 9) && (x >= 1) && (x < 10) && (sup > 0))
			{
				++res;
				--sup;
				continue;
			}
		}
		else if (1 == rem)
		{
			if((x+1 >= p) && (x >= 0) && (x <= 9))
			{
				++res;
				continue;
			}
		}
		else	// rem = 2
		{
			if((x >= 0) && (x <= 9) && (x+1 >= p) && (x < 10))
			{
				++res;
				continue;
			}
			if((x+2 >= p) && (x >= 0) && (x <= 8) && (sup > 0))
			{
				++res;
				--sup;
				continue;
			}
		}
	}
	ofs <<  "Case #" << i+1 << ": " << res << endl;
  }

  

}