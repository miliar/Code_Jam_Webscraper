
/* Theme Park : SMALL data set. */

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cassert>
#include <vector>

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

                long int rides_count = 0; // R
                long int kapacity = 0; // k
                long int groups_count = 0; // N
                long int total_money = 0;
                long int total_demand = 0;

                fin >> rides_count >> kapacity >> groups_count; 

                // SMALL data
                assert((1 <= rides_count) && (rides_count <= 1000));
                assert((1 <= kapacity) && (kapacity <= 100));
                assert((1 <= groups_count) && (groups_count <= 10));

                // Store group sizes.
                vector<long int> group_size; 
                group_size.reserve(groups_count);
                total_demand = 0;
                for(long int group_ind = 0; group_ind < groups_count; group_ind++) {
                        long int size;
                        fin >> size;
                        assert(size <= kapacity);

                        group_size[group_ind] = size;
                        total_demand += size;
                }
                
                // Calculated total demand, 1 round.
                // Case : total demand <= kapacity. money = (demand * rides_count) Euros;
                if(total_demand <= kapacity) {
                        total_money = total_demand * rides_count;
                        fout<<"Case #"<< tc_index <<": "<< total_money << endl; 
                        continue; // Next test case
                }
                
                // Case : total demand > kapacity. Divide total demand, wrap around.
                // Process each ride.
                
                total_money = 0;
                long int group_ind = 0;
                for(long int ride_ind = 1; ride_ind <= rides_count; ride_ind++) {

                        long int onboard = 0;

                        // Fill this ride.
                        while(true) {
                                // Add more people.
                                long int next_group_size = group_size[group_ind];    

                                if(onboard + next_group_size <= kapacity) {
                                        // Accept next group.
                                        onboard += next_group_size; 

                                        // Increment group, with wrap around.
                                        if(group_ind == (groups_count-1))  
                                                group_ind = 0;
                                        else 
                                                group_ind++;
                                } else  {
                                        // Cannot take next group. Ride filled.
                                        break;
                                }
                        } // Fill this ride.        

                        total_money += onboard;
                        onboard = 0;
                } // Next ride.

                fout<<"Case #"<< tc_index <<": "<< total_money << endl; 
                total_money = 0;

        } // For each test case

        fin.close();
        fout.close();

        return 0;
}
