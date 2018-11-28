#include <iostream>
#include <math.h>
#include <string>
using namespace std;


#include<fstream>
ifstream fin("A-large.in");
ofstream fout("output.txt");

int main()
{

	int n;
    int powbitSet = 0;

    if(NULL == fin)
    {
      cout<<"NO INPUT FILE"<<endl;
      return 0;
    }

    fin >> n;
    string result("OFF");

	for(int i = 0; i < n; i++)
	{
        int numN; fin >> numN;
		int numK; fin >> numK;

        powbitSet = pow(2, numN) - 1;


        if(powbitSet == (powbitSet & numK))
          result = "ON";
        else
          result  = "OFF";



		fout << "Case #" << i + 1 << ": " << result << endl;
	}




	return 0;
}







