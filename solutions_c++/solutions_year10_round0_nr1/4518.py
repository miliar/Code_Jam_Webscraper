#include <iostream>
#include <fstream>
using namespace std;

int main()
{

    bool power[40];
    bool on[40];

    ifstream cin("A-small-attempt0.in");

    ofstream cout("output.txt");

    for(int i=0;i<40;i++)
    {
        power[i] = false;
        on[i] = false;
    }
    int n ;
    cin >> n;



    for(int i=0; i<n;i++)
    {
         int N,K;
         cin >> N >> K;

         power[N-1] = 1;
         for(int j=0;j<K;j++)
         {
              for(int w=0;w<N;w++)
              {
                    if(power[w]== true)
                    {
                        on[w] = !on[w];

                    }

              }

            for(int z=N-1;z>0;z--)
              {
                    if(power[z]== true && on[z] == true)
                    {
                        power[z-1] = true;

                    }
                    else
                        break;

              }


              for(int z=N-1;z>=0;z--)
              {
                    if(on[z]== false || (on[z] == true && power[z] == false))
                    {
                        for(int m = z-1; m>=0;m--)
                        {
                            power[m] = false;
                        }

                        break;
                    }
              }

         }




    if(power[0] == true && on[0] == true)
    {
        cout << "Case #" << i+1 << ": "<< "ON" << endl;

    }
    else
        cout << "Case #" << i+1 << ": "<< "OFF" << endl;


    for(int i=0;i<40;i++)
    {
        power[i] = 0;
        on[i] = 0;
    }



    }


}
