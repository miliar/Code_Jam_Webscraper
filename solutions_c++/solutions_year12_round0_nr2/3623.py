#include <iostream>
#include <string>
using namespace std;

int main()
{
    int caseNum;
    cin >> caseNum;
    for(int i = 1; i <= caseNum ; i++)
    {
        cout << "Case #" << i << ": " ;
        int total = 0;
        int numDancer, supriseNum, cut;
        cin >> numDancer >> supriseNum >> cut;
        int* dancer = new int[numDancer];
        for(int i = 0 ; i < numDancer; i++)
        {
            cin >> dancer[i];
            int ave = dancer[i]/3;
            if(dancer[i] == 0)
            {
                if(cut == 0)
                {
                    total++;
                }                
            }
            else if(dancer[i] >= 3*cut - 2)
            {
                total ++;
            }
            else if(dancer[i] >= 3*cut -4)
            {  
                if(supriseNum > 0)
                {
                  total ++;
                  supriseNum--;
                }
            }
        }
        cout << total <<endl;
    }
}