#include <iostream>
#include <vector>
#include <math.h>

int found = 0;
int foundS = 0;


using namespace std;

int with = 0;
int non = 0;
int oblige = 0;
int et = 0;

int tryT(int score, int p)
{
  int nb = 0;
  int act[3] = {0,0,0};
  int max;
  bool used = false;
  bool n = false;

  for(int i1 = 0; i1 <= 10; i1++)
    {
      act[0] = i1;

      for(int i2 = 0; i2 <= 10; i2++)
	{
	  act[1] = i2;
	  for(int i3 = 0; i3 <= 10; i3++)
	    {
	      act[2] = i3;

	      if(i1 + i2 + i3 == score)
		{
		  if(fabs(i1 - i2) < 3 && fabs(i1 - i3) < 3 && fabs(i2 - i3) < 3)
		    {

		      if(i1 <= i2 && i2 <= i3)
			{
			  if(i1 >= p || i2 >= p || i3 >= p)
			    {
			      //cout << i1 << " " << i2 << " " << i3 << endl;
			      if(fabs(i1 - i2) == 2 || fabs(i1 - i3) == 2 || fabs(i2 - i3) == 2)
				{
				  with++;
				  //cout << "used" << endl;
				  used = true;
				}
			      else
				{
				  non++;
				  n = true;
				}
			    }
			}
		    }

		}
	    }
	}
    }

  if(!n && used)
    oblige++;

  if(n && used)
    et++;
}

int test(int score, int p, int surpr)
{
  int s = 0;
  bool w = false;
  bool n = false;

  tryT(score, p);
 
 if(with == oblige)
   found = non + oblige;
 else
   found = non + surpr;
    
 //cout << "FOUND: " << with << " " << non << " " << endl;
  //cout << oblige << " " << et << endl;
}

int main()
{
  
  int n;
  int score;
  int part;
  int surpr;
  int p;

  std::cin >> n;
  std::cin.ignore();

  for(int _i = 0; _i < n; ++_i)
    {
      std::cin >> part;
      std::cin >> surpr;
      std::cin >> p;
      for(int _f = 0; _f < part; ++_f)
	{
	  std::cin >> score;
	  test(score, p, surpr);
	}
      //cout << oblige << " " << et << " " << non << " " << with << endl;


      if(oblige > surpr)
	found = surpr + non;
      else
	found = non + oblige;

      cout << "Case #" << _i + 1<< ": " << found << endl;
      non = 0;
      with = 0;
      oblige = 0;
      et = 0;
    }
  return 0;
}
