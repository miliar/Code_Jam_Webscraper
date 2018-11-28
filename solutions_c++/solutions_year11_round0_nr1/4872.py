#include <iostream>
#include <iomanip>
#include <fstream>
#include <queue>

using namespace std;

int main()
   {

   ifstream inFile;
   ofstream outFile;

   inFile.open("./A-large.in");
   outFile.open("./A-large.out");
   
   int T,
       N,
       button,
	   Opos = 1,
	   Bpos = 1,
	   time = 0;
   
   char bot;

   bool Done = false;
   
   inFile >> T;

   for (int i = 1; i <= T; i++)
      {
	  inFile >> N;
	  
	  queue<char> color;
      queue<int> OB;
      queue<int> BB;
	  
      for (int j = 1; j <= N; j++)
	     {
         Done = false;
         Opos = 1;
         Bpos = 1;
		 inFile >> bot;
		 inFile >> button;
		 
		 color.push(bot);
		 
	     if (bot == 'O')
		    OB.push(button);
	     else
		    BB.push(button);         
		 }
      color.push('Q');
      OB.push(0);
      BB.push(0);

      while (Done == false)
	     {
         bot = color.front();
		 
		 if (bot == 'O' && bot != 'Q')
		    {
			if (Opos < OB.front())
			   Opos++;
			else if (Opos > OB.front())
			   Opos--;
			else
               {
               color.pop();
			   OB.pop();
               }
            }
		 else if (bot == 'B' && bot != 'Q')
		    {
			if (Bpos < BB.front())
			   Bpos++;
			else if (Bpos > BB.front())
			   Bpos--;
			else
			   {
               color.pop();
			   BB.pop();
               }
            }
		    
			if (bot == 'B' && OB.front() != 0)
		       {
			   if (Opos < OB.front())
		   	      Opos++;
		   	   else if (Opos > OB.front())
		   	      Opos--;
			   }
		    else if (bot == 'O' && BB.front() != 0)
		       {
			   if (Bpos < BB.front())
			      Bpos++;
			   else if (Bpos > BB.front())
			      Bpos--;
               }
		 time++;
		 if (color.front() == 'Q')
		    Done = true;
		 }

	  cout << "Case #" << i << ": " << time << endl;
      outFile << "Case #" << i << ": " << time << endl;
	  time = 0;
      }

   inFile.close();
   outFile.close();
   system("pause");
   return 0;
   }

