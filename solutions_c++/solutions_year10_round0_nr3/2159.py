#include <iostream.h>

int main() {
    
    unsigned int T;

    cin >> T;
    
    unsigned int i;
    for (i = 0; i < T; i++) {
        unsigned long long int R;
        unsigned long long int k;
        unsigned long int N;
        
        unsigned long long int g[1000];
        unsigned int isSeated[1000];
        
        cin >> R;
        cin >> k;
        cin >> N;
        
        unsigned long int j;
        for (j = 0; j < N; j++) {
                cin >> g[j];
                isSeated[j] = 0;
        }
        
        unsigned long int ptr_next_group = 0;

        unsigned long long int curr_ride_no = 0;
        unsigned long long int collections = 0;
        
        for (curr_ride_no = 0; curr_ride_no < R; curr_ride_no++) {
            unsigned long long int no_of_people_in_curr_ride = 0;
            unsigned long int no_of_groups_in_curr_ride = 0;
            unsigned long int ptr_first_group_in_curr_ride = ptr_next_group;

            while (no_of_people_in_curr_ride + g[ptr_next_group] <= k) {
                  if (isSeated[ptr_next_group] == 1) break;

                  no_of_people_in_curr_ride += g[ptr_next_group];
                  no_of_groups_in_curr_ride++;
                  isSeated[ptr_next_group] = 1;
                  ptr_next_group++;
                  ptr_next_group %= N;
            }
            collections += no_of_people_in_curr_ride;
            
            unsigned long int kay;
            for (kay = 0; kay < no_of_groups_in_curr_ride; kay++) {
                isSeated[(ptr_first_group_in_curr_ride + kay) % N] = 0;
            }            
            
        }
           
        cout << "Case #" << i+1 << ": " << collections << endl;
           
    }

}
