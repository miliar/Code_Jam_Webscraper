
#include <iostream>
#include <fstream>

#include <map>
#include <set>
#include <vector>

#include <algorithm>

typedef long long ll;

bool sort_function (const std::pair<unsigned, unsigned>& left,const std::pair<unsigned, unsigned>& right) { return (left.second>right.second); }

/*
namespace std
{
	inline bool  operator <(const std::pair<unsigned, unsigned>& left,const std::pair< unsigned, unsigned>& right) { return (left.second>right.second); }
}
*/

int main(int argc, char *argv[])
{
	std::ifstream in("A-small.in");
	std::ofstream out("A-small.out", std::ios::out | std::ios::trunc);

	unsigned N;
	in >> N;

	for (unsigned i = 0; i < N; ++i)
	{
		unsigned P,K,L;
		in >> P >> K >> L;
		std::map<unsigned, unsigned> freq;
		std::map<unsigned, std::vector<unsigned> > key_to_letters;

		for (unsigned j = 0; j < K; ++j)
		{
			std::vector<unsigned> vect;
			key_to_letters[j] = vect;
		}

		for (unsigned j = 0; j < L; ++j)
		{
			unsigned num;
			in >> num;
			freq[j] = num;
		}
		
		// sort letters by frequency
		std::vector<std::pair<unsigned, unsigned> > freq_vect(freq.begin(),freq.end());
		std::sort(freq_vect.begin(),freq_vect.end(), sort_function);

		unsigned cur_key = 0;
		bool go_forward = true;
		// for all letters, go forward-back
		for (std::vector<std::pair<unsigned, unsigned> >::const_iterator it = freq_vect.begin(); it != freq_vect.end(); ++it)
		{
			key_to_letters[cur_key].push_back((*it).first);
			std::cout << std::endl << i << ": "<<cur_key << " " << (*it).second;
			
			if (go_forward)
			{
				if (cur_key <= K - 2)
				{
					cur_key++;
					continue;
				}
				else
				{
					//cur_key--;
					go_forward = false;
					continue;
				}
			}
			else
			{
				if (cur_key >= 1)
				{
					cur_key--;
					continue;
				}
				else
				{
					//cur_key++;
					go_forward = true;
					continue;
				}
			}
			
		}

		unsigned presses = 0;
		for (std::map<unsigned, std::vector<unsigned> >::const_iterator it = key_to_letters.begin(); it != key_to_letters.end(); ++it)
		{
			unsigned depth = 1;
			for (std::vector<unsigned>::const_iterator it2 = (*it).second.begin(); it2 != (*it).second.end(); ++it2)
			{
				//std::cout << std::endl << i << ":| " << (*it).first << " --- " << *it2;

				presses += freq[*it2] * depth; 
				//std::cout << std::endl << i << ":| " << freq[*it2] << " " << presses;
				depth++;
			}
		}
		
		out << "Case #" << i + 1 << ": " << presses << std::endl;
		//delete freq;
	}

	in.close();
	out.close();
	
	return 0;
}
