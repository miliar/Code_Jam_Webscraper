#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <stdlib.h>
#include <math.h>

using std::string;
using std::vector;
using std::set;
using std::map;
using std::tr1::unordered_map;
using std::tr1::unordered_set;

class ProblemSolver {
public:
	ProblemSolver() : ist("input.txt"), ost("output.txt") {}
	void Run();
	void SolveOneTest();

private:
	std::ifstream ist;
	std::ofstream ost;
};

inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

struct Card {
	int reveals;
	int score;
	int turns;
};

inline std::istream& operator >> (std::istream& ist, Card& card)
{
	ist >> card.reveals >> card.score >> card.turns;
	return ist;
}

static void placeCard(vector<Card>& hand, vector<Card>& hidden, int& turns, int& score, int cardIndex)
{
//	std::cout << hand[cardIndex].reveals << " " << hand[cardIndex].score << " " << hand[cardIndex].turns << std::endl;
	turns--;
	Card card = hand[cardIndex];
	hand.erase(hand.begin() + cardIndex);
	while( card.reveals > 0 && hidden.size() > 0 ) {
		hand.push_back(hidden[0]);
		hidden.erase(hidden.begin());
		card.reveals--;
	}
	turns += card.turns;
	score += card.score;
}

static void discardPositiveTurns(vector<Card>& hand, vector<Card>& hidden, int& turns, int& score)
{
	bool canPutCard = true;
	while( canPutCard ) {
		canPutCard = false;
		for( int i = 0; i < hand.size(); i++ ) {
			if( hand[i].turns > 0 ) {
				placeCard(hand, hidden, turns, score, i);
				canPutCard = true;
				break;
			}
		}
	}
}

static bool discardWithNCards(int nCards, vector<Card>& hand, vector<Card>& hidden, int& turns, int& score)
{
	int maxIndex = -1;
	for( int i = 0; i < hand.size(); i++ ) {
		if( hand[i].reveals == nCards && hand[i].turns == 0 ) {
			if( maxIndex == -1 || hand[maxIndex].score < hand[i].score ) {
				maxIndex = i;
			}
		}
	}
	if( maxIndex >= 0 ) {
		placeCard( hand, hidden, turns, score, maxIndex );
		return true;
	}
	return false;
}

static int calcScore(int c10, int c20, const vector<Card>& _hand, const vector<Card>& _hidden)
{
	vector<Card> hand = _hand;
	vector<Card> hidden = _hidden;
	int turns = 1;
	int score = 0;
	while( turns > 0 && hand.size() > 0 ) {
		discardPositiveTurns(hand, hidden, turns, score);
		if( c20 > 0 && discardWithNCards(2, hand, hidden, turns, score) ) {
			c20--;
		} else if( c10 > 0 && discardWithNCards(1, hand, hidden, turns, score) ) {
			c10--;
		} else {
			if( !discardWithNCards(0, hand, hidden, turns, score) ) {
				turns--;
			}
		}
	}
	return score;
}

inline void ProblemSolver::SolveOneTest() 
{
	int n,m;
	ist >> n;
	vector<Card> cur(n);
	for( int i = 0; i < n; i++ ) {

		ist >> cur[i];
	std::cout << cur[i].reveals << " " << cur[i].score << " " << cur[i].turns << std::endl;
	}
	ist >> m;
	vector<Card> hidden(m);
	for( int i = 0; i < m; i++ ) {
		ist >> hidden[i];
	}
	int res = 0;
	for( int i = 0; i <= n + m; i++ ) {
		for( int j = 0; j <= n + m; j++ ) {
			res = std::max( res, calcScore(i, j, cur, hidden) );
		}
	}
	ost << res << "\n";
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

