// topcoder.cpp : Defines the entry point for the console application.
//

#include <stack>
#include <vector>
#include <sstream>
#include <iostream>

#define LARGE

static const char BLUE = 'B';
static const char ORANGE = 'O';
static const unsigned int MAX_LINE = 512;

struct Move
{
	char hallway;
	char buttonPos;

	Move():hallway(0),buttonPos(0) {}

	Move(char _hallway, char _buttonPos)
		:hallway(_hallway),buttonPos(_buttonPos) {}

	Move(const Move &m)
		:hallway(m.hallway),buttonPos(m.buttonPos) {}
};

class Problem
{
	std::vector<Move> moves;

public:

	void addMove(const Move &m)
	{
		moves.push_back(m);
	}
	
	unsigned int solve() const
	{
		unsigned char posBlue = 1;
		unsigned char posOrange = 1;

		std::stack<Move> blueMoves;
		std::stack<Move> orangeMoves;


		for (unsigned int i = moves.size()-1; i != std::numeric_limits<unsigned int>::max(); i--) {
			if (moves[i].hallway == ORANGE)
				orangeMoves.push(moves[i]);
			else
				blueMoves.push(moves[i]);
		}

		bool solved = false;
		unsigned int seconds = 0;
		std::vector<Move>::const_iterator it = moves.begin();

		while (!solved) {
			bool pushed = false;
			if (orangeMoves.size()) {
				Move nextOrange = orangeMoves.top();

				if (nextOrange.buttonPos == posOrange) { 
					if ((*it).hallway == ORANGE) {
						//push the button;
						it++;
						orangeMoves.pop();
						pushed = true;
					} else {
						//wait... its blue's time
					}
				} else if (nextOrange.buttonPos > posOrange) {
					//we have to just move it one position
					posOrange++;
				} else if (nextOrange.buttonPos < posOrange) {
					//we have to just move it one position
					posOrange--;
				}
			} 

			if (blueMoves.size()) {
				Move nextBlue = blueMoves.top();

				if (nextBlue.buttonPos == posBlue) { 
					if ((!pushed) && ((*it).hallway == BLUE)) {
						//push the button;
						it++;
						blueMoves.pop();
					} else {
						//wait... it was orange's time
					}
				} else if (nextBlue.buttonPos > posBlue) {
					//we have to just move it one position
					posBlue++;
				} else if (nextBlue.buttonPos < posBlue) {
					//we have to just move it one position
					posBlue--;
				}
			}

			if (blueMoves.empty() && orangeMoves.empty())
				solved = true;
			
			seconds++;
		}

		return seconds;
	}
};

static Problem parseProblem(const char *line);

int main(int argc, char* argv[])
{
	//freopen("ex.in","rt",stdin);

#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif


	char line[MAX_LINE];
	unsigned int cases;
	std::stringstream parser;

	std::cin.getline(line,MAX_LINE);
	parser.write(line,std::strlen(line));

	parser >> cases;

	for (unsigned int i = 1; i <= cases; i++) {
		std::cin.getline(line,MAX_LINE);

		Problem p = parseProblem(line);

		std::cout << "Case #" << i << ": " << p.solve() << std::endl;
	}

	return 0;
}

Problem parseProblem(const char *line)
{
	Problem problem;
	std::stringstream ss;

	ss.write(line,std::strlen(line));

	unsigned int moves;
	ss >> moves;

	for (unsigned int i = 0; i < moves; i++) {
		Move move;

		ss.get(); //discard ' '

		move.hallway = ss.get();

		ss.get(); //discard ' '

		unsigned int pos;
		ss >> pos;

		move.buttonPos = (char)pos;

		problem.addMove(move);
	}

	return problem;
}

