#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

struct card
{
	int c,s,t;
};

int main()
{
// 	ifstream fin("C-sample.in");
// 	ofstream fout("C-sample.out");
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C-small-attempt1.out");
	
	int T;
	fin >> T;
	for(int tt = 0; tt < T; tt++)
	{
		fout << "Case #" << tt+1 << ": ";
		
		int N;
		fin >> N;
		
		vector<card> hand;
		for(int i = 0; i < N; i++)
		{
			card x;
			fin >> x.c >> x.s >> x.t;
			hand.push_back(x);
		}
		int M;
		fin >> M;
		vector<card> deck;
		for(int i = 0; i < M; i++)
		{
			card x;
			fin >> x.c >> x.s >> x.t;
			deck.push_back(x);
		}
		
		int baseTurns = 1;
		int baseScore = 0;
		while(1)
		{
			int moreturn = 0;
			for(int i = 0; i < hand.size(); i++)
			if(hand[i].t > 0)
			{
				baseScore += hand[i].s;
				moreturn = 1;
				baseTurns--;
				baseTurns += hand[i].t;
				if(hand[i].c == 1 && deck.size() > 0)
				{
					hand.push_back(deck[0]);
					deck.erase(deck.begin());
				}
				hand.erase(hand.begin()+i);
				i--;
			}
			if(moreturn == 0) break;
		}
		
		int ans = baseScore;
		
		int toTake = -1;
		while(toTake < 100)
		{
			toTake++;
			
			int bad = 0;
			vector<card> myHand = hand;
			vector<card> myDeck = deck;			
			int currScore = baseScore;
			int currTurns = baseTurns;
			int leftToTake = toTake;
			
			while(leftToTake > 0)
			{
				if(currTurns == 0) 
				{
					bad = 1;
					break;
				}
				if(myDeck.size() == 0) 
				{
					bad = 1;
					break;
				}
				
				//find the card that allows you to take with the highest score
				int bestind = -1;
				int bestSc = -1;
				for(int i = 0; i < myHand.size(); i++)
				{
					if(myHand[i].c > 0 && myHand[i].s > bestSc)
						bestSc = myHand[i].s, bestind = i;
				}
				if(bestind == -1)
				{
					bad = 1;
					break;
				}
				
				leftToTake--;
				currTurns--;
				currScore += myHand[bestind].s;
				
				if(myDeck.size() > 0)
				{
					myHand.push_back(myDeck[0]);
					myDeck.erase(myDeck.begin());
					if(currTurns > 0)
					{
						while(1)
						{
							int moreturn = 0;
							for(int i = 0; i < myHand.size(); i++)
							if(myHand[i].t > 0)
							{
								currScore += myHand[i].s;
								moreturn = 1;
								currTurns--;
								currTurns += myHand[i].t;
								if(myHand[i].c == 1 && myDeck.size() > 0)
								{
									myHand.push_back(myDeck[0]);
									myDeck.erase(myDeck.begin());
								}
								myHand.erase(myHand.begin()+i);
								i--;
							}
							if(moreturn == 0) break;
						}
					}
				}
				myHand.erase(myHand.begin() + bestind);
			}
			if(bad) continue;
			
			vector<int> sc;
			for(int p = 0; p < myHand.size(); p++)
				sc.push_back(myHand[p].s);
			sort(sc.begin(),sc.end());
			reverse(sc.begin(),sc.end());
			for(int p = 0; p < sc.size(); p++)
				if(p < currTurns)
					currScore += sc[p];
			
			//play remaining high score cards
			if(currScore > ans) ans = currScore;
		}
		
		
				
		fout << ans << endl;
	}
	return 0;
}










