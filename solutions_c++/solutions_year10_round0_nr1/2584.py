
/* Snapper  : Large data set. */

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cassert>

using namespace std;

int main(int argc, char * argv[])
{
        ifstream fin;
        ofstream fout;

        assert(argc == 3);
        // Input file
        fin.open(argv[1]);
        // Output file
        fout.open(argv[2]);
        
        int tc_count = 0;

        // Read total number of test cases.
        fin >> tc_count;

        // Process each test case.
        for(int tc_index = 1; tc_index <= tc_count; tc_index++) {

                long int machine_count = 0;
                long int snap_count = 0;
                bool bulb_status = false;

                fin >> machine_count; // Power Exponent, base 2.
                fin >> snap_count; // Number <= 10 ** 8

                // BIG
                assert(machine_count >= 1);
                assert(machine_count <= 30);

                assert(snap_count >= 0);
                assert(snap_count <= 100000000);
                
                if(snap_count == 0) 
                        bulb_status = false;
                else {
                        // Positive number of snaps. 2 ^ machine_count
                        long int full_snap_count = (int) pow(2.0, (double)machine_count);

                        if((snap_count + 1) % full_snap_count == 0)
                                bulb_status = true;
                        else 
                                bulb_status = false;
                }
                
                if(bulb_status) 
                        fout<<"Case #"<< tc_index <<": "<< "ON" << endl; 
                else
                        fout<<"Case #"<< tc_index <<": "<< "OFF" << endl; 

        } // For each test case

        fin.close();
        fout.close();

        return 0;
}
