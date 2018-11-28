//Magicka.cpp
#include <fstream>
#include <vector>
#include <iostream>
#include <iterator>
#include <stdio.h>
using namespace std;
vector<char> v;
int letters[26];
char combineRules[26][26];
int ClearRule[26][26];

void push(char c)
{
  v.push_back(c);
  letters[c-'A']+=1;
}
void pop(char c)
{
  v.pop_back();
  letters[c-'A']-=1;
}
void clear()
{
  v.clear();
  for(int i=0;i<26;i++)
  {
    letters[i]=0;
  }
}
void reset()
{
  v.clear();
  for(int i=0;i<26;i++)
  {
    letters[i] =0;
    for (int j=0;j<26;j++)
    {
      ClearRule[i][j]=0;
      combineRules[i][j]=0;
    }
  }
}
  void AddCombineRule(char a, char b, char c)
  {
    int l = a-'A';
    int r = b-'A';
    combineRules[l][r]=c;
    combineRules[r][l]=c;
  }


void AddClearRule(char a, char b)
  {
    int l = a-'A';
    int r = b-'A';
    ClearRule[l][r]=1;
    ClearRule[r][l]=1;
  }
  bool TryClear(char a)
  {
    int index = a-'A';
    int* rule = ClearRule[index];
    for(int i=0;i<26;i++)
    {
      if (letters[i] && rule[i])
      {
       //printf("true \n");
        return true; 
      }
    }
    //printf("false \n");
    return false;
  }
  char TryCombine(char a, char b)
  {
    int l = a-'A';
    int r = b-'A';
    return combineRules[l][r];
  }

void ReadChar(char a)
{
    if(v.empty())
    {
      push(a);
      return;
    }
    char b = v.back();
    char c= TryCombine(a, b);
    //printf("try combine %c %c %c\n", a, b, c);
    if (c!=0)
    {
      pop(b);
      push(c);
      return;
    }
    
    if (TryClear(a))
    {
      clear();
      return;
    }
    
    push(a);
  }

void magicka(int caseNumber, ifstream& f)
{
  reset();

  int nCombineRules;
  f >> nCombineRules;
  for (int i=0;i<nCombineRules;i++)
  {
    char a,b,c;
    f >> a >> b >> c;
    //printf("Add combine rule %c %c %c \n", a, b, c);
    AddCombineRule(a, b, c);
  }

  int nClearRules;
  f >> nClearRules;
  for (int i=0;i<nClearRules;i++)
  {
    char a, b;
    f >> a>>b;
    //printf("Add clear rule %c %c \n", a, b);
    AddClearRule(a, b);
  }

  int count;
  f >> count;
  
  for(int i=0;i<count;i++)
  {
    char c;
    f >> c;
    ReadChar(c);
  }
  cout << "Case #"<< caseNumber << ": [";
  int nChars = v.size();
  if (nChars > 0)
  {
    for(int i=0;i< nChars-1;i++)
    {
      cout << v[i] << ", ";
    }
    cout << v.back() << "]" << endl;
  }
  else
  {
    cout << "]" << endl;
  }
}

int main(int argc, char** argv)
{
  if (argc!=2) return -1;

  ifstream f(argv[1]);
  //ifstream f("d:\\jam\\magicka\\test.in");
  int lines;
  f >> lines;
  for (int i=0;i<lines;i++)
  {
    magicka(i+1, f);
  }
}