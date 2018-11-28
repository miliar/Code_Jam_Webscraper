#include<iostream>
#include<fstream>

using namespace std;

int totalRevenue(int numRides, int numPeople, int numGroup, int peoplePerGroup[])
{
    int sum=0,numGroupPerRide=0,temp=0,groupCount=0;
    for(int i=0;i<numRides; i++)
    {
			temp=0;
			int j = numGroupPerRide;
			groupCount=0;
			while(j < numGroup)
			{
                
				if((numPeople-temp) >= peoplePerGroup[j] && groupCount < numGroup)
                {
			         temp += peoplePerGroup[j];                        
                     numGroupPerRide++;
                }
                else
                {
                     break;    
                }
    
                if(j==(numGroup-1))
                {
                     j=0;              
                }
				else
				{
					j++;
                }
                groupCount++;  
			}
            numGroupPerRide %= numGroup;        
			sum+=temp;
    }    
    return sum;
}

int main()
{
    int numTestCases=0;
    int numRides=0;
    int numPeople=0;
    int numGroup=0;
    ifstream inputFile("C-small-attempt0.in");
    ofstream outputFile("C-small-attempt0.out");
	inputFile >> numTestCases;
 	for(int i=1;i<=numTestCases;i++)
 	{
            inputFile >> numRides;
            inputFile >> numPeople;
            inputFile >> numGroup;
            if(numGroup != 0)
            {
             int *groups = new int[numGroup];
            
             for(int j=0;j<numGroup;j++)
             {
                    inputFile >> groups[j];
             }
             outputFile << "Case #" << i <<":  " << totalRevenue(numRides,numPeople,numGroup,groups) << endl;
             delete(groups);
            }
            else
            {
              outputFile << "Case #" << i <<":  " << 0 << endl;  
            }
            
     }

}
