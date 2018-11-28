#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char **argv)
{
	if (2 != argc)
		return -1;


	ifstream file;

	file.open(argv[1]);
	if (false == file.is_open())
	{
		printf("\nCannot open file\n");
		return -1;
	}
	int i, t;
	int N = 4, K = 47;
	file >> t; i = 0; 
	while(false == file.eof() && i != t ){
		file >> N >> K; i++;
		printf( "Case #%d: %s\n", i, (-1 == ((K%(1<<N)) - (1<<N))) ? "ON" : "OFF");
	}
	file.close();
	return 0;
}