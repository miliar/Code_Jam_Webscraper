#include <fstream>
#include <string>

using namespace std;

int candies[1000];
int count;

bool isPossible()
{
	int result = 0;
	for (int i = 0; i < count; ++i)
		result ^= candies[i];
	return !result;
}

int main (int argc, char* argv[])
{
	ifstream in("C-large.in");
	//ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	if (in.is_open() && out.is_open())
	{
		int case_count;
		in >> case_count;
		for (int i = 0; i < case_count; ++i)
		{
			in >> count;
			for (int j = 0; j < count; ++j)
			{
				in >> candies[j];
			}
			if (isPossible()) 
			{
				int minimum = candies[0],
					sum = minimum;
				for (int j = 1; j < count; ++j) {
					minimum = min(minimum, candies[j]);
					sum += candies[j];
				}
				out << "Case #" << i + 1 << ": " << sum - minimum << "\n";
			} else {
				out << "Case #" << i + 1 << ": " << "NO\n";
			}
			
			
			//for(int i = 0; i < spell.length(); ++i) {			
			//	out << spell[i];
			//	if (i < spell.length() - 1) out << ", "; 
			//}
			//out	<< "]\n";
		}
	}

	in.close();
	out.close();
	return 0;
}