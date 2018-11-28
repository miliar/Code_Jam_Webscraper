/* 
 * File:   main.cpp
 * Author: mfatihuslu
 *
 * Created on April 14, 2012, 7:33 PM
 */

#include <iostream>
#include <fstream>
using namespace std;
int reArrange(int,int,int);

int main(int argc, char** argv) {

    fstream input, output;
    int numberOfTry;
    input.open("input",ios::in);
    output.open("output",ios::out);
    
    input>>numberOfTry;
    
    for(int x = 0 ; x < numberOfTry ; x++){
        
        output<<"Case #"<<x+1<<": ";
        
        int firstNumber,lastNumber, numberOfData = 0, dummyVariable = 1, resultNumber = 0;
        input>>firstNumber>>lastNumber;
        
        for(int y = 0 ; firstNumber >= dummyVariable ; dummyVariable = dummyVariable * 10 )
            numberOfData++;
       
        for(int z = firstNumber ; z < lastNumber ; z++)
        {
            int reArranged[numberOfData];
            for(int y = 1 ; y < numberOfData ; y++)
            {
                reArranged[y] = reArrange(z,numberOfData,y);
                int milestoneVariable = 0;
                
                if(reArranged[y] > z and reArranged[y] >= firstNumber and reArranged[y] <= lastNumber)
                {
                    for(int t = 1 ; t < y ; t++)
                        if(reArranged[t] == reArranged[y])
                            milestoneVariable = 1;
                    
                    if(milestoneVariable == 0)
                        resultNumber++;
                        
                }                    
            }
        }
        
        output<<resultNumber;
        if(x!=numberOfTry-1)
            output<<endl;
    }
    return 0;
}

int reArrange(int data, int numberOfData, int numberOfOrder){
    
    int elementsOfNumber[numberOfData];
    int dummyVariable, functionResult = 0;
    dummyVariable = data;
    
    for(int x = 0 ; x < numberOfData ; x++)
    {
        elementsOfNumber[numberOfData - x - 1] = data % 10;
        data = data/10;
    }
    
    for(int x=0;x<numberOfOrder;x++)
    {
        dummyVariable = elementsOfNumber[numberOfData - 1];
        
        for(int j = numberOfData - 1 ; j >= 0 ; j--)
            elementsOfNumber[j+1] = elementsOfNumber[j];
        
        elementsOfNumber[0] = dummyVariable;
    }
    
    functionResult = 0;
    dummyVariable = 1;
    
    for(int x=0;x<numberOfData;x++)
    {  
        functionResult = functionResult + elementsOfNumber[numberOfData-1-x] * dummyVariable;
        dummyVariable = dummyVariable * 10;
    }
    
    return functionResult;
}

