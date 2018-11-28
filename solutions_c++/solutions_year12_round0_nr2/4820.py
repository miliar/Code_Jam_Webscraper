#include "dancing.hh"

using namespace std;

int main (int argc, char** argv)
{
  fstream f;
  ofstream o;
  char c[4];
  string s;
  unsigned int line;
  unsigned int player;
  unsigned int count;
  unsigned int surprise;
  unsigned int max_note;
  unsigned int notation;

  f.open(argv[1]);
  o.open("out");

  f.getline(c, 4);
  line = atoi(c);

  for (unsigned int i = 0; i < line; i++)
  {
    count = 0;
    player = 0;
    surprise = 0;
    max_note = 0;

    f.getline(c, 4,' ');
    player = atoi(c);

    f.getline(c, 4,' ');
    surprise = atoi(c);

    f.getline(c, 3,' ');
    max_note = atoi(c);

    for (unsigned int j = 0; j < player; j++)
    {
      notation = 0;

      if (j == player - 1)
	f.getline(c, 3);
      else
	f.getline(c, 3,' ');

      notation = atoi(c);

      if (max_note == 0)
	count++;
      else if ((max_note + (2 * (max_note - 1))) <= notation)
	count++;
      else if (((max_note + (2 * (max_note - 2))) <= notation)
	       && surprise > 0
	       && max_note > 1)
      {
	count++;
	surprise--;
      }
    }

    o << "Case #" << i + 1 << ": " << count << endl;

  }

  f.close();
  o.close();

  return 0;
}
