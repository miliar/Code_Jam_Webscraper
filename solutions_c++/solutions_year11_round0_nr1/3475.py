//
//  main.cpp
//  BotTrust
//
//  Created by Wanasit Tanakitrungruang on 5/7/11.
//  Copyright 2011 Chulalongkorn University. All rights reserved.
//

#include <iostream>

int NUMBER_OF_TESTCASE;
int NUMBER_OF_SEQ;

int time_spent = 0;

void clear();
void doTask_B(int moveTo);
void doTask_O(int moveTo);

void doTestCase(int testNumber)
{
    clear();
    std::cin >> NUMBER_OF_SEQ;
    char color = 0;
    int  moveTo = 0;
   
    for (int i=0; i<NUMBER_OF_SEQ; i++) {
        std::cin >> color;
        std::cin >> moveTo;
        
        if(color == 'O')
            doTask_O(moveTo);
        else
            doTask_B(moveTo);
    }
    
    std::cout << "Case #" << (testNumber+1) << ": " << time_spent << "\n";
    
}



int main (int argc, const char * argv[])
{
    
    std::cin >> NUMBER_OF_TESTCASE;
    
    for (int i=0; i<NUMBER_OF_TESTCASE; i++) {
        doTestCase(i);
    }
    
    return 0;
}



int location_B = 0;
int location_O = 0;

int parrallel_B = 0;
int parrallel_O = 0;

void doTask_B(int moveTo)
{
    int moveTime = abs( moveTo - location_B );
    
    if(moveTime > parrallel_O)
    {
        parrallel_B += (moveTime - parrallel_O) +1;
        time_spent += (moveTime - parrallel_O) +1;
    }
    else
    {
        parrallel_B = 1;
        time_spent += 1;
    }
    
    location_B = moveTo;
    parrallel_O = 0;

}

void doTask_O(int moveTo)
{
    int moveTime = abs( moveTo - location_O );
    
    if(moveTime > parrallel_B)
    {
        parrallel_O += (moveTime - parrallel_B) +1;
        time_spent += (moveTime - parrallel_B) +1;
    }
    else
    {
        parrallel_O = 1;
        time_spent += 1;
    }
    
    location_O = moveTo;
    parrallel_B = 0;
    
}

void clear()
{
    location_O = 1;
    parrallel_O = 0;
    
    location_B = 1;
    parrallel_B = 0;
    
    time_spent=0;
}
