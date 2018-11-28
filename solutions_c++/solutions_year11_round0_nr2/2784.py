#include <iostream>
#include <iomanip>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int ti = 1; ti <= T; ti++)
  {
    map<string, char> combine;
    map<char, char> opposed;
    int C, D, N;
    string invokation_list;
    string result;

    cin >> C;
    for(int ci = 0; ci < C; ci++)
    {
      string combination;
      cin >> combination;
      string comb = combination.substr(0,2);
      combine.insert(make_pair(comb, combination[2]));
      swap(comb[0], comb[1]);
      combine.insert(make_pair(comb, combination[2]));
    }

    cin >> D;
    for(int di = 0; di < D; di++)
    {
      string opposites;
      cin >> opposites;
      opposed.insert(make_pair(opposites[0], opposites[1]));
      opposed.insert(make_pair(opposites[1], opposites[0]));
    }

    cin >> N;
    cin >> invokation_list;

    typedef map<string, char>::iterator msciter;
    typedef map<char, char>::iterator mcciter;

    invokation_list += '\001';
    char last = invokation_list[0];
    for(int i = 1; i < N+1; i++)
    {
      char current = invokation_list[i];
      string combination = "";
      combination += last;
      combination += current;
      msciter comb_iter = combine.find(combination);
      mcciter opposite_iter = opposed.find(current);
      if(comb_iter != combine.end())
      {
        opposite_iter = opposed.find(comb_iter->second);
        if(opposite_iter != opposed.end())
        {
          result = "";
          last = '\0';
        }
        else
        {
          result += comb_iter->second;
//          last = comb_iter->second;
          last = '\0';
        }
      }
      else if(opposite_iter != opposed.end() && (result.find(opposite_iter->second) != -1ull || last == opposite_iter->second))
      {
        result = "";
        last = '\0';
      }
      else
      {
        if(last != '\0' && last != '\001')
          result += last;
        last = current;
      }
    }
    
    cout << "Case #" << ti << ": [";
    if(result.size() == 0)
    {
      cout << "]" << endl;
      continue;
    }
    for(size_t i = 0; i < result.size()-1; i++)
    {
      cout << result[i] << ", ";
    }
    cout << result[result.size()-1] << "]" << endl;
  }
}

