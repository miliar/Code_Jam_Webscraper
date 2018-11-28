#include <stdio.h>
#include <iostream.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <fstream.h>

ofstream fileOut("C:\\codejam\\alienDict\\A-small-attempt2.out");



void getWordsWithoutParenthesis(char inputWord[], char inputWordArray[][50],long &numberOfTotalWords)
{
  long len = strlen(inputWord);

  bool openParen = false, atleastOneParenFound = false;

  int j = 0, index = 0;

  for( int i = 0; i < len; i++)
  {
    if(inputWord[i] == '(')
    {
      openParen = true;
      atleastOneParenFound = true;
    }
    else if(inputWord[i] == ')')
    {
      inputWordArray[j][index] = '\0';
      numberOfTotalWords++;
      index = 0;
      j++;
      openParen = false;
    }
    else
    {
      if(openParen == true)
      {
       inputWordArray[j][index] = inputWord[i];
       index++;
      }
      else
      {
        inputWordArray[j][0] = inputWord[i];
        inputWordArray[j][1] = '\0';
        numberOfTotalWords++;
        j++;
      }
    }
  }

  if(atleastOneParenFound == false)
    numberOfTotalWords = 1;
}


bool strstr1(char *str, char c)
{
  for( int i = 0; str[i] != '\0'; i++)
  {
    if(str[i] == c)
    {
      return true;
    }
  }

  return false;
}

long getNumberOfWordsMatchingDictionary(char inputWordArray[50][50], char dictionary[5000][20], long numberOfWordsinDict,long numOfTotalWordsInput, long numberOfLetters)
{
  long totalMatching = 0,k=0;
  char word[20];
  bool found  = false;

  for(int i = 0; i < numberOfWordsinDict; i++)
  {
    strcpy(word,dictionary[i]);

    word[numberOfLetters + 1] = '\0';

    long len = numberOfLetters;

    for( int j = 0; j < len; j++) //"abc"
    {
      char c = word[j]; // 'a'

      while( k < numOfTotalWordsInput)
      {
        if(strstr1(inputWordArray[k],c))
        {
          found = true;
          break;
        }
        else
        {
          found = false;
          break;
        }
      }

      if(found == false)
      {
        k = 0;
        break;
      }
      else
      {
        k++;

        if(k == numberOfLetters)
        {
          totalMatching++;
          k = 0;
          break;
        }
      }

    }
  }

  return totalMatching;

}

int main()
{
  

  long numberOfLetters = 0;
  long numberOfWords = 0;
  long numberOfCases = 0, numOfMatches = 0;
  long numOfTotalWords = 0;

  char inputWord[250];
  char inputWordArray[50][50];



  ifstream fileIn("C:\\codejam\\alienDict\\A-small-attempt2.in");
  


  fileIn>>numberOfLetters;
  fileIn>>numberOfWords;
  fileIn>>numberOfCases;

 

  char dictionary[5000][20];
    

  for(int i = 0; i < numberOfWords; i++)
  {
    fileIn>>dictionary[i];    
  }
    
    
  for(int j = 1;j <= numberOfCases; j++)
  {
    fileIn>>inputWord;


    numOfTotalWords = 0;
    numOfMatches = 0;

    getWordsWithoutParenthesis(inputWord,inputWordArray,numOfTotalWords);

    if(numOfTotalWords > 1)
    {
      numOfMatches = getNumberOfWordsMatchingDictionary(inputWordArray,dictionary,numberOfWords, numOfTotalWords, numberOfLetters);
      
      fileOut<<"Case #"<<j<<": ";
      fileOut<<numOfMatches;
      fileOut<<endl;
    }
    else if( numOfTotalWords == 1)
    {
      for(int k = 0; k < numberOfWords; k++)
      {
        if(strcmp(inputWord,dictionary[k]) == 0)
        {
          numOfMatches++;          
          break;
        }
      }
      fileOut<<"Case #"<<j<<": ";
      fileOut<<numOfMatches;
      fileOut<<endl;
    }
    
  }
  
      
  return 0;
  
}
