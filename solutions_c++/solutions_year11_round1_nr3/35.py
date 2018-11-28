#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

struct Card {
	int c, s, t;
};

int N, M;
Card hand[100];
Card deck[100];

Card read_card()
{
	Card c;
	scanf("%d %d %d", &c.c, &c.s, &c.t);
	return c;
}

int score;
int turns;
int from_deck;
int handsize;

Card myhand[100];

void init()
{
	score = 0;
	turns = 1;
	from_deck = 0;
	handsize = N;
	for (int i = 0; i < N; ++i)
		myhand[i] = hand[i];
}

void get_from_deck()
{
	if (from_deck == M)
		return;
	myhand[handsize++] = deck[from_deck];
	from_deck += 1;
}

void play_card(int i)
{
	assert(turns > 0);
	score += myhand[i].s;
	turns += myhand[i].t - 1;
	if (myhand[i].c == 1) get_from_deck();
	myhand[i] = myhand[handsize-1];
	handsize -= 1;
}

void play_turn_cards()
{
	if (turns == 0)
		return;
	for (int i = 0; i < handsize; ++i) {
		if (myhand[i].t > 0) {
			play_card(i);
			i -= 1;
		}
	}
}

bool play_deck_card()
{
	int best = -1;
	int best_i = -1;
	for (int i = 0; i < handsize; ++i) {
		if (myhand[i].c == 0)
			continue;
		if (myhand[i].s > best) {
			best = myhand[i].s;
			best_i = i;
		}
	}

	if (best == -1)
		return false;
	play_card(best_i);
	play_turn_cards();
	return true;
}

bool play_score_card()
{
	int best = -1;
	int best_i = -1;
	for (int i = 0; i < handsize; ++i) {
		if (myhand[i].s > best) {
			best = myhand[i].s;
			best_i = i;
		}
	}

	if (best == -1)
		return false;
	play_card(best_i);
	play_turn_cards();
	return true;
}

bool move(int atleast_deck_usage)
{
	if (turns == 0)
		return false;
	if (from_deck < atleast_deck_usage && play_deck_card())
		return true;
	return play_score_card();
}

int get_score(int atleast_deck_usage)
{
	init();

	play_turn_cards();

	while (move(atleast_deck_usage))
		;
	return score;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			hand[i] = read_card();
		scanf("%d", &M);
		for (int i = 0; i < M; ++i)
			deck[i] = read_card();

		int best_score = -1;
		for (int i = 0; i <= M; ++i)
			max2(best_score, get_score(i));
		assert(best_score != -1);
		printf("Case #%d: %d\n", TC, best_score);
	}
	return 0;
}
