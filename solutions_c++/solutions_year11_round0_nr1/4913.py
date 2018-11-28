#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]){
	
	fstream input, output;
	stringstream str, inputReader;
	string line;
	unsigned int NbCases=0, OrangePos, BluePos, NbButtonsToPress, temp2, NbSeconds, ActualRequiredPosition, k;
	bool PositionReached;
	list<unsigned int> OrangeButtons, BlueButtons, Sequence;
	
	//input.open(argv[1], ios_base::in);
	input.open("input.txt", ios_base::in);
	//str << argv[1]<<".out";
	//output.open(str.str().c_str(), ios_base::out);
	output.open("output.txt", ios_base::out);
	//getting the number of cases.
	getline(input, line);
	inputReader<<line;
	inputReader>>NbCases;	 inputReader.str("");inputReader.clear(); 
	for(unsigned int i=1; i <= NbCases; i++){
		OrangePos = BluePos = 1;	NbSeconds=0;
		
		OrangeButtons.clear();	BlueButtons.clear();	Sequence.clear();
		inputReader.str("");inputReader.clear();
		getline(input, line);
		inputReader<<line;
		inputReader>> NbButtonsToPress;
		for (unsigned int j= 1; j <= NbButtonsToPress; j++){
			inputReader.seekg(1,inputReader.cur);
			if(inputReader.peek() == 'O'){
				inputReader.seekg(2,inputReader.cur);
				inputReader>>temp2;
				OrangeButtons.push_back(temp2);
				Sequence.push_back(temp2);
			}
			if(inputReader.peek() == 'B'){
				inputReader.seekg(2,inputReader.cur);
				inputReader>>temp2;
				BlueButtons.push_back(temp2);
				Sequence.push_back(100+temp2);
			}
		}
		k=0;
		while(NbButtonsToPress != k){
			ActualRequiredPosition = Sequence.front();
			Sequence.pop_front();
			PositionReached=false;
			while(!PositionReached){

				if(ActualRequiredPosition > 100){
					if(BluePos == (ActualRequiredPosition - 100)){
						//button pressed
						BlueButtons.pop_front();
						PositionReached = true;
					}else{
						if(BluePos < (ActualRequiredPosition - 100))
							BluePos++;
						if(BluePos > (ActualRequiredPosition - 100))
							BluePos--;
					}
					if(!OrangeButtons.empty())
						if(OrangePos > OrangeButtons.front())
							OrangePos--;
						else 
							if(OrangePos < OrangeButtons.front())
								OrangePos++;
				}

				if(ActualRequiredPosition < 100){
					if(OrangePos == (ActualRequiredPosition )){
						//button pressed
						OrangeButtons.pop_front();
						PositionReached = true;
					}else{
						if(OrangePos < (ActualRequiredPosition))
							OrangePos++;
						if(OrangePos > (ActualRequiredPosition))
							OrangePos--;
					}
					if(!BlueButtons.empty())
						if(BluePos > BlueButtons.front())
							BluePos--;
						else 
							if(BluePos < BlueButtons.front())
								BluePos++;
				}
				NbSeconds++;
			}
			k++;

		}
		output<<"Case #"<<i<<": "<<NbSeconds<<endl;
	}
	output.close();input.close();
	return 0;	
}