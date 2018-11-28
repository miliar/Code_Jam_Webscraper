#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[])
{
  int numCases, numEngines, numQueries, switches=0;
  string Enames[100];
  string Qnames[1000];
  string junk;
  int inUse[100];
  int numInUse;

  ifstream myFile ("small.txt");
  ofstream outFile("output.txt");

  if(myFile.is_open())
  {
    //first read
    myFile>>numCases;
    cout<<"num cases: "<<numCases<<endl;
  }
  else
  {
    cout<<"file not opened"<<endl;
    return 1;
  }

  for(int i=0;i<numCases;i++)
  {

    //reset for next case
    switches=0;
    for(int j=0;j<100;j++)
      {
        Enames[j].clear();
	inUse[j]=0;
      }
    for(int j=0;j<1000;j++)
      {
        Qnames[j].clear();
      }


    myFile>>numEngines;
    getline(myFile, junk);
    for(int j=0;j<numEngines;j++)
      {
	getline(myFile, Enames[j]);
	cout<<"got engine: "<<Enames[j]<<endl;
      }
    myFile>>numQueries;
    getline(myFile, junk);
    for(int j=0;j<numQueries;j++)
      {
	getline(myFile, Qnames[j]);
	cout<<"got query: "<<Qnames[j]<<endl;
      }

    numInUse=0;
    for(int j=0;j<numQueries;j++)
    {
      cout<<"checking query #"<<j+1<<": "<<Qnames[j]<<endl;
      //find out which engine current query would match
      for(int k=0;k<numEngines;k++)
      {
	if(0==Qnames[j].compare(Enames[k]))
	  {
	    //found the engine it matches, mark as in use
	    //see if already used
	    if(!inUse[k])
	    {
	      inUse[k]=1;
	      numInUse++;
	      cout<<"marking: "<<Enames[k]<<endl;
	    }
	    //if that's the last one, switch and reset
	    if(numInUse==numEngines)
	    {
	      cout<<"used them all"<<endl;
	      switches++;
	      numInUse=1;
	      for(int l=0;l<numEngines;l++)
		inUse[l]=0;
	      inUse[k]=1;
	    }
	  }
      }


    }


    outFile<<"Case #"<<i+1<<": "<<switches<<endl;
       
  }
  
  return 0;

}
