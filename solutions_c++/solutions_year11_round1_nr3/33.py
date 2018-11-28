#include <bitset>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <deque>
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;
ofstream fout("C-small.out");
ifstream fin("C-small.in");
int calculateAnswer(vector<pair<int, pair<int, int> > > hand, queue<pair<int, pair<int, int> > > deck, int turns){
	if(turns == 0 || hand.size() == 0){
		return 0;
	}
	int turns2 = turns - 1;
	for(int i=0;i<hand.size();i++){
		//cout << hand[i].first << " " << hand[i].second.first << " " << hand[i].second.second << endl;
		if(hand[i].second.second > 0){
			turns2 += hand[i].second.second;
		
			int sc = hand[i].second.first;
			if(hand[i].first == 1 && !deck.empty()){
				pair<int, pair<int, int> > nextcard = deck.front();
				deck.pop();
				hand.push_back(nextcard);
			}
			hand.erase(hand.begin() + i);
			return calculateAnswer(hand, deck, turns2) + sc;
		}
	}
	//cout << endl;
	int max1 = -1; // max guy with a 1 card bonus
	int maxbonus = 0;
	vector<int> scores0; // guys with a 0 card bonus
	
	for(int i=0;i<hand.size();i++){
		//cout << hand[i].first << " " << hand[i].second.first << " " << hand[i].second.second << endl;
		if(hand[i].first != 0){
			if(hand[i].second.first > maxbonus){
				max1 = i;
				maxbonus = hand[i].second.first;
			}
		} else {
			scores0.push_back(-hand[i].second.first); // put the max guys first
		}
		//cout << hand[i].first << " " << hand[i].second.first << " " << hand[i].second.second << endl;
	}
	
	sort(scores0.begin(), scores0.end());
	int total0 = 0;
	for(int k = 0; k < min((int)scores0.size(), turns); k++){
		total0 -= scores0[k];
	}
	
	int total1 = 0;
	if(max1 != -1){
		//cout << max1;
		if(!deck.empty()){
			pair<int, pair<int, int> > nextcard = deck.front();
			deck.pop();
			hand.push_back(nextcard);
		}
		int sc = hand[max1].second.first;
		hand.erase(hand.begin() + max1);
		total1 = calculateAnswer(hand, deck, turns2) + sc;
	}
	return max(total0, total1);
	
}
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int N, M;
		fin >> N;
		vector<pair<int, pair<int, int> > > hand;
		queue<pair<int, pair<int, int> > > deck;
		for(int i=0;i<N;i++){
			int c, s, t;
			fin >> c >> s >> t;
			hand.push_back(make_pair(c,make_pair(s,t)));
		}
		fin >> M;
		for(int i=0;i<M;i++){
			int c, s, t;
			fin >> c >> s >> t;
			deck.push(make_pair(c,make_pair(s,t)));
		}
		fout << "Case #"<< s+1 << ": " << calculateAnswer(hand, deck, 1) << endl;
	}
}
