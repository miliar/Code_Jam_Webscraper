//
//
//

#include <iostream>
#include <fstream>

using namespace std;

int main(){

    ifstream ifile( "input.txt" );
    ofstream ofile( "output.txt");

    int num_of_testcase = 0;

    ifile >> num_of_testcase;

    for ( int i = 0 ; i < num_of_testcase ; i++ ) {
    
        int num_of_element = 0;
        int result = 0;

        int *vector1 = NULL;
        int *vector2 = NULL;

        ifile >> num_of_element;

        vector1 = new int[  num_of_element ];
        vector2 = new int[  num_of_element ];

        for ( int k = 0; k < num_of_element; k ++ ) {

           ifile >>  vector1[k];

        }

        for ( int l = 0; l < num_of_element; l ++ ) 
        for ( int k = 0; k < num_of_element-1; k ++ ) {

             if ( vector1[k] < vector1[k+1]) {
                  int tmp = vector1[k];
                  vector1[k] = vector1[k+1];
                  vector1[k+1] = tmp;
             }
        }

        for ( int k = 0; k < num_of_element; k ++ ) {

            ifile >> vector2[k];

        }

        for ( int l = 0; l < num_of_element; l ++ )
        for ( int k = 0; k < num_of_element-1; k ++ ) {

             if ( vector2[k] > vector2[k+1]) {
                  int tmp = vector2[k];
                  vector2[k] = vector2[k+1];
                  vector2[k+1] = tmp;
             }
        }

        for ( int k = 0; k < num_of_element; k ++ ) {

            result += vector1[k] * vector2[k]; cout << vector1[k] << " " ;

        }

        ofile << "Case #" << i+1 << ": " << result << endl; 
        delete []vector1;
        delete []vector2;

    }
    return true;
}
