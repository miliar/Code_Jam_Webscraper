#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstdlib>
#include<string>
#include<cassert>

using namespace std;

struct move
{
	char bot;
	int place;
};


int buttontime(move buttons[], int n);
int getDest(move me, move butts[], int n, int & spot);

int main()
{
	int time; int numcases; int n;
	cin >> numcases;
	for(int index = 0; index < numcases; index++)
	{
		cin >> n;
		move *buttons = new move[n];
		for(int i = 0; i < n; i++)
		{
			cin >> buttons[i].bot >> buttons[i].place;
		}
		time = buttontime(buttons, n);
		cout << "Case #" << index+1 << ": " << time << endl;
		delete[] buttons;
	}
	return 0;
}

int buttontime(move buttons[], int n)
{
	move blue; blue.bot = 'B'; blue.place = 1; int bluespot = -1;
	move orange; orange.bot = 'O'; orange.place = 1; int orangespot = -1;
	int bluedest = getDest(blue, buttons, n, bluespot);
	int orangedest = getDest(orange, buttons, n, orangespot);
	int spot = 0;
	char turn;
	int time = 1;
	while(bluedest != INT_MIN || orangedest != INT_MIN)
	{
		turn = buttons[spot].bot;
		if(blue.place < bluedest)
			blue.place++;
		else if(blue.place > bluedest)
			blue.place--;
		else if(blue.bot == turn && blue.place == bluedest)
		{
			bluedest = getDest(blue, buttons, n, bluespot);
			spot++;
//			cout << "blue presses button" << endl;
		}
		if(orange.place < orangedest)
			orange.place++;
		else if(orange.place > orangedest)
			orange.place--;
		else if(orange.bot == turn && orange.place == orangedest)
		{
			orangedest = getDest(orange, buttons, n, orangespot);
			spot++;
//			cout << "orange presses button" << endl;
		}
//		cout << time << ", blue: " << blue.place << ", orange: " << orange.place << endl;
		time++;
	}
	return time - 1;
}




int getDest(move me, move butts[], int n, int & spot)
{
	spot++;
	while(spot < n)
	{
		if(butts[spot].bot == me.bot)
			return butts[spot].place;
		spot++;
	}
	return INT_MIN;
}








