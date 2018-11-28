#include <fstream>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	ifstream dataF("input.in");
	ofstream output("Ouput.out");
	int Ndim;
	int Kinarow;
	int cases;
	if (dataF.is_open())
	{
		while (! dataF.eof() )
		{
			cases = 0;
			dataF >> cases;
			for(long i = 1; i <= cases; i++)
			{
				dataF >> Ndim;
				dataF >> Kinarow;
				char rota[7][7];
				for(int j = 0; j < Ndim; j++)
					for(int k = 0; k < Ndim; k++)
						dataF >> rota[k][Ndim - j - 1];
				for(int j = 0; j < Ndim; j++)
				{
					int localtop = 0;
					for(int k = Ndim - 1; k >= 0; k--)
					{
						char curr = rota[k][j];
						if(curr != '.')
						{
							if(Ndim - 1 -localtop != k)
							{
								rota[Ndim - 1 -localtop][j] = curr;
								rota[k][j] = '.';
							}
							localtop++;
						}
						
					}
				}
				bool red = false;
				bool blue = false;
				//Rows
				for(int j = 0; j < Ndim; j++)
				{
					if(red && blue)
						break;
					for(int k = 0; k <= Ndim - Kinarow; k++)
					{
						int count = 0;
						char curr = rota[j][k];
						if(!red && curr == 'R')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j][k + r] == 'R')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								red = true;
						}
						else if(!blue && curr == 'B')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j][k + r] == 'B')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								blue = true;
						}
					}
				}
				//Columns
				for(int j = 0; j < Ndim; j++)
				{
					if(red && blue)
						break;
					for(int k = 0; k <= Ndim - Kinarow; k++)
					{
						int count = 0;
						char curr = rota[k][j];
						if(!red && curr == 'R')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[k+ r][j] == 'R')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								red = true;
						}
						else if(!blue && curr == 'B')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[k+ r][j] == 'B')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								blue = true;
						}
					}
				}
				//Diagnol
				for(int j = 0; j <= Ndim - Kinarow; j++)
				{
					if(red && blue)
						break;
					for(int k = 0; k <= Ndim - Kinarow; k++)
					{
						int count = 0;
						char curr = rota[j][k];
						if(!red && curr == 'R')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j + r][k + r] == 'R')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								red = true;
						}
						else if(!blue && curr == 'B')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j + r][k + r] == 'B')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								blue = true;
						}
					}
				}
				//Diagnol
				for(int j = 0; j <= Ndim - Kinarow; j++)
				{
					if(red && blue)
						break;
					for(int k = Ndim - 1; k >= Kinarow - 1; k--)
					{
						int count = 0;
						char curr = rota[j][k];
						if(!red && curr == 'R')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j - r][k + r] == 'R')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								red = true;
						}
						else if(!blue && curr == 'B')
						{
							for(int r = 0; r < Kinarow; r++)
							{
								if(rota[j - r][k + r] == 'B')
									count++;
								else
									break;
							}
							if(count == Kinarow)
								blue = true;
						}
					}
				}
				//
				string result;
				if(red)
				{
					if(blue)
						result = "Both";
					else
						result = "Red";
				}
				else if(blue)
					result = "Blue";
				else
					result = "Neither";

				//
				output << "Case #" << i << ": " << result << endl;

			}
		}
		dataF.close();
	}
	else cout << "Unable to open file"; 
}
