#include <cstdlib>
#include <iostream>
#include <queue>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fileIn("C-small-attempt0.in");
    ofstream fileOut("C-small.out");
    int R,k,N,cant,temp;
    fileIn >> cant;  // cases
    queue<int> q1;  //waiting
    queue<int> q2;  //seated
    int val;  // seats left
    int amount = 0; // $euros$
    for(int i=0;i<cant;i++)
    {
            amount =0;
            fileIn >> R;
            fileIn >> k;
            fileIn >> N;
            for(int j=0;j<N;j++)
            {
                    fileIn >> temp;
                    q1.push(temp);
            }  
            
            for(int z=0;z<R;z++)
            {
                    val=k;
                    while(!q1.empty() && val >= q1.front())
                    {
                           temp = q1.front();
                           val -= temp;
                           q1.pop();
                           q2.push(temp);
                    }
                    amount += k-val;
                    while( !q2.empty())
                    {
                           temp = q2.front();
                           q2.pop();
                           q1.push(temp);
                    }

            } 
            while( !q1.empty())
            {
                   q1.pop();            
            }
            while( !q2.empty())
            {
                   q2.pop();            
            }
            fileOut << "Case #" << i+1 << ": " << amount << endl;                     
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
