#include <fstream>
#include <string>

using namespace std;

int candies[1000];
int count;

long long n;
int pd, pg;

bool isPossible()
{
	if (pg == 100)
		if (pd == 100) return true;
		else return false;
	if (!pg && !pd) return true;
	else if (!pg) return false;
	if (n >= 100) return true;
	else {
		for (int i = 1; i <= n; ++i)
		{
			double value = (double) i * pd / 100;
			if (!(floor(value) - value)) return true; 
		}
	}
	return false;
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
			in >> n >> pd >> pg;
			if (isPossible()) 
			{
				out << "Case #" << i + 1 << ": " << "Possible\n";
			} else {
				out << "Case #" << i + 1 << ": " << "Broken\n";
			}
		}
	}

	in.close();
	out.close();
	return 0;
}