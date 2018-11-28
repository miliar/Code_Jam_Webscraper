#include <fstream>
#include <string>

using namespace std;

int combine_count,
	opposed_count,
	spell_len;

string combines[36],
	opposeds[28],
	spell;

bool combine(int pos)
{
	int init_len = spell.length();
	for(int i = 0; i < combine_count && spell.length() == init_len; ++i)
	{		
		string combine = combines[i].substr(0, 2),
				combine_rev = combine,
				result = combines[i].substr(2, 1);
		char c = combine_rev[0];
		combine_rev[0] = combine_rev[1];
		combine_rev[1] = c;
		if (spell.substr(pos - 1, 2) == combine || spell.substr(pos - 1, 2) == combine_rev)
			spell.replace(pos - 1, 2, result);
	}	
	return spell.length() != init_len;
}

bool clear(int pos)
{
	int init_len = spell.length();
	for(int i = 0; i < opposed_count && init_len == spell.length(); ++i)
	{
		int pos1 = -1;
		if (spell[pos] == opposeds[i][0]) {
			pos1 = spell.substr(0, pos).find_last_of(opposeds[i][1]);
		} else if (spell[pos] == opposeds[i][1])
			pos1 = spell.substr(0, pos).find_last_of(opposeds[i][0]);
		if (pos1 >= 0 ) spell.replace(0, pos + 1, "");
	}
	return spell.length() != init_len;
}

int main (int argc, char* argv[])
{
	ifstream in("B-large.in");
	//ifstream in("B-small-attempt9.in");
	ofstream out("out.txt");
	if (in.is_open() && out.is_open())
	{
		int case_count;
		in >> case_count;
		for(int i = 0; i < case_count; ++i)
		{
			in >> combine_count;
			if (combine_count)
				for(int i = 0; i < combine_count; ++i) 
					in >> combines[i];	
			in >> opposed_count;
			if (opposed_count)
				for(int i = 0; i < opposed_count; ++i) 
					in >> opposeds[i];	
			in >> spell_len;
			in >> spell;
			bool is_chaged = false;
			for (int i = 1; i < spell.length(); ++i)
			{
				if (combine(i)) --i;
				else if (clear(i)) i = 0;
			}

			out << "Case #" << i + 1 << ": " << "[";
			for(int i = 0; i < spell.length(); ++i) {			
				out << spell[i];
				if (i < spell.length() - 1) out << ", "; 
			}
			out	<< "]\n";
		}
	}

	in.close();
	out.close();
	return 0;
}