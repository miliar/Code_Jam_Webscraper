/**
  Google codejam 2011 qualification rounds Candy Splitting
  Heikki Ikäheimonen
  heikki.ikaheimonen@gmail.com
**/
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

string candySplitting(int candyCount, string str);


int pileSum(vector<int> pile);

int verystupidSum(vector<int> pile);

int main()
{
  int n=0;
  string cases;
  getline(cin,cases);
  istringstream(cases) >> n;

  int i = 0;

  while(i<n)
  {
    int N;
    string str;
    getline(cin,str);
    istringstream(str) >> N;

    string input;
    getline(cin,input);
    i++;
    cout << "Case #" << i << ": " << candySplitting(N, input) << endl;
  }

  return 0;
}

string candySplitting(int candyCount, string str)
{
  string result = "NO";
  
  istringstream iss(str, istringstream::in);

  vector<int> candies;
  int i = 0;
  while(i<candyCount)
  {
    int candy;
    iss >> candy;
    candies.push_back(candy);
    i++;
  }
  
  sort(candies.begin(), candies.end());

  bool cont = true;
  int howmany = 1;
  int beg = 0;
  while(cont)
  {
    
    vector<int> patrics;
    vector<int> seans;

    int patsum = 0;
    int seansum = 0;

    vector<int> candiesCopy = candies;
    
    if(howmany == 1)
    {
      patrics.push_back(candiesCopy.at(beg));
      candiesCopy.erase(candiesCopy.begin()+beg);
    }
    else if(howmany > 1)
    {
      for(int j=0; j<howmany; ++j)
      {
        if(beg<candiesCopy.size())
        {
          patrics.push_back(candiesCopy.at(beg));
          candiesCopy.erase(candiesCopy.begin()+beg);
        }
      }
    }

    seans = candiesCopy;
    

    patsum = pileSum(patrics);
    seansum = pileSum(seans);


    bool compare = false;
    if(patsum <= seansum){

      if(verystupidSum(patrics)==verystupidSum(seans))
      {
        ostringstream res;
        res << seansum;
        return res.str();
      }
    }
  
    beg++;
    if(beg == candies.size())
    {
      beg = 0;
      howmany++;
      if(howmany == candies.size()) cont = false;
    }
  }
  return result;
}


int verystupidSum(vector<int> pile)
{
  if(pile.size() == 1) return pile.at(0);

  int first = pile.at(0);
  for(int i=1; i<pile.size(); ++i){

    first = first ^ pile.at(i);

  }

  return first;

}


int pileSum(vector<int> pile)
{
  int sum = 0;
  for(int i=0; i<pile.size(); ++i)
  {
    sum += pile.at(i);

  }

  return sum;
}

