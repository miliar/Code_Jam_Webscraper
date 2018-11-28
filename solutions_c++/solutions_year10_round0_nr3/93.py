#include <iostream>
#include <vector>

using namespace std;


int main()
{
   int cases;
   cin >> cases;
   int c = 1;
   while (cases-- > 0)
   {
     int r, k, n;
     cin >> r >> k >> n;
     vector<int> people;
     while (n-- > 0)
     {
        int t;  
        cin >> t;
        people.push_back(t);
     }
     vector<int> pos(people.size(), 0);
     vector<int> sums(people.size(), 0);

     for(int i = 0; i < people.size(); i++)
     {
         int sum = 0; 
         int j = i;
         for(; j < people.size()+i; j++)
         {
             sum += people[j%people.size()];
             if (sum > k)
             {
                sum -= people[j%people.size()];
                break;
             }
            
         }
         pos[i] = j%people.size();
         sums[i] = sum;
     }


     long long revenue = 0;
     int p = 0;
     while(r-- > 0)
     {
         revenue += sums[p];
         p = pos[p];
     }
     cout << "Case #" << c++ << ": " << revenue << endl;

   }
}
