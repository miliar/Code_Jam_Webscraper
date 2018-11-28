#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

enum BotColor { ORANGE, BLUE };

struct move
{
  BotColor bot;
  int position;
};

int main()
{
  ifstream ff("input.txt");
  ofstream gg("output.txt");

  int T, N;
  vector<move> moves;
  string aux;

  moves.resize(100);

  ff >> T;
  for(int t = 0; t < T; ++t)
  {
    ff >> N;
   
    moves.clear();

    for(int n = 0; n < N; ++n)
    {
      move current;
      ff >> aux;
      if(aux == "O")
	current.bot = ORANGE;
      else
	current.bot = BLUE;
      ff >> current.position;
      moves.push_back(current);
    }

    int posOrange = 1;
    int posBlue = 1;
    int extraOrange = 0;
    int extraBlue = 0;
    int time = 0;
    int ct = 0;

    for(int n = 0; n < N; ++n)
    {
      if(moves[n].bot == ORANGE)
      {
	if(extraOrange > abs(posOrange - moves[n].position))
	  ct = 1;
	else
	  ct = abs(posOrange - moves[n].position) - extraOrange + 1;

	time += ct;
	extraBlue += ct;
	extraOrange = 0;
	posOrange = moves[n].position;
      }
      else
      {
	if(extraBlue > abs(posBlue - moves[n].position))
	  ct = 1;
	else
	  ct = abs(posBlue - moves[n].position) - extraBlue + 1;

	time += ct;
	extraOrange += ct;
	extraBlue = 0;
	posBlue = moves[n].position;
      }
    }

    gg << "Case #" << t+1 << ": " << time << endl;
  }

  return 0;  
}
