#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int
main (int argc, char **argv)
{
  if (argc != 2)
    return 1;

  unsigned int T;

  std::ifstream ifs (argv[1], std::ifstream::in);

  ifs >> T;

  for (unsigned i = 0; i < T; ++i)
    {
      int N, S, p;
      ifs >> N;
      ifs >> S;
      ifs >> p;
      unsigned res = 0;

      for (int n = 0; n < N; ++n)
	{
	  int score;
	  ifs >> score;

	  if (score >= 3 * p || (score == 3 * p - 1 && score >= 2) || (score == 3 * p - 2 && score >= 1))
	    ++res;
	  else
	    if (S > 0 && ((score == 3 * p - 3 && score >= 3) || (score == 3 * p - 4 && score >= 2)))
	      {
		++res;
		--S;
	      }
	}
      std::cout << "Case #" << i + 1 << ": " << res << std::endl;

    }
  /*
  //test cases
  for (unsigned i = 0; i < N; ++i)
    {
      std::string pattern;
      ifs >> pattern;
      std::vector <std::string> compatible;
      unsigned letter_nb = 0;

      for (unsigned j = 0; j < words.size (); ++j)
	compatible.push_back (words[j]);

      for (unsigned j = 0; j < pattern.length (); ++j)
	{
	  std::vector <char> cur_letters;
	  if (pattern[j] == '(')
	    while (pattern[++j] != ')')
	      cur_letters.push_back (pattern[j]);
	  else
	    cur_letters.push_back (pattern[j]);

	  for (unsigned index = 0; index < compatible.size (); index++)
	    {
	      bool OK = false;

	      for (unsigned index2 = 0; index2 < cur_letters.size (); ++index2)
		if (compatible[index][letter_nb] == cur_letters[index2])
		  OK = true;
	      
	      if (!OK)
		{
		  compatible.erase (compatible.begin () + index, compatible.begin () + index + 1);
		  --index;
		}
	    }
	  ++letter_nb;
	}
      std::cout << "Case #" << i + 1 << ": " << compatible.size () << std::endl;
    }*/

  ifs.close ();

  return 0;
}
