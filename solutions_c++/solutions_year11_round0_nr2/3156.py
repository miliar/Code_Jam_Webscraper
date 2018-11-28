/**

  Google codejam qualification round 2011 Magicka
  Heikki Ikäheimonen
  heikki.ikaheimonen@gmail.com
**/

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

struct Combine{
  char B1;
  char B2;
  char nb;
};

struct Opposite{
  char B1;
  char B2;
};

string magicka(string str);

int main()
{
  int n= 0;
  string cases;
  getline(cin, cases);
  istringstream(cases) >> n;
  int i = 0;
  while(i<n)
  {
    string input;
    getline(cin,input);
    i++;
    cout << "Case #" << i << ": " << magicka(input) << endl;
  }


  return 0;
}

string magicka(string str)
{
  string result = "";
  
  vector<Combine> combines;
  vector<Opposite> opposites;

  int C = 0;
  istringstream iss(str, istringstream::in);
  iss >> C;
  string combStr;
  int i=0;
  while(i<C)
  {
    iss >> combStr;
    Combine comb;
    comb.B1 = combStr.at(0);
    comb.B2 = combStr.at(1);
    comb.nb = combStr.at(2);
    combines.push_back(comb);
    i++;
  }

  int D = 0;
  iss >> D;
  i=0;
  string oppStr;
  while(i<D)
  {
    iss >> oppStr;
    Opposite opposite;
    opposite.B1 = oppStr.at(0);
    opposite.B2 = oppStr.at(1);
    opposites.push_back(opposite);
    i++;
  }

  int N = 0;
  iss >> N;
  string invokes;
  iss >> invokes;

  int invoked = 0;
  string elementList;
  for(int ind=0; ind<invokes.size(); ++ind)
  {
    char el = invokes.at(ind);
 //   cout << "invoke " << el << endl;
    elementList.push_back(el);
    if(elementList.size()>1)
    {
      
      char b1 = elementList.at(elementList.size()-1);
      
      char b2 = elementList.at(elementList.size()-2);

   //   cout << "b1 " << b1 << " b2 " << b2 << endl;

      bool hadCombine = false;
      for(int c=0; c<combines.size(); ++c)
      {
        if((b1 == combines.at(c).B1 && b2 == combines.at(c).B2) ||
           (b1 == combines.at(c).B2 && b2 == combines.at(c).B1)){
          elementList.erase(elementList.end()-2, elementList.end());
          elementList.push_back(combines.at(c).nb);
          hadCombine = true;
        }
      }
      
      if(hadCombine == false)
      {
        for(int op = 0;op<opposites.size(); ++op)
        {
          for(int j=0; j<elementList.size(); ++j)
          {
              b1 = elementList.at(j);
              if((el == opposites.at(op).B1 && b1 == opposites.at(op).B2) ||
                 (el == opposites.at(op).B2 && b1 == opposites.at(op).B1)){
                elementList.clear();
                op = opposites.size();
                j = elementList.size();
              }
          }
        } 
      }

    }
  }


  // process result string
  result.append("[");
  i = 0;
  while(i<elementList.size())
  {
    
    result += elementList.at(i);
    i++;
    if(i<elementList.size()) result.append(", ");
  }
  result.append("]");
  return result;
}
