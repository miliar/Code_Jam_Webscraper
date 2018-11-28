// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
//#include <string>
//#include <vector>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>

using namespace std;

//other functions may go here!

//main function!

char calculateBasin(int posH, int posW, int& H, int& W, int *map, char *mapBasin, char& actualLetter)
{
  bool sink=true;
  int newH, newW;
  int lower=map[posH*W+posW]-1;
  
  if((posH+1<H) && map[(posH+1)*W+posW]<=lower)
  {
	  sink = false;
	  newH = posH+1;
	  newW = posW;
	  lower = map[newH*W+newW];
  }
  if((posW+1<W) && map[(posH)*W+posW+1]<=lower)
  {
	  sink = false;
	  newH = posH;
	  newW = posW+1;
	  lower = map[newH*W+newW];
  }
  if((posW>0) && map[(posH)*W+posW-1]<=lower)
  {
	  sink = false;
	  newH = posH;
	  newW = posW-1;
	  lower = map[newH*W+newW];
  }
  if((posH>0) && map[(posH-1)*W+posW]<=lower)
  {
	  sink = false;
	  newH = posH-1;
	  newW = posW;
	  lower = map[newH*W+newW];
  }

  if(sink)
	  mapBasin[posH*W+posW] = actualLetter++;
  else
  {
	  if(mapBasin[newH*W+newW] != '0')
		mapBasin[posH*W+posW] = mapBasin[newH*W+newW];
	  else
	    mapBasin[posH*W+posW] = calculateBasin(newH, newW, H, W, map, mapBasin, actualLetter);
  }
  return mapBasin[posH*W+posW];
}

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("b-largein.txt");
    ofstream outputFile("b-blargeout.txt", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
    {
      //error openning input/output file!
      return 0;
    }

	int numIterations, H, W;
	int *map;
	char *mapBasin;
	inputFile >> numIterations;
    char initialChar;

    for (int numCase = 1; numCase <= numIterations; numCase++)
	{
		//parsing code goes here
        inputFile >> H; inputFile >> W;
        map = new int[H*W];
		mapBasin = new char[H*W];
		for(int i=0; i<H*W; i++)
			mapBasin[i]='0';

		for(int h=0; h<H; h++)
		{
          for(int w=0; w<W; w++)
		  inputFile >> map[h*W+w];
		}

		//problem code goes here
		initialChar = 'a';
		for(int h=0; h<H; h++)
		{
          for(int w=0; w<W; w++)
		  {
            if(mapBasin[h*W+w] == '0')
			  calculateBasin(h, w, H, W, map, mapBasin, initialChar);
		  }
		}
		outputFile << "Case #" << numCase << ": " << endl;
        for(int h=0; h<H; h++)
		{
		  for(int w=0; w<W; w++)
			outputFile << mapBasin[h*W+w] << ' ';
		  outputFile << endl;
		}
		delete map;
		delete mapBasin;
	}
	return 0;
}

