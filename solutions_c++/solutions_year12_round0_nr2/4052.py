#include<iostream>
using namespace std;

int main()
{
    int T, N ,S ,p,score;
    int qt,rem,s_rem,count =0,i,j;
    i =0;
    cin >> T;
    while(i < T)
    {
            cin >> N >> S >> p;
            j= 0;
            count = 0;
            s_rem = S;
            while(j < N)
            {
                    cin >> score;
                    qt = score/3;
                    rem = score%3;
                    if(rem == 0)
                    {
                           if(qt >= p)
                           count++;
                           else if(s_rem >0)
                           {
                                if(qt + 1 >= p && qt > 0)
                                {
                                  count++;
                                  s_rem--;
                                //  cout << "a";
                                }
                           }     
                    }
                    else if(rem == 1)
                    {
                             if(qt + 1 >= p)
                             {
                               count++;
                               //cout << "b";
                             }     
                    }         
                     else  
                     {
                               if(qt + 1 >= p )
                               {
                                     count++;
                               }
                               else if(s_rem > 0)
                               {
                                    if(qt +2 >= p)
                                    {
                                      count++;
                                      s_rem--;
                                    }
                               }
                     }             
                     j++;
           }
           cout << "Case #" <<i+1<< ": " << count << "\n";
           i++;
    }
   // int k;
   // cin >> k;
    return 0;
}                              
                                            
                     
    
