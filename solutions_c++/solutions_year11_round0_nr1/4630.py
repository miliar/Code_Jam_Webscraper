//alex kopowski
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct command
{
	string color;
	int priority;
	int button;
};

int main()
{
	string line;
	string dummy;
	int trialNum;
	ifstream inputFile;
	ofstream outputFile("output.txt");
	inputFile.open("input_simple.txt");
	if (inputFile.is_open())
	{
		while (inputFile.good())
		{
			getline(inputFile,line);
			trialNum = atoi(line.c_str());

			for (int x=0;x<trialNum;x++)
			{
				int buttonNum;
				int index = 0;
				string temp;
				getline(inputFile,line);
				string tempTemp;
				temp = line[index];
				while(temp!=" ")
				{
					tempTemp+=temp;
					index++;
					
					temp = line[index];
					
				}
				buttonNum = atoi(tempTemp.c_str());
				//cout << buttonNum;
				if (buttonNum>0)
				{
					command * orange = new command[buttonNum];
					command * blue = new command[buttonNum];
					int orangeIndex = 0;
					int blueIndex= 0;
					int tempPriority = 0;
					index++;
					while (index<line.length())
					{
						temp = line[index];
						
						if (temp=="O")
						{
							index+=2;
							command tempCommand;
							tempCommand.color="O";
							string tempBut;
							temp = line[index];
							while(temp!=" ")
							{
								tempBut+=temp;
								index++;
								if (index<line.length())
									temp = line[index];
								else
									temp = " ";
							}
							index++;
							tempCommand.button=atoi(tempBut.c_str());
							tempCommand.priority = tempPriority;
							tempPriority++;
							orange[orangeIndex] = tempCommand;
							orangeIndex++;
						}
						else if(temp=="B")
						{
							index+=2;
							command tempCommand;
							tempCommand.color="B";
							string tempBut;
							temp = line[index];
							while(temp!=" ")
							{
								tempBut+=temp;
								index++;
								if (index<line.length())
									temp = line[index];
								else
									temp = " ";
							}
							index++;
							tempCommand.button=atoi(tempBut.c_str());
							tempCommand.priority = tempPriority;
							tempPriority++;
							blue[blueIndex] = tempCommand;
							blueIndex++;
						}
						
					}
					

					int totalPriority = 0;
					int orangePosition = 0;
					orangeIndex = 0;
					int bluePosition = 0;
					blueIndex = 0;
					int steps = 0;
					int buttonPress = 0;

					while(buttonPress < buttonNum)
					{
						command tempOrange = orange[orangeIndex];
						command tempBlue = blue[blueIndex];
						//orange
						if(tempOrange.button == orangePosition)
						{
							if (totalPriority == tempOrange.priority)
							{
								buttonPress++;
								orangeIndex++;
							}
						}
						else
						{
							if (tempOrange.button > orangePosition)
							{
								orangePosition++;
							}
							else
								orangePosition--;
						}
						//blue
						if(tempBlue.button == bluePosition)
						{
							if (totalPriority == tempBlue.priority)
							{
								buttonPress++;
								blueIndex++;
							}
						}
						else
						{
							if (tempBlue.button > bluePosition)
							{
								bluePosition++;
							}
							else
								bluePosition--;
						}

						
						totalPriority = buttonPress;
						steps++;
						
						/*cout << "OPOS:" << orangePosition << " OIND:" << orangeIndex << " OPRI:" << tempOrange.priority << endl;
						cout << "BPOS:" << bluePosition << " BIND:" << blueIndex << " BPRI:" << tempBlue.priority << endl;
						cout << "TOTP:" << totalPriority << endl;
						system("PAUSE");*/
						
					}//while(buttonPress < buttonNum)
					
					outputFile << "Case #" << x+1 << ": " << steps-1 << endl;
					
				}//if (buttonNum>0)
				
			}//for (int x=0;x<trialNum;x++)
		}//while (inputFile.good())
		inputFile.close();
		outputFile.close();
	}//if (inputFile.is_open())
	
	system("PAUSE");
	return 0;
}