#include<iostream>
#include<queue>
#include<fstream>

using namespace std;

typedef struct Value {
    int quotient; 
    int remainder; 
}Value;

class CompareValue {
public:
    bool operator()(Value& t1, Value& t2) 
    {
		if (t1.quotient < t2.quotient) return true;
		if (t1.quotient == t2.quotient && t1.remainder < t2.remainder) return true;
		return false;
    }
};


int main(int argc, char *argv[])
{
	ifstream file;
	ofstream outputFile;
	
	priority_queue<Value, vector<Value>, CompareValue> myPQ;
	Value myValue;

	string inputString;
	
	int intTestCases=0,leng=0,x=0;
	int intNoOfGooglers=0, intNoOfSurprises=0, intBestResultExpected=0, intCurrentTotal=0;
	int intFinalCount=0;
	bool boolFlag=false;
	bool boolNotFinished=true;
	
	//cout << "File = " << argv[2];
	outputFile.open(argv[2]);
	file.open(argv[1]);
	
	//Read integers..
	if(!file.eof())
	{
		file >> intTestCases;
	}
		
	for(int i=0; i<intTestCases; ++i)
	{		
		file >> intNoOfGooglers;
		file >> intNoOfSurprises;
		file >> intBestResultExpected;
				
		for(int j=0; j<intNoOfGooglers; ++j)
		{
			file >> intCurrentTotal;
		
			x = intCurrentTotal/3;
			if(x>=intBestResultExpected)
				intFinalCount++;
			else if (x < (intBestResultExpected-2)) 
				continue;
			else
			{
				myValue.quotient = x;
				myValue.remainder = intCurrentTotal%3;
				
				if (x > 0){
					if( ( (intBestResultExpected - x) == 1) || (((intBestResultExpected - x) == 2) && myValue.remainder > 0)    )
						myPQ.push(myValue);
				}
			}
			
		}
		
		while (! myPQ.empty() && boolNotFinished) {
			Value myTempValue = myPQ.top();
			//cout << endl << myTempValue.quotient << " " << myTempValue.remainder << endl;
			
			if(intBestResultExpected - myTempValue.quotient == 1)
			{
				if (myTempValue.remainder >=1) {
					intFinalCount++;
				}
				else {
					if(intNoOfSurprises>0)
					{
						intFinalCount++;
						intNoOfSurprises--;
					}
				}
			}
			else {
				if(intNoOfSurprises==0)
				{
					boolNotFinished = false;
					//break;
				}
				else {
					if (myTempValue.quotient + myTempValue.remainder >= intBestResultExpected) {
						intFinalCount++;
						intNoOfSurprises--;
					}
				}
				
			}

			myPQ.pop();
		}
		
		while (! myPQ.empty())
			myPQ.pop();

		outputFile << "Case #" << i+1 << ": " << intFinalCount << endl;
		intFinalCount=0;
		boolNotFinished=true;
	}

	outputFile.close();
	file.close();
	
	return 0;

}

