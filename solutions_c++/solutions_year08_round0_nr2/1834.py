#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Event {
    int time;
    char location;
    char type;  // d = depart, r = ready
public:
    Event(int t, char loc, char ty) {
        time = t;
        location = loc;
        type = ty;
    }
    int getTime() { return time; }
    char getLocation() { return location; }
    char getType() { return type; }
};

bool operator<(Event e1, Event e2) {
    if (e1.getTime()==e2.getTime()) {
        if (e2.getType() == 'r') return false;
        else return true;
    } else {
        return e1.getTime()<e2.getTime();
    }
}

int main(int argc, int** argv) {
    int n;
    cin>>n;

    for (int i=0; i<n; i++) {
        int t,na,nb;
        cin>>t>>na>>nb;
        
        // Read in trips
        vector<Event> timeline;
        for (int j=0; j<na; j++) {
            int depart_h,depart_m,arrive_h,arrive_m;
            char colon;
            cin>>depart_h>>colon>>depart_m;
            cin>>arrive_h>>colon>>arrive_m;
            timeline.push_back(Event(depart_h*60+depart_m,'a','d'));
            timeline.push_back(Event(arrive_h*60+arrive_m+t,'b','r'));
        }

        for (int j=0; j<nb; j++) {
            int depart_h,depart_m,arrive_h,arrive_m;
            char colon;
            cin>>depart_h>>colon>>depart_m;
            cin>>arrive_h>>colon>>arrive_m;
            timeline.push_back(Event(depart_h*60+depart_m,'b','d'));
            timeline.push_back(Event(arrive_h*60+arrive_m+t,'a','r'));
        }
        
        sort(timeline.begin(),timeline.end());
        
        int resultA = 0;
        int resultB = 0;
        int currA = 0;
        int currB = 0;
        for (size_t j=0; j<timeline.size(); j++) {
            // Events at a
            if (timeline[j].getLocation() == 'a') {
                if (timeline[j].getType() == 'r') {
                    // train ready
                    currA++;
                } else {
                    // departure
                    if (currA == 0) resultA++;
                    else currA--;
                }
            }
            // Events at b
            if (timeline[j].getLocation() == 'b') {
                if (timeline[j].getType() == 'r') {
                    // train ready
                    currB++;
                } else {
                    // departure
                    if (currB == 0) resultB++;
                    else currB--;
                }
            }
        }
        
        cout<<"Case #"<<i+1<<": ";
        cout<<resultA<<' '<<resultB<<'\n';
    }
    return 0;
}
