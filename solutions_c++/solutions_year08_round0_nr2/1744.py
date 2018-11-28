#include<string>
#include<sstream>
#include <iostream>
#include <fstream>
using namespace std;

struct tripPair {
  int start;
  int end;
};

int main(int argc, char* argv[])
{
  int numCases, index, earliest;
  int numABRuns,numBARuns,turnTime, numABTrains, numBATrains;
  string time;
  tripPair inputA[100], inputB[100];
  tripPair leavingA[100];
  tripPair leavingB[100];
  int availatA[100];
  int availatB[100];
  int numatA, numatB, curA, curB, available;

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
    numABTrains=0;
    numBATrains=0;

    myFile>>turnTime;
    myFile>>numABRuns;
    myFile>>numBARuns;
    for(int j=0;j<numABRuns;j++)
    {
      //get string
      myFile>>time; 
      //remove :
      time.erase(2, 1);
      //turn into number
      stringstream(time)>>inputA[j].start;

      //get string
      myFile>>time;
      //remove :
      time.erase(2, 1);
      //turn into number
      stringstream(time)>>inputA[j].end;
    }
    for(int j=0;j<numBARuns;j++)
    {
      //get string
      myFile>>time;
      //remove :
      time.erase(2, 1);
      //turn into number
      stringstream(time)>>inputB[j].start;

      //get string
      myFile>>time;
      //remove :
      time.erase(2, 1);
      //turn into number
      stringstream(time)>>inputB[j].end;
    }
    
    //sort the A leave times
    //stupid sort
    for(int j=0;j<numABRuns;j++)
    {
      //find smallest remaining start time
      earliest=2500;
      index=-1;
      for(int k=0;k<numABRuns;k++)
      {
	if(inputA[k].start<earliest)
	{
	  earliest=inputA[k].start;
	  index=k;
	}
      }
      //move to next spot in real array
      leavingA[j].start=inputA[index].start;
      leavingA[j].end=inputA[index].end;
      inputA[index].start=2600;
    }
    cout<<"leaving A times"<<endl;
    for(int j=0;j<numABRuns;j++)
      cout<<leavingA[j].start<<" "<<leavingA[j].end<<endl;

    //sort the B leave time
    //stupid sort
    for(int j=0;j<numBARuns;j++)
      {
	//find smallest remaining start time
	earliest=2500;
	index=-1;
	for(int k=0;k<numBARuns;k++)
	  {
	    if(inputB[k].start<earliest)
	      {
		earliest=inputB[k].start;
		index=k;
	      }
	  }
	//move to next spot in real array
	leavingB[j].start=inputB[index].start;
	leavingB[j].end=inputB[index].end;
	inputB[index].start=2600;
      }
    cout<<"leaving B times"<<endl;
    for(int j=0;j<numBARuns;j++)
      cout<<leavingB[j].start<<" "<<leavingB[j].end<<endl;


    if(numABRuns>0 && numBARuns==0)
    {
      //only A trains
      outFile<<"Case #"<<i+1<<": "<<numABRuns<<" "<<0<<endl;
    }
    else if(numBARuns>0 && numABRuns==0)
    {
      //only B trains
      outFile<<"Case #"<<i+1<<": "<<0<<" "<<numBARuns<<endl;
    }
    else if(numBARuns==0 && numABRuns==0)
    {
      //no trains
      outFile<<"Case #"<<i+1<<": "<<0<<" "<<0<<endl;
    }
    else
    {
      curA=0;
      curB=0;
      numatA=0;
      numatB=0;
      //for all the trains yet to leave, do this:
      while(curA<numABRuns || curB<numBARuns)
      {
	//find next train to add
	if((curB==numBARuns) || ((curA<numABRuns) && (leavingA[curA].start<leavingB[curB].start)))
	{
	  cout<<"processing train from A: "<<leavingA[curA].start<<" "<<leavingA[curA].end<<endl;
	  //train is leaving from A
	  //see if earlier trains are available
	  available=-1;
	  for(int k=0;k<numatA;k++)
	    if(availatA[k]<=leavingA[curA].start)
	      available=k;
	  if(available>=0)
	  {
	    //use the available train
	    availatB[numatB]=leavingA[curA].end+turnTime;
	    numatB++;
	    curA++;
	    //reduce available trains
	    while(available<(numatA-1))
	    {
	      availatA[available]=availatA[available+1];
	      available++;
	    }
	    numatA--;
	  }
	  else
	  {
	    //add an A train
	    numABTrains++;
	    availatB[numatB]=leavingA[curA].end+turnTime;
	    numatB++;
	    curA++;
	  }
	}
	else
	{
	  cout<<"processing train from B: "<<leavingB[curB].start<<" "<<leavingB[curB].end<<endl;
          
	  //train is leaving from B
          //see if earlier trains are available
          available=-1;
          for(int k=0;k<numatB;k++)
            if(availatB[k]<=leavingB[curB].start)
              available=k;
          if(available>=0)
	    {
	      //use the available train
	      availatA[numatA]=leavingB[curB].end+turnTime;
	      numatA++;
	      curB++;
	      //reduce available trains
	      while(available<(numatB-1))
		{
		  availatB[available]=availatB[available+1];
		  available++;
		}
	      numatB--;
	    }
          else
	    {
	      //add a B train
	      numBATrains++;
	      availatA[numatA]=leavingB[curB].end+turnTime;
	      numatA++;
	      curB++;
	    }

	}
      }


      outFile<<"Case #"<<i+1<<": "<<numABTrains<<" "<<numBATrains<<endl;
    }
    
  }
  
  return 0;

}
