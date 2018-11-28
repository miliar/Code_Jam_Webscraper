#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int index(char c)
{
  switch(c)
  {
    case 'Q':
      return 0;
    case 'W':
      return 1;
    case 'E':
      return 2;
    case 'R':
      return 3;
    case 'A':
      return 4;
    case 'S':
      return 5;
    case 'D':
      return 6;
    case 'F':
      return 7;
    default:
      return -1;
  }
}


int main()
{
  ifstream ff("input.txt");
  ofstream gg("output.txt");

  int T, N, C, D;
  char combine[8][8];
  bool opposed[8][8];
  string aux;
  vector<char> word;

  ff >> T;
  for(int t = 0; t < T; ++t)
  {
    word.clear();

    for(int i = 0; i < 8; ++i)
      for(int j = 0; j < 8; ++j)
      {
	combine[i][j] = 0;
	opposed[i][j] = false;
      }

    ff >> C;
    for(int c = 0; c < C; ++c)
    {
      ff >> aux;
      combine[index(aux[0])][index(aux[1])] = aux[2]; 
      combine[index(aux[1])][index(aux[0])] = aux[2]; 
    }
    ff >> D;
    for(int d = 0; d < D; ++d)
    {
      ff >> aux;
      opposed[index(aux[0])][index(aux[1])] = true;
      opposed[index(aux[1])][index(aux[0])] = true;
    }

    ff >> N;
    ff >> aux;

    for(int n = 0; n < N; ++n)
    {
      if(word.size() > 0 && index(word.back()) != -1 && combine[index(word.back())][index(aux[n])] != 0)
      {
	char x = combine[index(word.back())][index(aux[n])];
	word.pop_back();
	word.push_back(x);
        continue;
      }
      bool op = false;
      for(int i = 0; i < word.size(); ++i)
	if(index(word[i]) != -1 && opposed[index(word[i])][index(aux[n])] == true)
	{
	  word.clear();
	  op = true;
	  continue;
	}
      if(op == false)
	word.push_back(aux[n]);
    }

    gg << "Case #" << t+1 << ": [";
    if(word.size() > 0)
      gg << word[0];
    for(int w = 1; w < word.size(); ++w)
      gg << ", " << word[w];
    gg << "]" << endl;
   
  }

  return 0;
}
