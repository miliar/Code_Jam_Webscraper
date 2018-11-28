#include <iostream>
#include <string>
#include <fstream>
#include "tvector.h"


using namespace std;

tvector<string> EveryLetter(string s)
{
	tvector<string> MyVec2(s.length());
	int num = 0;
	while (num < s.length())
	{
		MyVec2[num] = s.substr(num,1);
		num++;
	}

	return MyVec2;
}

int NewWd(tvector<string> MyVec, int x)
{
	while(MyVec[x] != "----------")
	{
		x++;
	}
	if(MyVec[x+1] == "---------------->")
		return 0;

	return x+1;
}

int NewSy(tvector<string> MyVec, int x)
{
	while(MyVec[x] != "----------")
	{
		x++;
	}
	return x+1;
}

bool EndOfCheck(tvector<string> MyVec, int x)
{
	return (MyVec[x] == "----------");
}

bool IsThereAMatch(tvector <string> MyVec, int StartPoint, string word)
{
	int x = 0;
	tvector<string> Letters(15);
	Letters = EveryLetter(word);
	while (x<word.length()-1 && !EndOfCheck(MyVec,StartPoint))
	{
		if (Letters[x] == MyVec[StartPoint])
		{
			x+=1;
			if(NewWd(MyVec,StartPoint) != 0)
			{
				StartPoint = NewSy(MyVec,StartPoint);
			}
			else
			{
				return true;
			}
		}
		else
		{
			StartPoint++;
		}
	}
	return false;
}


int main()
{
	ifstream input;
	input.open("MyText.txt");

	int MyNum = 0;
	int WordLength;
	int TotalWords;
	int TotalTestCases;
	string MyWord;

	input>>WordLength;
	input>>TotalWords;
	input>>TotalTestCases;

	string KnownWords[5000];
	for(int i = 0; i <5000; i++)
	{
		KnownWords[i] = "CemG";
	}

	for(i = 0; i < TotalWords; i++)
	{
		input>>MyWord;
		KnownWords[i] = MyWord;
	}

	tvector<string> InterP(10000);
	int TotalInterP = 0;
	int control = 0;
	int MainControl = -1;

	int LP;
	string PieceOfWord;
	int PieceSize;
	int PieceSizeB;

	

	while(MainControl < TotalTestCases)
	{
		if (control == 0)
		{
			control = 1;
			if(TotalTestCases != MainControl)
			{
				input>>MyWord;
			}
			MainControl++;
			InterP[TotalInterP] = "---------------->";
			TotalInterP++;
		}
		else if (MyWord.substr(0,1) != "(")
		{	
			InterP[TotalInterP] = MyWord.substr(0,1);


			TotalInterP++;

			if ( MyWord.length() != 1)
			{
				MyWord = MyWord.substr(1,MyWord.length()-1);
				InterP[TotalInterP] = "----------";
				TotalInterP++;
			}
			else
			{
				control = 0;
				InterP[TotalInterP] = "----------";
				TotalInterP++;
			}
		}
		else if (TotalTestCases != MainControl)
		{
			LP = MyWord.find(")");
			
			PieceOfWord = MyWord.substr(1,LP-1);
			
			PieceSize = PieceOfWord.length();
			PieceSizeB = PieceSize;
			while(PieceSize != 0)
			{
				InterP[TotalInterP] = PieceOfWord.substr(0,1);
				TotalInterP++;
				PieceSize--;
				PieceOfWord = PieceOfWord.substr(1,PieceOfWord.length()-1);
			}
			
			if ( MyWord.length() == PieceSizeB+2 )
			{
				control = 0;
				InterP[TotalInterP] = "----------";
				TotalInterP++;
			}
			else
			{
				MyWord = MyWord.substr(LP+1,MyWord.length()-1-LP);
				InterP[TotalInterP] = "----------";
				TotalInterP++;
			}
		}
	}
	InterP[TotalInterP] = "-1-1";

/*	tvector<string> control5(15);
	int counter3 = 0;
	int GlobalC = 1;
	string FirstCheck;
	bool CheckPass = true;

	for(i = 0; i < 100 ; i++)
	{

		
		cout<<InterP[i]<<endl;
	}

	tvector<string> WordList(2);
	int SuccessC = 0;
	int MatchCount = 0;

	for (i = 0; KnownWords[i] != "CemG" ; i++)
	{
		WordList.push_back(KnownWords[i]);
		counter3++;
	}

	
	for (i = 0; i < 8 ; i++)
	{
		cout<<WordList[i]<<endl;
	} 
	int CheckThis = 0;
	int tempG = GlobalC;
	string tempWord;

		for(i=0; i < TotalWords ; i++)
		{
			for (int k = 0; k < WordLength; k++)
			{
				tempWord = WordList[i].substr(k,1);
				control5[k] = tempWord;
			}
			while(!EndOfCheck(InterP,GlobalC) && SuccessC == 0)
			{
				if(InterP[GlobalC] == FirstCheck)
				{
					CheckPass = true;
					while(InterP[GlobalC] != "----------")
					{
						GlobalC++;
					}
					GlobalC++;
					if(InterP[GlobalC] == "---------------->")
					{
						counter3 = 0;
						SuccessC = 1;
						i = 0;
						GlobalC++;
						MatchCount++;
						tempG = GlobalC;
					}
					else
					{
						counter3++;
					}
					FirstCheck = control5[counter3];
				}
				else if(!EndOfCheck(InterP,GlobalC+1))
				{
					GlobalC++;
				}
				else
				{
					CheckPass = false;
				}
			}
			if(i+1 != TotalWords)
			{
				GlobalC = tempG;
			}
			else if (InterP[GlobalC] != "-1-1")
			{
				i = 5001;
			}
			else
			{
				i = 0;
			}
		}	

		
	cout<<MatchCount<<endl;
*/
	int a = 0;
	string NewWord;
	int Letter = 0;
	string NewLetter;
	int GlobalC = 1;
	int WhileControl = 0;
	int tempGlobalC = 1;
	int tempGlobalC2= 1;
	bool LetterMatches = true;
	bool WordMatches = true;
	int CaseMatch = 0;
	ofstream output;
	output.open("Output.txt");
	int CaseNumber = 1;
	
while(InterP[GlobalC] != "-1-1")
{
	while(KnownWords[a] != "CemG")
	{
		NewWord = KnownWords[a];
		while(WordLength > Letter && WordMatches)
		{
			NewLetter = NewWord.substr(Letter,1);
			while(WhileControl == 0)
			{
				if( NewLetter == InterP[GlobalC])
				{
					WhileControl = 1;
					tempGlobalC2= GlobalC;
					while(InterP[GlobalC] != "----------")
					{
						GlobalC++;
					}
					GlobalC++;
					LetterMatches = true;
				}
				else if (InterP[GlobalC] == "----------")
				{
					LetterMatches = false;
					tempGlobalC2= GlobalC;
					GlobalC = tempGlobalC;
					WhileControl = 1;
				}
				else
				{
					GlobalC++;
				}
			}
			if(LetterMatches == true)
			{
				Letter++;
				WordMatches = true;
				WhileControl = 0;
			}
			else
			{
				WhileControl = 0;
				WordMatches = false;
			}
		}
		if(WordMatches)
		{
			CaseMatch++;
			GlobalC = tempGlobalC;
		}
		else
		{
			WordMatches = true;
		}
		a++;
		Letter = 0;
	}

	output<<"Case #"<<CaseNumber<<": "<<CaseMatch<<endl;

	while(InterP[GlobalC] != "---------------->")
	{
		GlobalC++;
	}
	GlobalC++;
	tempGlobalC = GlobalC;
	a = 0;
	CaseMatch = 0;
}


	return 0;
}