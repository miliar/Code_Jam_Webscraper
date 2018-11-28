
#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;



#define fr(a,b,c) for(ui a=(b);a < (c);a++)


void eatBlank()
{
	while(isspace(std::cin.peek()))
		std::cin.get();
}

template<class T> T in()
{
	T t;
	eatBlank();
	std::cin >> t;
	return t;
}

template<> std::string in()
{
	std::string s;
	char c;
	eatBlank();
	while(!isspace(c = std::cin.get()))
		s.append(1,c);
	return s;
}


typedef unsigned int ui;

bool wantC;

struct Card
{
	ui c;
	ui s;
	ui t;

	bool operator<(const Card &o) const
	{
		if(t != o.t)
			return t > o.t;
		else if(wantC)
		{
			if(c != o.c)
				return c > o.c;
			return s > o.s;
		}
		else
		{
			if(s != o.s)
				return s > o.s;
			return c > o.c;
		}
	}

	void print() { std::cout << "Card " << c << " " << s << " " << t << std::endl; }
};

ui score(list<Card> &hand, const list<Card> &deck, ui turns);
ui play(const list<Card> hand, list<Card> deck, ui turns);

ui score(list<Card> &hand, const list<Card> &deck, ui turns)
{
	if(turns == 0 || hand.size() == 0)
		return 0;

	wantC = false;
	hand.sort();

	Card c = hand.front();
	ui m1 = 0;
	if(c.c == 0)
	{
		m1 = play(hand, deck, turns);
	}
	
	wantC = true;
	hand.sort();
	c = hand.front();
	ui m2 = 0;
	if(c.c == 1)
	{
		m2 = play(hand, deck, turns);
	}
	return std::max(m1, m2);
}

ui play(list<Card> hand, list<Card> deck, ui turns)
{
	Card c = hand.front();
	hand.pop_front();

	turns = turns + c.t - 1;
	if(c.c == 1 && deck.size() > 0)
	{
		hand.push_front(deck.front());
		deck.pop_front();
	}

	return c.s + score(hand, deck, turns);
}

Card readCard()
{
	Card c;
	c.c = in<ui>();
	c.s = in<ui>();
	c.t = in<ui>();
	return c;
}

void solve()
{
	ui N = in<ui>();
	list<Card> hand;
	fr(i,0,N)
		hand.push_front(readCard());
	
	ui M = in<ui>();
	list<Card> deck;
	fr(i,0,M)
		deck.push_back(readCard());
	std::cout << score(hand, deck, 1);
}

int main()
{
	ui n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(ui i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}
