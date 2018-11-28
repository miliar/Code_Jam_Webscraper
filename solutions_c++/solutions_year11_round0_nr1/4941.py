#include <iostream>
#include <fstream>

#define O 0
#define B 1
using namespace std;


int main()
{
    ifstream input;
    ofstream output;
    int T;
    
    input.open  ("input.txt",ifstream::in);
    output.open ("output.txt");
    input >> T;
    for (int ncase = 1; ncase <= T; ++ncase)
    {
        int N;
        int current [2],
            last_pressed[2],
            time = 0,
            button ;
        current [ 0 ]  = 1; 
        current [ 1 ]  = 1;
        //memset (last_pressed,0,sizeof (last_pressed));
        last_pressed[0] = 0;
        last_pressed[1] = 0;
        input >> N;
        cout << N<<"\n";
        for (int k = 0; k < N; ++k)
        {
            char robot;
            int r;
            input >> robot; 
           
            if (robot == 'O') r = 0; else r = 1;
            input >> button;
            if (button > current[r])
            {
                   current [r] += time - last_pressed[r];
                               if (current[r] > button)
                                              current [r] = button;

            }
            else 
            {
                   current [r] -= time - last_pressed[r];
                   if (current[r] < button)
                                              current [r] = button;

            }
            time += abs (button - current [r]) + 1;
            last_pressed [r] = time;
            current [r] = button;
            cout << robot << " " <<button <<" "<<time<< " \n";
        }    
        
        output << "Case #"<<ncase<<": "<<time<<"\n";
         
    }
      
 input.close();
 output.close();   
system("PAUSE");
}


