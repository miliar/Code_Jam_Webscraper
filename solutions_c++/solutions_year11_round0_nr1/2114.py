#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

typedef struct PUSHBUTTON
{
  int color;
  int button;
} tPushButton;

int calculateMinimumTime(tPushButton* pPB, int numberOfButton);

int main(int argc, char*argv[])
{
  int i,j;
  int numberOfLines = 0;
  ifstream inFile;
  ofstream outFile;
  
  if (argc!=3)
    {
      cout<<"usage: botTrust <input File> <output File>"<<endl;
      exit(0);
    }
  inFile.open(argv[1], ios::in);
  if (!inFile)
    {
      cerr<<"Cant's open input file "<<argv[1]<<endl;
      exit(1);
    }

  outFile.open(argv[2], ios::out);
  if (!outFile)
    {
      cerr<<"Cant's open input file "<<argv[2]<<endl;
      exit(1);
    }

  if (inFile.eof())
    {
      cerr<<"Input file formation error!"<<endl;
      exit(1);
    }
  
  inFile>>numberOfLines;
  cout<<numberOfLines<<endl;
  for(i=0;i<numberOfLines;i++)
    {
      int ii;
      int numberOfButton;
      int timeConsumed = 0;
      inFile>>numberOfButton;
      cout<<numberOfButton<<" ";
      tPushButton* pPB = (tPushButton*)malloc(sizeof(tPushButton)*numberOfButton);
      for(ii=0;ii<numberOfButton;ii++)
	{
	  char color;
	  inFile>>color;
	  if (color == 'O')
	    pPB[ii].color = 0;
	  else if (color == 'B')
	    pPB[ii].color = 1;
	  else
	    {
	      cout<<"Should not have color other than O and B!"<<endl;
	      exit(0);
	    }
	  cout<<pPB[ii].color<<" ";
	  inFile>>pPB[ii].button;
	  cout<<pPB[ii].button<<" ";
	  if (inFile.eof())
	    {
	      cerr<<"Input file formation error!"<<endl;
	      exit(1);
	    }
	}
      cout<<endl;

      timeConsumed = calculateMinimumTime(pPB, numberOfButton);
      cout<<timeConsumed<<endl;
      outFile<<"Case #"<<(i+1)<<": "<<timeConsumed<<endl;
    }

  return 0;
}

int calculateMinimumTime(tPushButton* pPB, int numberOfButton)
{
  int i;
  int position[2] = {1,1};
  int minimumTime = pPB[0].button;
  int lastTimeConsumed = minimumTime;
  int prevBot=pPB[0].color;
  if ((prevBot!=0)&&(prevBot!=1))
    {
      cout<<"Should not have color other than O and B!"<<endl;
      exit(0);
    }
  position[prevBot] = pPB[0].button;

  for(i=1;i<numberOfButton;i++)
    {
      int currentPosition = pPB[i].button;
      int prevPosition = position[pPB[i].color];
      if(pPB[i].color==prevBot)
	{
	  minimumTime += (abs(currentPosition-prevPosition)+1);
	  lastTimeConsumed += (abs(currentPosition-prevPosition)+1);
	}
      else
	{
	  if (lastTimeConsumed>=abs(currentPosition-prevPosition))
	    {
	      lastTimeConsumed = 1;
	    }
	  else
	    {
	      lastTimeConsumed = abs(currentPosition-prevPosition)-lastTimeConsumed+1;
	    }
	  minimumTime += lastTimeConsumed;
	}
      position[pPB[i].color] = currentPosition;
      prevBot = pPB[i].color;
    }

  return minimumTime;
}
