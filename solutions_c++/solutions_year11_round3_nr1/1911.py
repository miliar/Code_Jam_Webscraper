// HotDog.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	int T, R,C;
	char tiles[51][51];
	bool quit;


	ifstream fin;
	fin.open("tilesL.in");

	ofstream fout;
	fout.open("tilesL.txt");


	fin >> T;
	
	for(int z=0;z<T;z++)
	{
		int num=0;
		quit=false;
		fin >> R >> C;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				fin >> tiles[i][j];
				if(tiles[i][j]=='#') num++;
			}
		}

		fout << "Case #"<<z+1<<":"<<endl;

		if(num%4!=0) fout <<"Impossible"<<endl;
		else
		{
			for(int i=0;(i<R)&&(!quit);i++)
			{
				for(int j=0;(j<C)&&(!quit);j++)
				{
					
					if(tiles[i][j]=='#') 
					{
						if((tiles[i+1][j]!='#') && (tiles[i][j+1]!='#') && (tiles[i+1][j+1]!='#')) quit=true;
						else
						{
							tiles[i][j]='/';
							tiles[i][j+1]='\\';
							tiles[i+1][j+1]='/';
							tiles[i+1][j]='\\';
						}

					}
				}
			}
			if(quit) fout <<"Impossible"<<endl;
			else
			{
				for(int i=0;(i<R)&&(!quit);i++)
				{
					for(int j=0;(j<C)&&(!quit);j++)
					{
					
						fout << tiles[i][j];
					}
					fout << endl;
				}
			}
		}

	}




	fin.close();
	fout.close();
	return 0;
}

