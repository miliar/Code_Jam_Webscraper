/* 
 * File:   ans2.cpp
 * Author: kunal
 *
 * Created on 17 July, 2008, 11:09 AM
 */

#include <fstream>
#include <iostream>

int strcmp(char str1[], char str2[]) {
    int i;
    for (i=0; str1[i]!='\0' && str2[i]!='\0' && str1[i]==str2[i]; i++);
    return str1[i]-str2[i];
}

int findEarliest(char** arr, bool fDone[], int no) {
    int tmpActualPosn = -1;
    for (int i=0; i<no; i++) 
        if (!fDone[i]) {
            if (tmpActualPosn == -1) tmpActualPosn = i;
            else if (strcmp(arr[tmpActualPosn], arr[i]) > 0) tmpActualPosn = i;
        }
    return tmpActualPosn;
}

int findNext(char* starter, char** arr, bool fDone[], int start, int end) {
    int tmpActualPosn = -1;
    for (int i=start; i<end; i++) {
        if ((!fDone[i]) && (strcmp(arr[i], starter) >= 0)) {
            if (tmpActualPosn == -1) tmpActualPosn = i;
            else if (strcmp(arr[tmpActualPosn], arr[i]) > 0) tmpActualPosn = i;
        }
    }
    return tmpActualPosn;
}

void incrementTime (char* timeStr, char T) { 
    int min = (int(timeStr[3])-48)*10 + (int(timeStr[4])-48);
    int hrs = (int(timeStr[0])-48)*10 + (int(timeStr[1])-48);
    
    min += int(T)-48;
    if (min>60) { min-=60; hrs+=1; }
    
    timeStr[0] = char(hrs/10) + 48;
    timeStr[1] = char(hrs%10) + 48;
    timeStr[3] = char(min/10) + 48;
    timeStr[4] = char(min%10) + 48;
}

void solveTrains (char** dep, char** arr , int forA, int forB, char T, int * Arr) {
    bool* fDone = new bool[forA+forB];
    for (int i=0; i<(forA+forB); i++) fDone[i] = false;
    
    int trainsFromA = 0, trainsFromB = 0;
    int len = forA + forB;
    int currTime, tmpTime;
    
    for (int i=0; i<len; i++) incrementTime (arr[i], T);
    
    do {
        currTime = findEarliest(arr, fDone, len);   //Find the earliest arrival at any station.
        fDone[currTime] = true;               //A train is assigned for that arr/dep
        if (currTime >= forA) trainsFromB++;
        else if (currTime>=0 && currTime<forA) trainsFromA++;
        tmpTime = currTime;
        while (tmpTime !=-1) {
            if (tmpTime >= forA)                       //If the train arrives at A
                tmpTime = findNext(arr[tmpTime], dep, fDone, 0, forA);   //Find the closest departure time from arrival at A 
            else                                       //If the train arrives at B
                tmpTime = findNext(arr[tmpTime], dep, fDone, forA, forA+forB); //Find the closest departure time from arrival at B
            fDone[tmpTime] = true;                  //currenttrain assigned to this schedule
        }
        
    } while (currTime != -1);
    
    Arr[0] = trainsFromA;
    Arr[1] = trainsFromB;
}

int main(int argc, char** argv) {
    int nCases, forA, forB; char T;
    int k=1; int results[2]; 
    
    std::ofstream output2("/home/kunal/Desktop/output.txt"); 
    
    std::cin>>nCases;
    while(k<=nCases) {
        std::cin>>T>>forA>>forB;
        
        
            char ** dep = new char*[forA+forB];
            for (int i=0; i<(forA+forB); i++) dep[i] = new char[6];
            char ** arr = new char*[forA+forB];
            for (int i=0; i<(forA+forB); i++) arr[i] = new char[6];
            for (int j=0; j<forA+forB; j++) std::cin>>dep[j]>>arr[j];
            
            if (forA ==0 || forB==0) {
                output2<< "Case #"<<k<<": "<<forA<<" "<<forB<<"\n";
            }
            else {
                solveTrains (dep, arr, forA, forB, T, results);
                output2<<"Case #"<<k<<": "<<results[0]<<" "<<results[1]<<"\n"; 
            }
            
            delete[] dep;
            
            delete[] arr;
        
        
        
        k++;
    }
   
    output2.close();
    return 0;
}

