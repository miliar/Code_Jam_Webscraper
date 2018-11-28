#include <iostream>
#include <math.h>
#include <conio.h>
#include <fstream>

typedef unsigned char cellNum;
enum robotColor {orange, blue};


//SORRY FOR MY ENGLISH

/*
(note) I change rules a bit.
Each turn that robot waits he gains a teleporation opportunity.
1.)k turns of waiting = power to get anywhere within radius of k
2.)each teleportation nulls teleporter charge
Which is pretty much the same rules, but written another words.
spareTurns == teleport charge

Q: WHY IS IT THE SAME I DONT GET IT ARE YOU CRAZY
A:	While waiting for another robot k turns, one can freely walk back and forward k turns.
	Since robot is more or less intelligent he doesn't waste his time and goes to the next
	target.
	So we "remember" his last click location and assume he was on his way to the next button.
*/

//next turn in sequence
struct doTurn
{
	robotColor color;
	cellNum clickCell;
};

//nulls negative numbers
int nullNegative(int val)
{
	return val < 0 ? 0 : val;
}

//If robot was on X button and he must press Y button, 
//it will take him |X-Y| turns to get there and 1 to press it
//If he had spareTurns (a.k.a. teleporter charge), good for him - it's |X-Y|-spareTurns to get there
//with a minimum of 0 and 1 to click it
//because spareTurns reduces movement turns to minimum of 0 and to the minimum of 1 total (with click turn)
int turnsToComplete(cellNum clickPos, cellNum initPos, int spareTurns)
{
	return nullNegative(abs(clickPos - initPos) - spareTurns)+1;
}

//gets result for a sequence
int sumTurns(doTurn* turnArr, size_t size)
{
	int spareOTurns = 0; //"teleport charge" (see note) for orange 
	int spareBTurns = 0; //"teleport charge" (see note) for blue

	cellNum orangeLoc = 1; //current orange robot location
	cellNum blueLoc = 1;   //current blue   robot location

	int sum = 0;			//turns to perform so far
	for(size_t i=0; i<size; i++) //go through array of to-do turns
	{
		int forOrangeToGo = 0;
		int forBlueToGo = 0;
		
		//orange turn? Calculate how long it will take him. Blue can rest
		if(turnArr[i].color == orange)
		{
			forOrangeToGo = turnsToComplete(turnArr[i].clickCell, orangeLoc, spareOTurns);
			orangeLoc = turnArr[i].clickCell;
		}
		else
		{//same for blue
			forBlueToGo = turnsToComplete(turnArr[i].clickCell, blueLoc, spareBTurns);
			blueLoc = turnArr[i].clickCell;
		}

		//who was busy?
		//one who was busy loses all the teleporter charge 
		//one who was resting gains as much charge as the amount of turns he waited
		//don't forget to increase total turns!
		if(forOrangeToGo > forBlueToGo)
		{
			spareBTurns += forOrangeToGo;
			spareOTurns = 0;
			sum += forOrangeToGo;
		}
		else
		{
			spareOTurns += forBlueToGo;
			spareBTurns = 0;
			sum += forBlueToGo;
		}
	}
	return sum;
}

doTurn* readTurnsLine(std::ifstream& input, size_t turns)
{
	doTurn* turnArr = new doTurn[100];
	char color = ' ';
	int cell = 0;
	for(size_t i=0; i<turns; i++)
	{
		input >> color;
		input >> cell;
		turnArr[i].color		= (color == 'O') ? orange : blue;
		turnArr[i].clickCell	= cell;
	}
	return turnArr;
}

int main()
{
//	doTurn turns[] = {{blue,2},{blue,1}};
//	std::cout<<sumTurns(turns,2);

	size_t cases = 0;
	size_t turns = 0;
	//open input and output
	std::ifstream input("C:\\temp\\a-large-robots.in");
	std::ofstream output("C:\\temp\\a-large-robots.out");
	//read T
	input>>cases;
	//case counter
	int i = 0;
	//go through whole file
	while(i++ != cases)
	{
		//read N
		input>>turns;
		//get all numbers from line
		doTurn* turnArr = readTurnsLine(input,turns);
		//get turns total
		int turnsTotal = sumTurns(turnArr,turns);
		//memory is allocated each time readTurnsLine is called. Let's clear the mess.
		output<<"Case #"<<i<<": "<<turnsTotal<<std::endl;
		delete [] turnArr;
	}
	//so i don't have to wait anymore? Swell
	std::cout<<"Done!";
	_getch();
	return 0;
}