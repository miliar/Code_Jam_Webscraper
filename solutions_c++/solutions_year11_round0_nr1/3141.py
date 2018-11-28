#include <iostream>
#include <vector>
using namespace std;

int main()
{
   int T;
   cin >> T;

   for(int i = 0; i < T; i++)
   {
      vector<char> Bot;
      vector<int> Button;
      vector<int> B;
      vector<int> O;
      int opos = 1;
      int bpos = 1;
      int index = 0;
      int bindex = 0;
      int oindex = 0;
      int time = 0;
      int N;
      cin >> N;
      for(int j = 0; j < N; j++)
      {
         char R;
         cin >> R;
         int P;
         cin >> P;

         Bot.push_back(R);
         Button.push_back(P);

         if(R == 'O')
            O.push_back(P);
         else
            B.push_back(P);
      }

      while( index < Bot.size() )
      {
         if( Bot[index] == 'O' && O[oindex] == opos )
         {
            oindex++;
            index++;
            //advance B
            if( bindex < B.size() )
            {
               if( bpos < B[bindex] )
                  ++bpos;
               else if(bpos > B[bindex])
                  --bpos;
            }
            
         }
         else if(Bot[index] == 'B' && B[bindex] == bpos )
         {
            bindex++;
            index++;
            //advance O
            if( oindex < O.size() )
            {
               if( opos < O[oindex] )
                  ++opos;
               else if(opos > O[oindex])
                  --opos;
            }
         }
         else
         {
            //advance B
            if( bindex < B.size() )
            {
               if( bpos < B[bindex] )
                  ++bpos;
               else if(bpos > B[bindex])
                  --bpos;
            }
            //advance O
            if( oindex < O.size() )
            {
               if( opos < O[oindex] )
                  ++opos;
               else if(opos > O[oindex])
                  --opos;
            }
         }

         ++time;
      }

      std::cout << "Case #" << i+1 << ": " << time << std::endl;
   }

}
