#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;
using std::sort;
using std::ifstream;
using std::ofstream;
using std::stringstream;
using std::string;
using std::vector;

// returns the time string as an integer of minutes
int TimeToMins(string time)
{
    
    stringstream sh(stringstream::in | stringstream::out);
    stringstream sm(stringstream::in | stringstream::out);
    
    // push in the hours
    sh << time.substr(0, 2);
    
    int mins;
    sh >> mins;
    
    // 60 mins in an hour
    mins *= 60;
    
    // push in the minutes
    sm << time.substr(3, 2);
    
    int minutes;
    
    sm >> minutes;
    
    
    mins += minutes;
    
    return mins;
}


int main(int argc, char* argv[])
{
		// No input file given
		if (argc != 2)
		   exit(0);
	    
		// file name is in argv[1]
		string file = "";
		file += argv[1];
	    
	    
		// open input file
		ifstream inFile(file.c_str());
	    
		// change .in to .out
		file = file.substr(0,file.length() - 2);
		file += "out";
	    
		// open a file for output
		ofstream outFile(file.c_str());
	    
	    
		// file must be opened
		if (!inFile)
		   exit(0);

         // get the number of cases
         int cases;
         inFile >> cases;
         
         int index;
         for (index = 0; index < cases; index++)
         {
             int turnAround, aTrips, bTrips;
             inFile >> turnAround >> aTrips >> bTrips;
             
             vector<int> aDepartures;
             vector<int> bArrivals;
             
             vector<int> bDepartures;
             vector<int> aArrivals;
             
             //populate the vectors with times and sort them
             int aIndex;
             for (aIndex = 0; aIndex < aTrips; aIndex++)
             {
                 string time;
                 inFile >> time;
                 aDepartures.push_back(TimeToMins(time));
                 inFile >> time;
                 bArrivals.push_back(TimeToMins(time) + turnAround);
             }
             int bIndex;
             for (bIndex = 0; bIndex < bTrips; bIndex++)
             {
                 string time;
                 inFile >> time;
                 bDepartures.push_back(TimeToMins(time));
                 inFile >> time;
                 aArrivals.push_back(TimeToMins(time) + turnAround);
             }
             sort(aDepartures.begin(), aDepartures.end());
             sort(bDepartures.begin(), bDepartures.end());
             sort(aArrivals.begin(), aArrivals.end());
             sort(bArrivals.begin(), bArrivals.end());
             
             
             // count of the trains
             int aTrains = 0;
             int bTrains = 0;
             
             // count the trains needed to meet the departures from station a
             int aDepartIndex = 0;
             int aArriveIndex = 0;
             for (aDepartIndex = 0; aDepartIndex < aDepartures.size(); aDepartIndex++)
             {
                   if (aArriveIndex == aArrivals.size())
                   {
                                    aTrains++;
                   }          
                   else if (aDepartures[aDepartIndex] < aArrivals[aArriveIndex])
                   {
                        aTrains++;
                   }
                   else
                   {
                       aArriveIndex++;
                   }
             }
             
             // count the trains needed to meet the departures from station b
             int bDepartIndex = 0;
             int bArriveIndex = 0;
             for (bDepartIndex = 0; bDepartIndex < bDepartures.size(); bDepartIndex++)
             {
                 if (bArriveIndex == bArrivals.size())
                 {
                                  bTrains++;
                 }
                 else if (bDepartures[bDepartIndex] < bArrivals[bArriveIndex])
                 {
                      bTrains++;
                 }
                 else
                 {
                     bArriveIndex++;
                 }
             }
             
             
             outFile << "Case #" << (index + 1) << ": " << aTrains << " " << bTrains << endl;
             
         }
         
         
         // cleanup
         inFile.close();
         outFile.close();
         
         return 0;
}
