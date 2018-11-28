#include <iostream>
#include <fstream>

using namespace std;

//initializing variables

int buttons;

int arrayOne[100];

int arrayTwo[100];



int Oprio[100];

int Bprio[100];



int indexZero;

int indexOfB;


int locZero;

int locB;


int doneZero;


int doneB;



int _time;

void moveORobot(bool hit)

{

	if(locZero == arrayOne[doneZero])

	{

		if(hit)

			doneZero++;

		else

			return;

	}

	else

	{

		if(locZero < arrayOne[doneZero])

			locZero++;

		else

			locZero--;

	}

}



void moveBRobot(bool hit)

{

	if(locB == arrayTwo[doneB])

	{

		if(hit)

			doneB++;

		else

			return;

	}

	else

	{

		if(locB < arrayTwo[doneB])

			locB++;

		else

			locB--;


	}

}



void moveRobots()

{

	if(doneZero == indexZero && doneB != indexOfB)

	{

		moveBRobot(true);

	}

	else if(doneB == indexOfB && doneZero != indexZero)

	{	

		moveORobot(true);

	}

	else if(Oprio[doneZero] < Bprio[doneB])

	{

		moveORobot(true);

		moveBRobot(false);

	}


	else if(Bprio[doneB] < Oprio[doneZero])

	{

		moveBRobot(true);

		moveORobot(false);

	}

}



int main()

{

	ifstream in;

	in.open("input.txt");



	ofstream out;

	out.open("output.txt");



	int tc = 0;

	int i_tc = 0;



	in >> tc;

	while(i_tc < tc)

	{

		for(int i=0; i<100; i++)

			arrayOne[i] = arrayTwo[i] = Oprio[i] = Bprio[i] = 0;

		

		indexZero = indexOfB = 0;



		in >> buttons;



		char r_char;

		for(int i=0; i<buttons; i++)

		{

			in >> r_char;

			if(r_char == 'B')

			{

				in >> arrayTwo[indexOfB];

				Bprio[indexOfB] = i;

				indexOfB++;

			}

			else if(r_char == 'O')

			{

				in >> arrayOne[indexZero];

				Oprio[indexZero] = i;

				indexZero++;


			}

		}



		locZero = locB = 1;

		doneZero = doneB = 0;

		_time = 0;



		while((doneZero < indexZero) || (doneB < indexOfB))

		{

			moveRobots();

			_time++;

		}

		

		out << "Case #" << i_tc+1 << ": " << _time << endl;

		

		i_tc++;

	}



	in.close();

	out.close();



	cout << endl;

	system("pause");

	return 0;

}


