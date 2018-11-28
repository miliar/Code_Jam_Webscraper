#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

char digit_to_ascii(int digit);

int main()
{
	int T, i, j, k, lsd, lsdint;
	char N[22], ASCIIDigit[2];
	int Nint[21], OriginalNumDigits[10], NewNumDigits[10];
	bool bFoundNextNumber, bTooLarge, bStillIncrementing;
			
	ifstream inFile;
	ofstream outFile;
	
	inFile.open("B-small-attempt0.in");
	
	if (!inFile)
	{
		cerr << "Could not open input file!" << endl;
		exit(1);		
	}
	
	outFile.open("results.out");
	if (!outFile)
	{
		cerr << "Could not open output file!" << endl;
		exit(1);		
	}
	
	//NULL terminate this dummy string
	ASCIIDigit[1]=0;
	
	inFile >> T;
	
	//Read T lines from input file and process each in turn	
	for (i=0; i<T; ++i)
	{
		inFile >> N;
		cout << "Read " << N << " from file" << endl;
		
		//store the least significant digit position
		lsd=strlen(N)-1;
		
		for (j=0; j<21; ++j)
			Nint[j]=0;
		
		for (j=1; j<10; ++j)
			OriginalNumDigits[j]=0;	

		//copy to a numeric array (in reverse order)
		for (j=0; j<=lsd; ++j)
		{
			ASCIIDigit[0]=N[j];
			Nint[lsd-j]=atoi(ASCIIDigit);
			++OriginalNumDigits[Nint[lsd-j]];
		}
		
		bFoundNextNumber=false;
		bTooLarge=false;
		
		while ((!bFoundNextNumber) && (!bTooLarge))
		{
			//increment N by 1
			j=0; //lsd;
			++Nint[j];
			bStillIncrementing=true;
			
			while ((bStillIncrementing) && (!bTooLarge))
			{
				if (Nint[j]>9)
				{
					if (j<21)
					{
						for (k=j; k>=0; --k)
							Nint[k]=0;
						++j;
						++Nint[j];
						
					} else {
						bTooLarge=true;
					}
				} else {
					bStillIncrementing=false;
				}
			}
			
			//check digits of Nint
			for (j=1; j<10; ++j)
				++NewNumDigits[j]=0;

			//find "length" of integer rep of N
			lsdint=-1;
			for (j=20; ((j>=0) && (lsdint<0)); --j)
				if (Nint[j]>0)
					lsdint=j;
			
			for (j=0; j<22; ++j)
				N[j]=0;

			for (j=0; j<=lsdint; ++j)
				++NewNumDigits[Nint[j]];
						
			bFoundNextNumber=true;
			for (j=1; ((j<10) && (bFoundNextNumber)); ++j)
				if (NewNumDigits[j]!=OriginalNumDigits[j])
					bFoundNextNumber=false;
		}
		
		if (bFoundNextNumber)
		{
			cout << "  --> Found next number: ";
			for (j=0; j<=lsdint; ++j)
				N[lsdint-j]=digit_to_ascii(Nint[j]);
			cout << N << endl;
			outFile << "Case #" << i+1 << ": " << N << endl;						
		}
		if (bTooLarge)
			cout << "Number too large! Quitting..." << endl;		
	}
	
	inFile.close();
	outFile.close();
	return 0;
}

char digit_to_ascii(int digit)
{
	if (digit==0)
		return '0';
	else if (digit==1)
		return '1';
	else if (digit==2)
		return '2';
	else if (digit==3)
		return '3';
	else if (digit==4)
		return '4';
	else if (digit==5)
		return '5';
	else if (digit==6)
		return '6';
	else if (digit==7)
		return '7';
	else if (digit==8)
		return '8';
	else if (digit==9)
		return '9';
	else
		return 'X';
}

