#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <map>
#include <sstream>
#include <vector>

using namespace std;



//0 - false, 1 - doesnt require surprise, 2 - requires surprise

int meetsCase(int sum, int target)
{
    float sumThree = (float)sum/3.f;
    
    int a = (int)sumThree;
    int b = (int)sumThree;
    int c = sum - a - b;
    
    int diff = c - b;
    
    if(diff==0)
    {
        if(c>=target)
            return 1;
        if(a==0)
            return 0;        
        a--;
        c++;
        if(c>=target)
            return 2;
        return 0;
    }
    if(diff==1)
    {
        if(c >= target)
            return 1;
        return 0; 
    }
    if(diff==2)
    {
        c--;
        b++;
        if(c>=target)
            return 1;
        c++;
        b--;
        if(c>=target)
            return 2;
        return 0;
    }
    printf("ERROR: THIS SHOULD NEVER BE PRINTTED");
    return 0;
}


int main()
{
    string line;
    getline(cin, line); 
    stringstream ss("");
    ss<<line;
    int numCases;
    ss>>numCases;

    int numGooglers;
    int numSurprises;
    int target;
    int numPoints;

    int temp;
    for(int i = 0; i < numCases; i++)
    {
        stringstream ss("");        
        getline(cin, line);
        ss<<line;
        int count = 0;
        int surprisesUsed = 0;

        ss>>numGooglers;
        ss>>numSurprises;
        ss>>target;
        for(int j = 0; j < numGooglers; j++)
        {
            ss>>temp;
            numGooglers<<temp;

            switch(meetsCase(temp, target))
            {
                case 1:
                    count++;
                    break;
                case 2:
                    surprisesUsed++;
                    break;
                default:
                    break;
            }
        }
        printf("Case #%d: %d\n", i+1, count + min(surprisesUsed, numSurprises));
    }
}

//The idea is:
//For each googler, we need to classify them as meets case, 
//  meets case (surprise), or doesnt meet case ever.


