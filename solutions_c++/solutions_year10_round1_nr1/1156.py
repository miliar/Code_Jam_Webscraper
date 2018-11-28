//============================================================================
// Name        : Problem1.cpp
// Author      : GetAZoom
// Version     :
// Copyright   : 
// Description : GCJ in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <map>
#include <bitset>

//		bitset<32> va((long)noOfClick);
//		map<int,int> mymap;
//		map<int,int>::iterator it;
//		if(mymap.find(index) == mymap.end())
//		{
//			mymap[index]=1;
//		}

using namespace std;

int main() {
	//read input from file...
	int noOfChars;
	int noOfTest;
	int maxSame;
	int Rwin = 0;
	int Bwin = 0;
	cin >> noOfTest;

	for(int i=0; i < noOfTest; i++)
	{
		cin >> noOfChars >> maxSame ;
		int game[noOfChars][noOfChars];
		Rwin = 0;
		Bwin = 0;
		for(int j = 0 ; j < noOfChars; j++)
		{
			int r = 0, b= 0 , z=0;
			for(int k = 0 ; k < noOfChars; k++)
			{
				char val;
				cin >> val;
				if(val == '.')
				{
					game[j][k] = 0;
					if(r ==1 || b == 1)
						z++;
				}
				if(val == 'R')
				{
					game[j][k] = 1;
					r = 1;
				}
				if(val == 'B')
				{
					game[j][k] = -1;
					b = 1;
				}
			}
			//cout << z <<endl;
			//Do the right shifting for gravity ...
			for(int k = noOfChars-1 ; k > 0 && z > 0; k--)
			{
				if(game[j][k] == 0)
				{
					for(int l = k; l > 0;l--)
					{
						game[j][l] = game[j][l-1];
						game[j][l-1]=0;
					}
					//game[j][l]=0;
					if(game[j][k] == 0)
						k++;
					z--;
				}
			}

		}
			//Try to rotate/gravity while taking the i/p only.
		for(int j = 0 ; j < noOfChars; j++)
		{
			for(int k = 0 ; k < (noOfChars); k++)
			{
			//	cout << game[j][k] << endl;
				if(game[j][k]== 1)
				{
					int count = 1;
					for(int l = 1 ; l < maxSame;l++)
					{
						//right
						if(k+l < noOfChars)
						{
							if(game[j][k+l] == 1)
								count++;
							else
								break;
						}
						else
							break;
					}
					if(count == maxSame)
						Rwin = 1;
					else
					{
						count = 1;
						for(int l = 1 ; l < maxSame;l++)
						{
							//right + down
							if(k+l < noOfChars && j+l < noOfChars )
							{
								if(game[j+l][k+l] == 1)
									count++;
								else
									break;
							}
							else
								break;
						}
						if(count == maxSame)
							Rwin = 1;
						else
						{
							count = 1;
							for(int l = 1 ; l < maxSame;l++)
							{
								// down
								if(j+l < noOfChars )
								{
									if(game[j+l][k] == 1)
										count++;
									else
										break;
								}
								else
									break;
							}
							if(count == maxSame)
								Rwin = 1;
							else
							{
								count = 1;
								for(int l = 1 ; l < maxSame;l++)
								{
									//left + down
									if(k-l > -1  && j+l < noOfChars )
									{
										if(game[j+l][k-l] == 1)
											count++;
										else
											break;
									}
									else
										break;
								}
								if(count == maxSame)
									Rwin = 1;
							}
						}
					}
				}
				else if(game[j][k]== -1)
				{
					int count = 1;
					for(int l = 1 ; l < maxSame;l++)
					{
						//right
						if(k+l < noOfChars)
						{
							if(game[j][k+l] == -1)
								count++;
							else
								break;
						}
						else
							break;
					}
					if(count == maxSame)
						Bwin = 1;
					else
					{
						count = 1;
						for(int l = 1 ; l < maxSame;l++)
						{
							//right + down
							if(k+l < noOfChars && j+l < noOfChars )
							{
								if(game[j+l][k+l] == -1)
									count++;
								else
									break;
							}
							else
								break;
						}
						if(count == maxSame)
							Bwin = 1;
						else
						{
							count = 1;
							for(int l = 1 ; l < maxSame;l++)
							{
								// down
								if(j+l < noOfChars )
								{
									if(game[j+l][k] == -1)
										count++;
									else
										break;
								}
								else
									break;
							}
							if(count == maxSame)
								Bwin = 1;
							else
							{
								count = 1;
								for(int l = 1 ; l < maxSame;l++)
								{
									//left + down
									if(k-l > -1  && j+l < noOfChars )
									{
										if(game[j+l][k-l] == -1)
											count++;
										else
											break;
									}
									else
										break;
								}
								if(count == maxSame)
									Bwin = 1;

							}
						}
					}
				}
			}
		}
		cout <<"Case #" << i+1 <<": ";
		if(Rwin == 1 && Bwin == 1)
			cout << "Both";
		else if(Rwin == 1)
			cout << "Red";
		else if(Bwin == 1)
			cout << "Blue";
		else
			cout << "Neither";
		cout << endl;
	}

}
