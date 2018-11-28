#include <iostream>
#include <cmath>

using namespace std;

int main() {
        int cases;
        int rounds;
        int queue[1000];
        int queue_position;
        int queue_size;
        int seats;
        int groups;
        
        cin >> cases;
        for (int i=0; i<cases; i++) {
                int sum=0;
                cout << "Case #" << i+1 << ": ";
                cin >> rounds;
                cin >> seats;
                cin >> groups;
                queue_position=0;
                
                for (int m=0; m<groups; m++)
                        cin >> queue[m];

                for (int j=0; j<rounds; j++) {
                        int used_seats=0;
                        //                        cout << "NEW ROUND" << endl;
                        int start=queue_position;
                        while (used_seats+queue[queue_position]<=seats) {
                                //      cout << "\tTAKING: " << queue[queue_position] << endl;
                                used_seats+=queue[queue_position];
                                queue_position=(queue_position+1)%groups;
                                if (start==queue_position)
                                        break;
                        }
                        sum+=used_seats;
                }
                cout << sum << endl;
        }
}
