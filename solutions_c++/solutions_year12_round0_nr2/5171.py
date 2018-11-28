#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

char buf[10240];

int STAry1[31];
int STAry2[31];
int numDancer;
int minScore;
int minBetterCount;

int scoreAry[200];

void walkScore(int dancer, int betterCount, int leftSP)
{
  if(dancer == numDancer) {
    if(leftSP != 0) {
      return;
    }
    
    if(minBetterCount < betterCount) {
      minBetterCount = betterCount;
    }
   
    return; 
  }
  
  int leftDancer = numDancer - dancer;
  if(leftDancer < leftSP) {
    return;
  }
  if(leftDancer <= (minBetterCount - betterCount)) {
    return;
  }
  
  const int score = scoreAry[dancer];
  if((leftSP) > 0 && (STAry1[score] > 0)) {
    assert(score > 0);
    if(STAry1[score] >= minScore) {      
      walkScore(dancer + 1, betterCount + 1, leftSP-1);
    }
    else {
      walkScore(dancer + 1, betterCount, leftSP-1);
    }
  }

  if(STAry2[score] >= minScore) {      
    walkScore(dancer + 1, betterCount + 1, leftSP);
  }
  else {
    walkScore(dancer + 1, betterCount, leftSP);
  }        
}


int main(int argc, int* argv)
{
  memset(STAry1, 0, sizeof(STAry1));
  memset(STAry2, 0, sizeof(STAry2));  
  
  for(int i1=0; i1<=10; ++i1) {        
    for(int i2=0; i2<=10; ++i2) {
      int d1 = abs(i1-i2);
      if(d1>2) {
        continue;
      }
      
      for(int i3=0; i3<=10; ++i3) {
        bool isST = false;
        
        if(d1 == 2) {
          isST = true;
        }
                
        int d2 = abs(i1-i3);
        if(d2>2) {
          continue;
        } 
        if(d2 == 2) {
          isST = true;
        }
               
        int d3 = abs(i2-i3); 
        if(d3>2) {
          break;
        } 
        if(d3 == 2) {
          isST = true;
        }           
        
        int maxScore = i1;
        if(maxScore < i2) {
          maxScore = i2;
        }
        if(maxScore < i3) {
          maxScore = i3;
        }      
        
        //printf("%d %d %d %d\n", i1, i2, i3, isST);  
        
        int totalScore = i1 + i2 + i3;
        if(isST) {
          if(STAry1[totalScore] < maxScore) {
            STAry1[totalScore] = maxScore;
          }
        }          
        else {
          if(STAry2[totalScore] < maxScore) {
            STAry2[totalScore] = maxScore;
          }
        }                 
      }
    }
  }
  
  /*
  for(int i = 0; i <31; ++i) {
    printf("%d %d\n", STAry1[i], STAry2[i]);
  }
  */
  
  gets(buf);
  int nt = atoi(buf);
  for(int i=1; i<=nt; ++i) {
    gets(buf);
    char* pch= strtok(buf, " \t");
    assert(pch);
    numDancer = atoi(pch);
    
    pch = strtok(NULL, " \t");
    int ns = atoi(pch);
    
    pch = strtok(NULL, " \t");
    minScore = atoi(pch);    
  
    for(int j=0; j < numDancer; ++j) {
      pch = strtok(NULL, " \t");
      assert(pch);
      scoreAry[j] = atoi(pch);
    }
    
    minBetterCount = 0;
    walkScore(0, 0, ns);
    
    printf("Case #%d: %d\n", i, minBetterCount);
  }
  
  return 0;
}

