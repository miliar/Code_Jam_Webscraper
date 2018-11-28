
/*
Written by Jack Vucemillo.
On 14/04/2012.
Last known email address: shadow.wraith.12@gmail.com
*/


#include <fstream>
#include <iostream>
#include <string>


std :: fstream inFile;
std :: fstream outFile;


struct ScoreTriple
{
	int scores[3];
};


bool needsAdjusting(ScoreTriple triple, int targetScore)
{
	if(triple.scores[0] >= targetScore)
		return false;
	return true;

	// note:
	// scores[0] will always be at least as big as [1] or [2] because it is the first of only two possibilities to be increased by one when generated
}


bool canBeAdjusted(ScoreTriple triple)
{
	if(triple.scores[0] > triple.scores[1])
		return false;
	if(triple.scores[0] == 10)
		return false;
	if(triple.scores[1] == 0)
		return false;
	return true;

	/*
	note:
	{0, 0, 0} can be adjusted to {1, -1, 0}
	{1, 0, 0} cannot be adjusted (to increase the maximum value would decrease either minimum value below the 2 difference threshold
	{1, 1, 0} can be adjusted to {2, 0, 0}
	this means that if [0] > [1] the result is true and false otherwise
	*/
}


ScoreTriple adjust(ScoreTriple triple)
{
	triple.scores[0] ++;
	triple.scores[1] --;
	return triple;

	// note:
	// {1, 0, 0} will never be given here (i hope *cough cough*)
	// both other cases involve adding {1, -1, 0}
}


bool canBeAdjusted(ScoreTriple triple, int minScore)
{
	if(canBeAdjusted(triple)) // if the triple is adjustable
		if(!needsAdjusting(adjust(triple), minScore)) // if adjusted score puts the triple in range
			return true; // return "can be adjusted"

	return false;
}


int main()
{
	// open/create the input/output files
	std :: string baseFilename = "B-large";
	std :: string inFileName = baseFilename + ".in";
	std :: string outFileName = baseFilename + ".out";
	inFile.open(inFileName.c_str(), std :: ios :: in);
	outFile.open(outFileName.c_str(), std :: ios :: out | std :: ios :: trunc);


	// read the number of problems in the set
	int problemCount = 0;
	inFile >> problemCount;


	// for each problem in the set
	for(int problem = 0; problem < problemCount; problem ++)
	{
		// read the number of googlers
		int googlerCount = 0;
		inFile >> googlerCount;

		// read the number of surprising scores
		int surprisingScoreCount = 0;
		inFile >> surprisingScoreCount;

		// read the target score
		int targetScore = 0;
		inFile >> targetScore;

		// read in the googler scores and calculate the triples
		int adjustmentsRemaining = surprisingScoreCount;
		int scoresOnTarget = 0; // number of scores that fit the min score criteria
		for(int score = 0; score < googlerCount; score ++)
		{
			int newScore = 0;
			inFile >> newScore;

			ScoreTriple newTriple;
			int scoreThird = newScore / 3;
			newTriple.scores[0] = scoreThird + (3 * scoreThird < newScore? 1: 0);
			newTriple.scores[1] = scoreThird + (3 * scoreThird + 1 < newScore? 1 : 0);
			newTriple.scores[2] = scoreThird;

			// if score is met
			if(!needsAdjusting(newTriple, targetScore))
			{
				// count it and continue on with the next score
				scoresOnTarget ++;
				continue;
			}


			// if the score is not adjustable or there are no adjustments remaining
			if((adjustmentsRemaining == 0) || (!canBeAdjusted(newTriple, targetScore)))
			{
				continue;
			}

			
			// the score can be adjusted and there are adjustments remaining
			// the actual result of the adjustment is irrelevant, only the fact that it "has been done"
			// newTriple = adjust(newTriple);
			adjustmentsRemaining --;
			scoresOnTarget ++;
		}

		outFile << "Case #" << problem + 1 << ": " << scoresOnTarget;
		if(problem + 1 < problemCount)
			outFile << std :: endl;
	}


	// close the input/output files
	inFile.close();
	outFile.close();
//	system("pause");
}
