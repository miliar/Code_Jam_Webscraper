#include <vector>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

#define for0(i, l) for(int i = 0; i < (l); ++i)

int main ()
{
     int t;
     cin >> t;
     for0(p, t)
     {
	  int o = 1;
	  int b = 1;
	  vector < int > btodo;
	  vector < int > otodo;
	  vector < int > order;
	  int total = 0;
	  cin >> ws;
	  string line;
	  getline(cin, line);
	  istringstream iss (line);
	  int lol;
	  iss >> lol;
	  //cout << "yawn" << endl;
	  while (!(iss >> ws).eof())
	  {
	       int moveto;
	       string bot;
	       iss >> bot;
	       iss >> moveto;
	       
	       if (bot == "O")
	       {
		    order.push_back (1);
		    otodo.push_back (moveto);
	       }
	       else
	       {
		    order.push_back (0);
		    btodo.push_back (moveto);
	       }
	  }
	  //cout << "sigh" << endl;	
	  
	  int i = 0;
	  int count = 0;
	  int bt = 0;
	  int ot = 0;
	  while (i < (int)order.size())
	  {     
	       bool pressed = false;
	
	       if (!btodo.empty())
	       {
		    if (b < btodo[bt])
		    {
			 ++b;
		    }
		    else if (b > btodo[bt])
		    {
			 --b;
		    }
		    else if (!order[i])
		    {
			 bt++;
			 i++;
			 pressed = true;
		    }
	       }
	       
	       if (!otodo.empty())
	       {
		    if (o < otodo[ot])
		    {
			 ++o;
		    }
		    else if (o > otodo[ot])
		    {
			 --o;
		    }
		    else if (order[i] && !pressed)
		    {
			 ot++;
			 i++;
		    }
	       }      
	       count++;
	       
	  }
	  
	  cout << "Case #" << (p + 1) << ": " << count << endl;
     }
}