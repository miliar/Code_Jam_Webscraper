#include<iostream>
#include<fstream>

using namespace std;

class Combination {
	char element1, element2, newElement;

public :	Combination(char el1, char el2, char rel) { element1 = el1, element2 = el2, newElement = rel;}
	Combination(){};

	char check(char el1, char el2) 
	{
		if (el1 == element1) { if (el2 == element2) return newElement;}
		if (el1 == element2) { if (el2 == element1) return newElement;}

		return '\0';
	}
};

class Oposition {
	char element1, element2;

public :

	Oposition(char element1, char element2) {this->element1 = element1; this->element2 = element2;}
	Oposition(){};

	bool check(char element1, char element2) 
	{
		if (element1 == this->element1) { if (element2 == this->element2) return true;}
		if (element1 == this->element2) { if (element2 == this->element1) return true;}

		return false;
	}
};


void main()
{
	ifstream ulaz;
	ofstream izlaz;

	ulaz.open("input.txt");
	izlaz.open("output.txt");

	int t, c, d, n;
	char* word = new char[3];
	Combination* combination[36];
	Oposition* oposition[28];

	char invokeList[100];
	char elementList[100];

	ulaz >> t;

	for (int i = 0; i < t; i++)
	{
/***************************************************************************************************************************************************/
		ulaz >> c;
		for (int i = 0; i < c; i++)
		{
			ulaz >> word;
			combination[i] = new Combination(word[0], word[1], word[2]);
		}
		
		ulaz >> d;
		for (int i = 0; i < d; i++)
		{
			ulaz >> word;
			oposition[i] = new Oposition(word[0], word[1]);
		}

		ulaz >> n >> invokeList;

		elementList[0] = invokeList[0];

		int cur = 0;

		for (int i = 1; i < n; i++)
		{
			elementList[++cur] = invokeList[i];

			for (int i = 0; i < c; i++)
			{
				if ( cur > 0 && combination[i]->check(elementList[cur], elementList[cur - 1]) != '\0' ) 
				{
					elementList[cur - 1] = combination[i]->check(elementList[cur], elementList[cur - 1]);
					cur--;
					break;
				}
			}

			for (int j = cur; j >= 0; j--)
			{
				for (int k = j - 1; k >= 0; k--)
				{
					for (int i = 0; i < d; i++)
					{
						if ( oposition[i]->check(elementList[j], elementList[k]) ) 
						{
							cur=-1;
							break;
						}
					}
				}
			}
		}
		izlaz << "Case #" << i + 1 << ": [";
		if (cur > -1 ) izlaz << elementList[0];
		for (int i = 1; i <= cur; i++) izlaz << ", " << elementList[i];
		izlaz << ']' << endl;
		for (int i = 0; i < c; i++) delete combination[i];
		for (int i = 0; i < d; i++) delete oposition[i];
/******************************************************************************************************************************************************/	
	}

	ulaz.close();
	izlaz.close();
}