//Source Code
//Code compiled and run in Microsoft Visual C++ 6.0
//Standard Libraries Used

#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<math.h>

using namespace std;

int main()
{
	   ifstream finput;
	   ofstream foutput("F:/ASmallOut");		

	   finput.open("F:/ASmall.txt"); 
	       	   
	   int numTests;
	   
	   char a[100];								
	   char ch;
	   
	   finput>>numTests;

	   finput.get(ch);
	   while(isspace(ch))finput.get(ch);
	   finput.putback(ch);
	   
	   //Trace
	   cout<<"num = "<<numTests<<endl;    
	
	   if(!finput.is_open())
	   {
		   cout<<"ERROR in opening input file";
		   return 1;
	   }

	
	  foutput<<"Output"<<endl;

	  for(int test =1;test <= numTests; test++)
	   {
		int numSE;
		map<string,int> sNumMap;
		map<string,int>::iterator myIter;
		
		finput>>numSE;   
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);

		cout<<endl<<"Input "<<test<<endl;
		cout<<"Engine ="<<numSE<<endl;

		for(int count = 0; count < numSE;count++)
		{
			string engine;

			finput.get(a,99,'\n');	
			finput.get(ch);
			while(isspace(ch)) finput.get(ch);
			finput.putback(ch);

			engine.insert(0,a);
			sNumMap[engine] = count;
			
			cout<<"engine="<<engine<<endl;

		}

		int numQ;
		
		finput>>numQ;
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);
		

		cout<<"Queries="<<numQ<<endl;
		map<string,int>tempMap;
		tempMap = sNumMap;
		
		int Switches = 0;
		for(count = 0; count<numQ; count++)
		{
			string engine;

			finput.get(a,99,'\n');	
			finput.get(ch);
			while(isspace(ch)) finput.get(ch);
			finput.putback(ch);			
			
			engine.insert(0,a);

			cout<<"query="<<engine<<endl;

			myIter = tempMap.find (engine);
			if(myIter == tempMap.end());
			else
			  tempMap.erase(myIter);

			if(tempMap.empty())
			{
				tempMap = sNumMap;
				tempMap.erase(tempMap.find(engine));
				Switches++;
			}

		}
		cout<<"Case #"<<test<<":"<<Switches<<endl;
		sNumMap.erase(sNumMap.begin(), sNumMap.end());
    	tempMap.erase(tempMap.begin(), tempMap.end());
	  }

finput.close();
foutput.close();
return 0;
}

