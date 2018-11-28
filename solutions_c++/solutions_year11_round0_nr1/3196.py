#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	//ifstream fin ("A-small-attempt0.in");
	ifstream fin ("A-large.in");
    //ofstream fout ("A-output-small.txt");
	ofstream fout ("A-output-large.txt");

	int cases = 0;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<": ";
		fout << "Case #"<<(i+1) <<": ";

		int buttons;
		fin>>buttons;

		int *targetsO = new int[buttons+1], *targetsB = new int[buttons+1];
		for(int j=0; j<buttons; j++)
		{
			targetsO[j] = 0;
			targetsB[j] = 0;
			char robot;
			fin>>robot;
			int pos;
			fin>>pos;
			if(robot == 'O')
				targetsO[j] = pos;
			else
				targetsB[j] = pos;
		}
		targetsO[buttons] = 101;
		targetsB[buttons] = 101;

		int posO = 0, posB = 0;
		while(targetsO[posO] == 0 && posO < buttons)
			posO++;
		while(targetsB[posB] == 0 && posB < buttons)
			posB++;

		int onO = 1, onB = 1, counter = 0;//, o = false, b = false;

		while((posO < buttons) || (posB < buttons))
		{
			if(posO < posB) //orange portals first
			{
				counter += (abs(targetsO[posO] - onO) + 1);
				if((onB + (abs(targetsO[posO] - onO) + 1)) < targetsB[posB])
					onB += (abs(targetsO[posO] - onO) + 1);
				else if((onB - (abs(targetsO[posO] - onO) + 1)) > targetsB[posB])
					onB -= (abs(targetsO[posO] - onO) + 1);
				else
					onB = targetsB[posB];
				onO = targetsO[posO];

				posO++;
				while(targetsO[posO] == 0 && posO < buttons)
					posO++;
			}
			else //blue portals first
			{
				counter += (abs(targetsB[posB] - onB) + 1);
				if((onO + (abs(targetsB[posB] - onB )+ 1)) < targetsO[posO])
					onO += (abs(targetsB[posB] - onB) + 1);
				else if((onO - (abs(targetsB[posB] - onB) + 1)) > targetsO[posO])
					onO -= (abs(targetsB[posB] - onB) + 1);
				else
					onO = targetsO[posO];
				onB = targetsB[posB];

				posB++;
				while(targetsB[posB] == 0 && posB < buttons)
					posB++;
			}

			/*if(onO == targetsO[posO] && posO < buttons && o)
			{
				posO++;
				while(targetsO[posO] == 0 && posO < buttons)
					posO++;
			}
			if(onB == targetsB[posB] && posB < buttons && b)
			{
				posB++;
				while(targetsB[posB] == 0 && posB < buttons)
					posB++;
			}*/
		}

		cout<<counter<<endl;
		fout<<counter<<endl;
		
		delete(targetsO);
		delete(targetsB);
	}
	system("pause");
	return 0;
}