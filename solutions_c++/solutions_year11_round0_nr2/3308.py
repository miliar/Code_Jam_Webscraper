//
//  main.cpp
//  Magicka
//
//  Created by Wanasit Tanakitrungruang on 5/7/11.
//  Copyright 2011 Chulalongkorn University. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>

int NUMBER_OF_TESTCASE;
int NUMBER_OF_COMBINE;
int NUMBER_OF_OPPOSED;
int NUMBER_OF_LIST;

int time_spent = 0;

using namespace std;

string elementList;
void putElement(char element);
void clear();

map<int, char> combineMap;
map<char, char> opposedMap;


void doTestCase(int testNumber)
{
    clear();
    
    string text;
    
    std::cin >> NUMBER_OF_COMBINE;
    
    if(NUMBER_OF_COMBINE > 0) std::cin >> text;
    for (int i=0; i<NUMBER_OF_COMBINE; i++) {
        
        combineMap[text[i*3]<<4 + text[i*3+1]] = text[i*3 + 2];
        combineMap[text[i*3+1]<<4 + text[i*3]] = text[i*3 + 2];
    }

    std::cin >> NUMBER_OF_OPPOSED;
    
    if(NUMBER_OF_OPPOSED > 0) std::cin >> text;
    for (int i=0; i<NUMBER_OF_OPPOSED; i++) {
        opposedMap[text[i*3]] = text[i*3 + 1];
        opposedMap[text[i*3 + 1]] = text[i*3];
    }
    
    
    std::cin >> NUMBER_OF_LIST;
    std::cin >> text;
    for (int i=0; i<NUMBER_OF_LIST; i++) {
        putElement(text[i]);
    }
    
    std::cout << "Case #" << (testNumber+1) << ": [";
    for (int i=0; i<elementList.length(); i++) {
        if(i == 0) std::cout << elementList[i];
        else std::cout << ", "<<elementList[i];
    }
    std::cout << "]\n";
}

int main (int argc, const char * argv[])
{
    
    std::cin >> NUMBER_OF_TESTCASE;
    
    for (int i=0; i<NUMBER_OF_TESTCASE; i++) {
        doTestCase(i);
    }
    
    return 0;
}


char lastElement = 0;

void putElement(char element)
{
    
    char combine = combineMap[lastElement<<4 + element];
    if(combine)
    {
        elementList = elementList.erase(elementList.length()-1,1);
        elementList = elementList+combine;
        lastElement = combine;
        
    }
    
    else if(opposedMap[element] && elementList.find(opposedMap[element]) != string::npos)
    {
        elementList.clear();
        lastElement = 0;
    }
    else
    {
        elementList = elementList + element;
        lastElement = element;
    }
}


void clear()
{
    lastElement = 0;
    elementList = "";
    
    combineMap.clear();
    opposedMap.clear();
}
