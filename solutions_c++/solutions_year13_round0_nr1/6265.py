#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("lol.txt");
	int T, A, B, C, D;
	fin >> T;
	fin.get();
	for (int i = 0; i < T; i++)
	{
		A = 0;
		char box[100][200];
		for(int j = 0; j < 4; j++)
		{
			for (int p = 0; p < 4; p++)
			{fin >> box[j][p];}
			fin.get();
		}
		int txt = 0;
		for (int j = 0; j < 4; j++)
		{
			int lol = 0;
		    for (int p = 0; p < 4; p++)
		    {
				switch (int(box[j][p]))
				{
				case 46 : lol = lol + 101;
					      break;
				case 88 : lol = lol + 2; 
			              break; 
				case 79 : lol = lol + 10;
				          break;
				case 84 : lol = lol + 12;
					      break;
				}
				if (lol > 100)
					 A = 1;
				 if (lol == 8 || lol == 18 || lol == 40|| lol == 42)
			    {
				txt = lol;
				 
			    break;
			    }
			  
			}
			 
			lol = 0;
			for(int p = 0; p < 4; p++)
			{
				 
				switch (int(box[p][j]))
				{
				case 46 : lol = lol + 101;
					      break;
				case 88 : lol = lol + 2; 
			              break; 
				case 79 : lol = lol + 10;
				          break;
				case 84 : lol = lol + 12;
					      break;
				}
				 if (lol > 100)
					 A = 1;
				 if (lol == 8 || lol == 18 || lol == 40|| lol == 42)
			    {
				txt = lol;
				 
			    break;
			    }
			}
			 if (txt == 8 || txt == 18 || txt == 40 || txt == 42)
				 break;
		}
		 
		int lol = 0;
		for (int p = 0, j = 0; p < 4; ++p, ++j)
		{
			switch (int(box[p][j]))
				{
				case 46 : lol = lol + 101;
					      break;
				case 88 : lol = lol + 2; 
			              break; 
				case 79 : lol = lol + 10;
					      
				          break;

				case 84 : lol = lol + 12;
					      break;
				}

				 if (lol > 100)
					 A = 1;
				  
				  if (lol == 8 || lol == 18 || lol == 40|| lol == 42)
			    {
				txt = lol; 
			    }
		}
		 
		lol = 0;
		for (int p = 0, j = 3; j >= 0; ++p, --j)
		{
			switch (int(box[p][j]))
				{
				case 46 : lol = lol + 101;
					      break;
				case 88 : lol = lol + 2; 
			              break; 
				case 79 : lol = lol + 10;
					      
				          break;

				case 84 : lol = lol + 12;
					      break;
				}

				 if (lol > 100)
					 A = 1;
				 
				  
				  if (lol == 8 || lol == 18 || lol == 40|| lol == 42)
			    {
				txt = lol; 
			    }
				   
		}
		if (txt == 8 || txt == 18)
			fout << "Case #" << i+1 <<  ": " << "X won"<< endl;
		 else if(txt == 40 || txt == 42)
			fout << "Case #" << i+1 <<  ": " << "O won"<< endl;
		  else if ( A == 1) 
			  fout << "Case #" << i+1 << ": " <<"Game has not completed"<< endl;
		  else fout << "Case #" << i+1 << ": " <<"Draw"<< endl;

	}
	cout << "lol";
		 
	while(true);
	return 0;
}
			
			

			 
		                