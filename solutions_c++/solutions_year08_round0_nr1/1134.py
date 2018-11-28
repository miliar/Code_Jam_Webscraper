#include <fstream>
#include <ctime>

using namespace std;

int main()
{
	ofstream out("linear.in");
	
	srand(time(0));
	
	int n = rand() % 18 + 3;
	out << n << endl;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= n; j++)
			out << rand()%100 << ' ';
		out << endl;
	}
}
