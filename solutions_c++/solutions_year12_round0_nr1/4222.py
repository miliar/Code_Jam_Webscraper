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
  //            a  , b,    c,   d,   e,   f,   g,   h,   i,   j,   k,   l,   m,   n,   o,   p,   q,   r,   s,   t,   u,   v,   w,   x,   y,   z
  char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

  std::ifstream ifs (argv[1], std::ifstream::in);

  ifs >> T;
  char tmp[4096];
  ifs.getline (tmp, 4096);
  for (unsigned i = 0; i < T; ++i)
    {
      char tmp[4096];
      ifs.getline (tmp, 4096);
      std::string word (tmp);
      std::string res (word);
      //std::cout << "word = " << word << std::endl;
      for (unsigned j = 0; j < word.size (); ++j)
	{
	  if (word[j] == ' ')
	    res[j] = ' ';
	  else
	    res[j] = map[word[j] - 'a'];
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
    }
  */
  ifs.close ();

  return 0;
}
