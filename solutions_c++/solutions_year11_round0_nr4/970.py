#include <fstream>
#include <string>

using namespace std;

int numbers[1000],
	numbers_sorted[1000];
int count;

int compare (const void *a, const void *b)
{
  return ( *(int*)a - *(int*)b );
}

int main (int argc, char* argv[])
{
	ifstream in("D-large.in");
	//ifstream in("D-small-attempt0.in");
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
				in >> numbers[j];
			}
			memcpy(numbers_sorted, numbers, sizeof(int) * count);
			qsort(numbers_sorted, count, sizeof(int), compare);
			int swaps = 0;
			for (int j = 0; j < count; ++j) 
			{
				if (numbers_sorted[j] != numbers[j]) ++swaps;
			}
			out << "Case #" << i + 1 << ": " << swaps << "\n";				
		}
	}

	in.close();
	out.close();
	return 0;
}