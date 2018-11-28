#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cassert>

using namespace std;

int main()
{
	ifstream in("input.txt");

	int case_count;
	in >> case_count;
	string dummy;
	getline(in, dummy);

	ofstream out("output.txt");

	for (int case_index = 0; case_index < case_count; ++case_index)
	{
		string symbols;
		getline(in, symbols);

		vector<int> symbol_found_flags(256);
		fill(symbol_found_flags.begin(), symbol_found_flags.end(), -1);
		vector<char> encountered_symbols;
		for (int sym_index = 0, sym_count = int(symbols.length()); sym_index < sym_count; ++sym_index)
		{
			if (symbol_found_flags[symbols[sym_index]] == -1)
			{
				symbol_found_flags[symbols[sym_index]] = sym_index;
				encountered_symbols.push_back(symbols[sym_index]);
			}
		}

		int base = int(encountered_symbols.size());
		if (base < 2)
			base = 2;

		vector<int> position_values(encountered_symbols.size());
		if (encountered_symbols.size() > 0)
			position_values[0] = 1;
		if (encountered_symbols.size() > 1)
			position_values[1] = 0;
		for (int sym_index = 2, sym_count = int(encountered_symbols.size()); sym_index < sym_count; ++sym_index)
			position_values[sym_index] = sym_index;

		vector<int> symbol_values(256);
		fill(symbol_values.begin(), symbol_values.end(), 0);
		for (int sym_index = 0, sym_count = int(encountered_symbols.size()); sym_index < sym_count; ++sym_index)
			symbol_values[encountered_symbols[sym_index]] = position_values[sym_index];

		unsigned __int64 value = 0;
		int place_value = 1;
		for (int sym_index = int(symbols.length()) - 1; sym_index >= 0; --sym_index)
		{
			value += symbol_values[symbols[sym_index]] * place_value;
			place_value *= base;
		}

		out << "Case #" << case_index + 1 << ": " << value << "\n";
	}

	return 0;
}
