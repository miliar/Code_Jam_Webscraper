
#include <iostream>
#include <cstdio>
using namespace std;


void find(const char* start, const char* match, unsigned long& count)
{
	if (*match == 0) {
		count++;
		if (count > 9999) {
			count -= 10000;
		}

		return;
	}


	while (*start != 0) {

		// recursively send off all matches
		if (*match == *start) {
			find(start+1, match+1, count);
		}
		start++;
	}
}



char in[1024];

int main(int argc, char* argv[])
{
	unsigned long cases = 0;
	unsigned long matches = 0;

	cin >> cases;
	cin.getline(in, 1024);

	for (unsigned long i = 0; i < cases; i++) {
		cin.getline(in, 1024);
		matches = 0;
		find(in, "welcome to code jam", matches);
		fprintf(stdout, "Case #%u: %04u\n", i+1, matches);
	}	

	return 0;
}
