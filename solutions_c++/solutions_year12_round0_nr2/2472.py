//
//  main.cpp
//  GoogleCJ_3
//
//  Created by Michèle De Decker on 14/04/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, const char * argv[])
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    
    int T = 0;
    input >> T;
    input.ignore();
    cout << "T = " << T << endl << endl;
    
    for(int i = 0; i < T; i++)
    {
        int N,S,l = 0;
        input >> N >> S >> l;
        cout << "N = " << N << " S = " << S << " l = " << l << endl;
        int *points = new int[N];
        
        int count = 0;
        for(int j = 0; j < N; j++)
        {
            input >> points[j];
            cout << points[j] << endl;
            if(points[j] > 3*(l-1))
                count++;
            else if(points[j] > 3*(l-2)+1 && 3*(l-2)+1 >= 0 && S > 0)
            {
                S--;
                count++;
            }

        }
                
        output << "Case #" << i+1 << ": " << count << endl;
        
        delete[] points;
    }
    return 0;
}

