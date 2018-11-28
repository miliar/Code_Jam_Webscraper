//  Copyright 2012 Sam Boles. All rights reserved.
//

#include <iostream>
using namespace std;
int main ()
{
    //Variables
    int max;
    int NumberOfTests;
    int NumberOfGooglers;
    int RareCases;
    
    //Set up repeater for number of test cases
    cin >> NumberOfTests;
    for (int i = 0; i < NumberOfTests; i++) 
    {
        //main code
        
        cin >> NumberOfGooglers; //gets number of participants
        int Scores[NumberOfGooglers]; //variable for individual scores
        cin >> RareCases;  //gets number of surprising cases
        cin >> max; //gets the score required to quallify
        int min = (max * 3) - 2; //stores value required for non rare cases
        int counter = 0; //variable to count quallified cases
        
        for (int j = 0; j < NumberOfGooglers; j++) 
        {
            cin >> Scores[j];
            if (Scores[j] >= min) 
            {
                counter++;
            }
            else if(Scores[j]>=(min-2) && RareCases > 0 && Scores[j]!=0)
            {
                counter++;
                RareCases--;
            }
        }
        cout << "\nCase #" << i+1 << ": " << counter;        
    }
    return 0;
}


