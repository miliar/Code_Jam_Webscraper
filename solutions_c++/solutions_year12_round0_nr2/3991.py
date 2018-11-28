#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

typedef pair<char, int> botP;
typedef vector<int> intV;
typedef vector<botP>  pairV;
typedef pairV::iterator pairVIter;
typedef intV::iterator intVIter;

int MaxPplWithBestScoreHigher(vector<int> sumScore, int numSurprise, int bestExpected)
{
	int maxPpl=0;
	int possibleMax=0;
	for(int i=0; i<sumScore.size(); i++)
	{
		int totalScore = sumScore[i];
		if(totalScore ==0)
		{
			if(bestExpected ==0)
			{
				maxPpl++;
			}
		}
		else 
		{
			int lowestMaxWithoutSurp=3*bestExpected-2;
			int lowestMaxWithSurp=3*bestExpected-4;
			if(totalScore>=lowestMaxWithoutSurp)
				maxPpl++;
			else if (totalScore>=lowestMaxWithSurp)
				possibleMax++;
			/*
			int avg=totalScore/3;
			int mod=totalScore%3;
			if (avg>=bestExpected)
				maxPpl++;
			else if (avg+1 >=bestExpected && mod !=0)
				maxPpl++;
			else if (avg+1 >=bestExpected && numSurprise>0 &&mod==0)
			{
				maxPpl++;
				numSurprise--;
			}
			else if (avg+2 >=bestExpected && numSurprise>0 &&mod >0)
			{
				maxPpl++;
				numSurprise--;
			}
			*/
		}

	}
	return maxPpl+min(possibleMax,numSurprise);
}

int main()
{
  int num_case;
  string line;
  string inFileName, outFileName;
  cout<<"input data file name:"<<endl;
  cin>>inFileName;
  cout<<"input output file name:"<<endl;
  cin>>outFileName;
  
  ifstream in_file(inFileName.c_str());
  ofstream out_file(outFileName.c_str());

  in_file>>num_case;
  getline(in_file, line);//ignore 1st line
  //cout<<num_case<<" test cases "<<endl;
    
  int numPpl;
  int numSurprise;
  int bestExpected;
  vector<int> sumScorePpl;
  int sumScore=0;
  int caseNum=1;

  while (getline(in_file, line))
    {
      istringstream sline(line);
      sline>>numPpl;
      sline>>numSurprise;
	  sline>>bestExpected;
	  for(int i=0; i<numPpl; i++)
	  {
		  sline>>sumScore;
		  sumScorePpl.push_back(sumScore);
	  }
      out_file<<"Case #"<<caseNum<<": "<<MaxPplWithBestScoreHigher(sumScorePpl, numSurprise, bestExpected)<<endl;
      sumScorePpl.clear();
      caseNum++;       
    }    
    return 1;    
}
