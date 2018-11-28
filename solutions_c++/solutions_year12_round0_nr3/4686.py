#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>

#define DEB(x) std::cerr<<"TaChIdOk: "<<#x<<":("<<x<<")"<<std::endl

using namespace std;

void getDigits(unsigned number, string &digits);
void checkRecycled(unsigned n, unsigned m, string &ns, string &ms, std::set<std::pair<unsigned, unsigned> > &recycled);

int main(int argc, char *argv[])
 {

	unsigned n_test_cases;
	scanf("%d", &n_test_cases);
//	DEB(n_test_cases);
	getchar();

	FILE *output;
	output = fopen("output.txt", "w");

	for (unsigned i = 0; i < n_test_cases; i++)
 	{

		unsigned A, B;
		scanf("%d %d", &A, &B);

//		DEB(A);
//		DEB(B);
		getchar();

		std::set<std::pair<unsigned, unsigned> > recycled_pairs;
		recycled_pairs.clear();
		for (unsigned n = A; n < B; n++)
		{
			string ns;
			ns.clear();
			getDigits(n, ns);
			for (unsigned m = n + 1; m <= B; m++)
			{
				string ms;
				ms.clear();
				getDigits(m, ms);
				checkRecycled(n, m, ns, ms, recycled_pairs);

			}

		}

		unsigned recycled = recycled_pairs.size();
/*
		std::set<std::pair<unsigned, unsigned> >::iterator it;

		for (it = recycled_pairs.begin(); it != recycled_pairs.end(); it++)	{
			DEB((*it).first);
			DEB((*it).second);
		}

		DEB(B - A);
	*/
		fprintf(output, "Case #%d: %d\n", i+1, recycled);

	}

	fclose(output);

	return 1;

 }

void getDigits(unsigned number, string &digits) {

	char c;

//	DEB(number);

	unsigned count = 0;
	while (number > 0) {

		unsigned digit = number%10;
		sprintf(&c, "%d", digit);
		digits.append(&c);
	        number /= 10;
		count++;

	}

	std::reverse(digits.begin(), digits.end());
/*
	for (unsigned hh = 0; hh < digits.size(); hh++)
		DEB(digits[hh]);
*/
}

void checkRecycled(unsigned n, unsigned m, string &ns, string &ms, std::set<std::pair<unsigned, unsigned> > &recycled) 
{

	unsigned size_ns = ns.size();
	unsigned size_ms = ms.size();

	if (size_ns != size_ms)
		return;

	string tmp_ns;
	tmp_ns.resize(size_ns);

	for (unsigned i = 0; i < size_ns; i++)
		tmp_ns[i] = ns[i];

	// Create all possible permutations from ns
	for (unsigned j = 0; j < size_ns-1; j++) {
		char tmp_c;
		tmp_c = tmp_ns[0];
		for (unsigned i = 0; i < size_ns-1; i++)
		{
			tmp_ns[i] = tmp_ns[i+1];
		}
		tmp_ns[size_ns-1] = tmp_c;

		// Compare with ms
		bool equal = true;
//		DEB(j);
		for (unsigned i = 0; i < size_ns; i++)
		{
			if (tmp_ns[i]!=ms[i]) {
				equal = false;
				break;
			}
		}
		if (equal) {

/*		unsigned multiplier = 1;
		unsigned new_n = 0;
		unsigned new_m = 0;
		for (unsigned i = 0; i < size_ns; i++)
		{
			char tmp_cndig = tmp_ns[i];
			unsigned tmp_ndig = atoi(&tmp_cndig);
			new_n+= multiplier * tmp_ndig;

			char tmp_cmdig = ms[i];
			DEB(tmp_cmdig);
			unsigned tmp_mdig = atoi(&tmp_cmdig);
			DEB(tmp_mdig);
			new_m+= multiplier * tmp_mdig;

			multiplier*=10;
			DEB(new_m);

		}

			DEB(new_n);*/
			std::pair<unsigned, unsigned> equal_pair;
			equal_pair = make_pair(n, m);
			recycled.insert(equal_pair);
		}

	}
	
}

