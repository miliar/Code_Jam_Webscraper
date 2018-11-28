#include <iostream>
using namespace std;

typedef struct Line
{
  Line() : X(0), O(0) {}
  unsigned X;
  unsigned O;
} Line;

int main(int argc, char** argv)
{
  int n;
  cin >> n;

  for(int i = 1; i <= n; i++)
    {
      bool finished = true;
      Line lines[4], cols[4], diag[3];

      char s;
      for(int l = 0; l < 4; l++)
	for(int c = 0; c < 4; c++)
	  {
	    char x;
	    cin >> x;

	    unsigned d = 0;
	    if(l == c)
	      d = 1;
	    else if(l == (3 - c))
	      d = 2;

	    switch(x)
	      {
	      case 'X':
		lines[l].X++; cols[c].X++; diag[d].X++;
		break;
	      case 'O':
		lines[l].O++; cols[c].O++; diag[d].O++;
		break;
	      case 'T':
		lines[l].X++; lines[l].O++;
		cols[c].X++;  cols[c].O++;
		diag[d].X++;  diag[d].O++;
		break;
	      case '.':
		finished = false;
		break;
	      }
	  }

      const char* res = NULL;
      for(int k = 0; !res && k < 4; k++)
	if(lines[k].X == 4 || cols[k].X == 4)
	  res = "X won";
	else if(lines[k].O == 4 || cols[k].O == 4)
	  res = "O won";
	else if(0 < k && k < 3)
	  {
	    if(diag[k].X == 4)
	      res = "X won";
	    else if(diag[k].O == 4)
	      res = "O won";
	  }

      if(!res)
	{
	  if(finished)
	    res = "Draw";
	  else
	    res = "Game has not completed";
	}

      cout << "Case #" << i << ": " << res << endl;
    }

  return 0;
}
