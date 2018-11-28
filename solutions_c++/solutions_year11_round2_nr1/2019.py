/*
 * File: Combinations.cpp
 * ----------------------
 * Name: [TODO: enter name here]
 * Section: [TODO: enter section leader here]
 * This file is the starter project for the combinations problem.
 * [TODO: rewrite the documentation]
 */

#include "genlib.h"
#include "simpio.h"
#include <iostream>
#include <fstream>
#include "scanner.h"
#include "strutils.h"
#include "vector.h"
#include "queue.h"
#include "grid.h"

const string Title = "A-large 1.in";
const string Test = "test.txt";

int playgame(Vector<Vector<int>>hand, Queue<Vector<int>>deck, int cards, int points, int turns);

int main() {
	//string Title = GetLine();
	ifstream infile;
	ofstream offile;
	offile.open(Test.c_str());
	infile.open(Title.c_str());
	//if(!infile.fail()) cout <<"Error: File Could Not Be Read"<< endl;
	string num;
	getline(infile, num); 
	int Numb = StringToInteger(num);

	//cout << Numb << endl;
	for(int i = 0; i < Numb; i++){
		string temp;
		getline(infile, temp);
		int numOfTeams = StringToInteger(temp);
		Grid<char> playedwho (numOfTeams, numOfTeams);
		int *wins = new int[numOfTeams];
		int *gamesplayed = new int[numOfTeams];

		for(int j = 0; j < numOfTeams; j ++){
			wins[j] = 0;
			gamesplayed[j] = 0;

			for(int k = 0; k < numOfTeams; k++){
				playedwho[j][k] = '0';
			}
		}
		for(int j = 0; j < numOfTeams ; j++){
			Vector<char> card;
			int c, s, t;
			getline(infile, temp);
			for(int k = j + 1; k < numOfTeams; k++){
				char result = temp[k];
				
				if(result == '1'){
					wins[j]++;
					gamesplayed[j]++;
					gamesplayed[k]++;
					playedwho.setAt(j, k, '2');
					playedwho.setAt(k, j, '1');
				} else if(result == '0'){
					wins[k]++;
					gamesplayed[k]++;
					gamesplayed[j]++;
					playedwho.setAt(j, k, '1');
					playedwho.setAt(k, j, '2');
				} else {
					playedwho.setAt(j, k, '0');
					playedwho.setAt(k, j, '0');
				}
			}
		}
		
		double *WP= new double[numOfTeams];
		double *OWP = new double[numOfTeams];
		double *OOWP = new double[numOfTeams];
		
		for (int j = 0; j < numOfTeams; j++){
			OWP[j] = 0;
			OOWP[j] = 0;
			WP[j] = ((double)wins[j]/(double)gamesplayed[j]);
			int counter = 0;
			double value = 0.0;
			for(int k = 0; k <numOfTeams; k++){
				if(playedwho[j][k] == '2'){
					counter++;
					value = value + ((double)(wins[k])/(double)(gamesplayed[k]- 1));
					
				} else if(playedwho[j][k] == '1'){
					counter++;
					value = value + ((double)(wins[k]- 1)/(double)(gamesplayed[k]- 1));
						
				}
			}
			OWP[j] = value/(double)counter;
		}
		
		
		for(int j = 0; j < numOfTeams; j++)
		{
			int counter = 0;
			double value = 0.0;
			for(int k = 0; k < numOfTeams; k++){
				if(playedwho[j][k] != '0'){
					counter++;
					value = value + OWP[k];
				}
			}
			OOWP[j] = value/(double) counter;
		}
		offile <<"Case #" << i + 1 << ":" << endl;
		for(int j = 0; j < numOfTeams; j++){
			double temps = 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j];
			offile << temps << endl;
		}
	}
	
			

	return 0;
}

int playgame(Vector<Vector<int>>hand, Queue<Vector<int>>deck, int cards, int points, int turns){
	//cout << "Cards: " << cards << "  Points:   " << points << "   Turns:   " << turns << endl;
	if(turns == 0 || cards == 0) return points;
	int pointindex = 0;
	int maxpoint = 0;
	int cardindex = 0;
	int maxcard = 0;
	for(int i = 0; i < cards; i++){
		Vector<int> temp = hand[i];
		if(temp[2] > 0){
			hand.removeAt(i);
			cards = cards - 1;
			points = points + temp[1];
			turns = turns - 1 + temp[2];
			for(int j = 0; j < temp[0]; j++){
				if(!deck.isEmpty())	{
					hand.add(deck.dequeue());
					cards++;
				}
			}
			return playgame(hand, deck, cards, points, turns);
		}
		if(temp[1] >= maxpoint){
			maxpoint = temp[1];
			pointindex = i;
		}
		if(temp[0] >= maxcard){
			maxcard = temp[0];
			cardindex = i;
		}
	}
	if(deck.isEmpty()){
	//	cout << "EMPTY  EMPTY " << endl;
		Vector<int>best = hand[pointindex];
		hand.removeAt(pointindex);
		points = points + maxpoint;
		turns--;
		cards--;
		return playgame(hand, deck, cards, points, turns);
	}
	
	if(turns >= cards + deck.size()){
		Vector<Vector<int>>temphand = hand;
		Vector<int> tempcardcard = hand[cardindex];
		int tempcard = cards;
		temphand.removeAt(cardindex);
		Queue<Vector<int>>tempdeck = deck;
		for(int j = 0; j < tempcardcard[0]; j++){
			if(!tempdeck.isEmpty())	{
				temphand.add(tempdeck.dequeue());
				tempcard++;
			}
		}
		return playgame(temphand, tempdeck, tempcard - 1, points + tempcardcard[1], turns - 1);
		
	}

	if(turns == 1){
			Vector<Vector<int>>temphand = hand;
		Vector<int> temppointcard = hand[pointindex];
		int tempcard = cards;
		temphand.removeAt(pointindex);
		Queue<Vector<int>> tempdeck = deck;
		for(int j = 0; j < temppointcard[0]; j++){
		if(!tempdeck.isEmpty())	{
			temphand.add(tempdeck.dequeue());
			tempcard++;
		}
	}
		return playgame(temphand, tempdeck, tempcard - 1, points + maxpoint, turns - 1);
	}

	int maxscore = 0;
	//cout << " SPLIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
		int bigcards = 0;
	int bigpoints = 0;
	for(int k = 0; k < cards; k++){
		Vector<int> tempcard = hand[k];
		if(tempcard[0] > bigcards && tempcard[1] > bigpoints){
			Vector<Vector<int>>temphand = hand;
			int tempcardnum = cards;
			temphand.removeAt(k);
			Queue<Vector<int>>tempdeck = deck;
			for(int j = 0; j < tempcard[0]; j++){
				if(!tempdeck.isEmpty())	{
					temphand.add(tempdeck.dequeue());
					tempcardnum++;
				}
			}
			int newnum = playgame(temphand, tempdeck, tempcardnum - 1, points + tempcard[1], turns - 1);
			if(newnum > maxscore) maxscore = newnum;
			if (tempcard[0] >= bigcards && tempcard[1] >= bigpoints){
				bigcards = tempcard[0];
				bigpoints = tempcard[1];
			}
		}	
	}

	return maxscore;
}