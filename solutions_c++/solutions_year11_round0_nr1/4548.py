
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include "string.h"

using namespace std;

int main()
{
  char seq[512];
  char filename[10];
  int time = 0, num, Bpos = 1, Opos = 1, BT = 0, OT = 0, cnt = 0, elapsed;
  char last;
  ifstream inFile;
  cout << "enter filename: ";
  cin >> filename;
  inFile.open(filename);
  while(!inFile.eof())
  {  
      inFile.getline(seq, 512);
      for(int i = 0 ; i < 512 ; i++)
      {
	  if(seq[i] == '\0') break; 
	  if(seq[i] == ' ') continue;
	  if(last == 'B')
	  {
	    num = atoi(&seq[i]);
	    elapsed = abs(num - Bpos) + 1;
	    if((elapsed + BT) <= time) time++;
	    else time = (elapsed + BT);
	    Bpos = num;
	    BT = time;
	  } 
	  if(last == 'O')	
	  {
	    num = atoi(&seq[i]);
	    elapsed = abs(num - Opos) + 1;
	    if((elapsed + OT) <= time) time++;
	    else time = (elapsed + OT);
	    Opos = num;
	    OT = time;
	  }  
	  last = seq[i];
      }
      if(cnt != 0)
	cout << "Case #" << cnt << ": " << time << endl;
      Bpos = 1;
      Opos = 1;
      OT = 0;
      BT = 0;
      time = 0;
      cnt++;
  }
  inFile.close();
  return 0;
}