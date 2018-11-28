#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

#define pb push_back
#define fs first
#define sc second

using namespace std;

#define FOUT


int jump[1005];
long long num_people[1005];
long long memoo[1005];
long long num_rides[1005];
bool found_cycle[1005];

vector <long long> groups;


void precalc ( vector <long long> &v, long long maxSize){
        for (int i=0;i<v.size();++i){
                long long tmpSum = 0LL;
                int j;

                for (j=0;j<v.size();++j){
                        tmpSum+=v[(i + j)%v.size()];
                        if ( tmpSum + v[(i+j+1)%v.size()] > maxSize){ ++j;break;}
                    }

                jump[i] = ( i + j ) % v.size();
                num_people[i] = tmpSum;
            }
    }



int main( void ){

#ifdef FOUT
    freopen ( "C-large.in", "r", stdin);
   freopen  ( "C-large.out", "w", stdout);
#endif

    int num_tests , curr_test = 1;
    long long numGroups, maxSum, numRides, tmp;

    scanf ("%d", &num_tests );

    while ( num_tests -- ){

            groups.clear();
            scanf ("%lld %lld %lld", &numRides, &maxSum, &numGroups);

            for (int i=0;i<numGroups;++i){
                    scanf ("%lld", &tmp);
                    groups.pb ( tmp );
                }

            precalc ( groups, maxSum);

            long long earned = 0, curr_ride = 0;
            int curr_index = 0;
            for (int i=0;i<groups.size();++i) memoo[i] = -1LL, found_cycle[i] = false;

            while ( 1 ){


                    if ( found_cycle[curr_index] && curr_ride + num_rides[curr_index] < numRides ){

                            curr_ride+=num_rides[curr_index];
                            earned+=memoo[curr_index];
                            continue;
                        }

                    if ( memoo[curr_index] != -1 && !found_cycle[curr_index]){
                            memoo[curr_index] = earned - memoo[curr_index];
                            num_rides[curr_index] = curr_ride - num_rides[curr_index];

                            found_cycle[curr_index] = true;
                        }




                if ( !found_cycle[curr_index]){
                    memoo[curr_index] = earned;
                    num_rides[curr_index] = curr_ride;
                }
                    earned+=num_people[curr_index];

                    ++curr_ride;
                    curr_index = jump[curr_index];
                    if ( curr_ride == numRides ) break;
                }
            printf ("Case #%d: %lld\n", curr_test, earned);
            curr_test++;
        }


    return 0;
}
