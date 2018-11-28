#include <iostream>
#include <vector>

using namespace std;

int calc(vector<int> &lst, string a, int k)
{
   string b = "";
   for(int i = 0; i < a.length(); i++)
   {
      b = b + a[(i/k)*k+lst[i%k]];  
   }

    char last = 0;
    int sofar  = 0;
   for(int i = 0; i < b.size(); i++)
   {
     if (b[i] != last) { sofar++; last = b[i]; }
   }
   return sofar;

}

int main()
{
  int tests;
  cin >> tests;
  int cases =1;
  while (tests-- > 0)
  {
     int k = 0;
     cin >> k;
     string blah;
     cin >> blah;
     vector<int> lst(k);
     for(int i = 0; i < k; i++)
       lst[i] = i;
     int sofar = 0x7000000;
     do
     {
       sofar = min(sofar, calc(lst,blah,k));
     } while (next_permutation(lst.begin(), lst.end()));

     cout << "Case #" << cases++ << ": " << sofar << endl;   
  }
}
