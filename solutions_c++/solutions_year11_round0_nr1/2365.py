#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

struct Point
{
	int x,y;
	Point(){x=0,y=0;}
	Point(int _x, int _y)
	{
		x = _x;
		y = _y;
	}
};

long test,tcounter;

int main()
{
    SetInputFile();
    
    queue<Point>blue;
    queue<Point>orange;
    int n,x;
    char c;
	int step = 0, flag = 0;
	int currentRank = 1;

    cin >> test;
    tcounter = 0;
	
    while(test--)
    {
      blue.empty();
      orange.empty();
      
      cin >> n;
      step = 1;
      while(n--)
      {
         cin >> c >> x;
         if(c=='B') blue.push(Point(x,step++));
         else orange.push(Point(x,step++));
      }
      
      int bPosition = 1;
      int oPosition = 1;
	  currentRank = 1;
	  step = 0; 
      Point b,o;
      while(blue.size() != 0 || orange.size() !=0)
      {
         step ++;
         flag = 0;
         
         if(blue.size()!=0){                            
                  b = blue.front();
                  if(bPosition == b.x)
                   {
                        if(currentRank == b.y)
						{							
							currentRank++;
							blue.pop();
                            flag = 1;
						}
                   }
                   else if(bPosition < b.x)
					   bPosition++;
				   else if(bPosition > b.x)
					   bPosition--;

         }
         
          if(orange.size()!=0){                            
                  o = orange.front();
                  if(oPosition == o.x)
                   {                        
                     if(flag==0 && currentRank == o.y)
					 {
					  	 currentRank++;
						 orange.pop();
					 }
                   }
                   else if(oPosition < o.x)
					   oPosition++;
				   else if(oPosition > o.x)
					   oPosition--;
         }
         
         
      }
      
      cout << "Case #"<< ++tcounter << ": " << step << endl;
    }
    
    return 0;
}
