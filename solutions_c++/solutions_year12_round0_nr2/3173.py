#include <iostream>
#include <fstream>

using namespace std;

struct Scores
{
	int a, b, c;
	bool surprising;
	bool notPossible;
	int getTotal (void) {return a+b+c;}
	Scores ()
	{
		a = b = c = 0;
		surprising = notPossible = false;
	}
};



int bruteForce (void);

int main (void)
{
	//open files
	ifstream inFile ("B-large.in");
	ofstream outFile ("B-large.out");
	
	int T;

	cout << "starting" << endl;

	inFile >> T;

	for (int t = 1; t <= T; t++)
	{
		cout << "starting case" << endl;

		int N, S, p;

		inFile >> N;
		inFile >> S;
		inFile >> p;

		int *totals = new int[N];
		for (int n = 0; n < N; n++)
			inFile >> totals[n];

		//try to divvy up the scores
		Scores * scores = new Scores[N];
		for (int n = 0; n < N; n++)
		{
			//start by making all 3 scores = p
			scores[n].a = p;
			scores[n].b = p;
			scores[n].c = p;

			while (scores[n].getTotal() > totals[n])
			{
				scores[n].a--;
				if (scores[n].b - scores[n].a == 2)
				{
					scores[n].a++;
					scores[n].b--;
				}
			}

			while (scores[n].getTotal() < totals[n])
			{
				if (scores[n].a < scores[n].b)
					scores[n].a++;
				else if (scores[n].b < scores[n].c)
					scores[n].b++;
				else
					scores[n].c++;
			}

			if (scores[n].c - scores[n].a == 2)
			{
				//allocate one of the surprisings to it if possible
				if (S > 0)
				{
					scores[n].surprising = true;
					S--;
				}
				else
				{
					scores[n].notPossible = true;
					int x = totals[n]%3;
					scores[n].a = (totals[n]-x)/3;
					scores[n].b = scores[n].a;
					scores[n].c = scores[n].a;
					if (x > 0)
					{
						scores[n].c++;
						x--;
					}
					if (x > 0)
						scores[n].b++;
				}
			}

			if (scores[n].c - scores[n].a > 2 || scores[n].a < 0)
			{
				scores[n].notPossible = true;
				int x = totals[n]%3;
				scores[n].a = (totals[n]-x)/3;
				scores[n].b = scores[n].a;
				scores[n].c = scores[n].a;
				if (x > 0)
				{
					scores[n].c++;
					x--;
				}
				if (x > 0)
					scores[n].b++;
			}
		}

		//allocate any surprising scores

		//first give to nonpossibles, as this makes no difference
		for (int n = 0; n < N && S > 0; n++)
		{
			if (scores[n].notPossible && !scores[n].surprising)
			{
				int a = scores[n].a;
				int b = scores[n].b;
				int c = scores[n].c;

				a--;
				b++;

				if (b > c)
				{
					int x = c;
					c = b;
					b = x;
				}

				if (a >= 0 && c <= 10 && c - a == 2)
				{
					scores[n].a = a;
					scores[n].b = b;
					scores[n].c = c;
					scores[n].surprising = true;
					S--;
				}
				//try the other way
				a = scores[n].a;
				b = scores[n].b;
				c = scores[n].c;

				b--;
				c++;

				if (a > b)
				{
					int x = b;
					b = a;
					a = x;
				}

				if (a >= 0 && c <= 10 && c - a == 2)
				{
					scores[n].a = a;
					scores[n].b = b;
					scores[n].c = c;
					scores[n].surprising = true;
					S--;
					continue;
				}
			}

		}

		//then try to make valid scores surprising without ruining them
		for (int n = 0; n < N && S > 0; n++)
		{
			if (scores[n].notPossible || scores[n].surprising)
				continue;

			int a = scores[n].a;
			int b = scores[n].b;
			int c = scores[n].c;

			a--;
			b++;

			if (b > c)
			{
				int x = c;
				c = b;
				b = x;
			}

			if (a >= 0 && c <= 10 && c - a == 2)
			{
				scores[n].a = a;
				scores[n].b = b;
				scores[n].c = c;
				scores[n].surprising = true;
				S--;
				continue;
			}
			//try the other way
			a = scores[n].a;
			b = scores[n].b;
			c = scores[n].c;

			b--;
			c++;

			if (a > b)
			{
				int x = b;
				b = a;
				a = x;
			}

			if (a >= 0 && c <= 10 && c - a == 2)
			{
				scores[n].a = a;
				scores[n].b = b;
				scores[n].c = c;
				scores[n].surprising = true;
				S--;
				continue;
			}
		}

		//if there are any surprises left, invalidate non surprising scores
		for (int n = 0; n < N && S > 0; n++)
		{
			if (scores[n].notPossible || scores[n].surprising)
				continue;

			scores[n].notPossible = true;
			S--;
		}

		//count the number of valid scores
		int goodScores = 0;
		for (int n = 0; n < N; n++)
		{
			if (!scores[n].notPossible)
				goodScores++;
		}

		//output the result
		outFile << "Case #" << t << ": " << goodScores << endl;

		//clear up
		delete[] totals;
	}

	inFile.close();
	outFile.close();
	return 0;
}