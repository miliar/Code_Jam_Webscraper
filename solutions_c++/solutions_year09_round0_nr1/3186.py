#include <iostream>
#include <vector>
#include <sstream>

using namespace std;


// this just reads in a dictionary, parses the messed up messages
// and then loops through dictionary to see if word is makeeable from the message

int main()
{
  int L,D,N;
  //stringstream ss;
  cin >> L >> D >> N;
  
  vector <string> dictionary;
  
  // get words from dictionary from stdin
  for (int i = 0; i < D; i++)
    {
      string s;
      cin >> s;
      dictionary.push_back(s);
    }

  int letters_count [L*N][26];  

  for (int i = 0; i < L*N; i++)
    {
      for (int j = 0; j < 26; j++)
	{
	  letters_count[i][j] = 0;
	}
    }


  // parse each message and flip if letter is in slot in letter_count
  for (int i = 0; i < N; i++)
    {
      // get the msg
      string m;
      cin >> m;
      
      // current slot- ranges from 0 to L-1
      int cl = 0;
      // parse the msg
      for (int j = 0; j < m.size(); j++)
	{
	  if (m[j] >= 'a' && m[j] <= 'z')
	    {
	      int k = m[j] - 'a';
	      letters_count[L*i+cl][k] = 1;
	      cl++;
	    }
	  else
	    {      
	      // read in until close paren
	      while(true)
		{
		  if (m[j] == ')')
		    {break;}
		  if (m[j] >= 'a' && m[j] <= 'z')
		    {
		      int k = m[j] - 'a';
		      letters_count[L*i+cl][k] = 1;
		    }
		  j++;
		}
	      cl++;
	    }
	}
    }

  for (int i = 0; i < N; i++)
    {
      int word_count = 0;
      for (int j = 0; j < D; j++)
	{
	  bool present = true;
	  // check if in current message
	  for (int k = 0; k < L; k++)
	    {
	      string s = dictionary[j];
	      char c = s[k];
	      int index = c-'a';
	      if (letters_count[i*L+k][index] == 0)
		present = false;
	    }
	  if (present)
	    word_count++;
	}
      cout << "Case #" << i+1 << ": " << word_count << endl;
    }

  return 0;

}
