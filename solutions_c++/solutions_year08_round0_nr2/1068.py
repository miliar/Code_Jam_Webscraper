#include <iostream>
#include <queue>
#include <utility>

struct Event {
    char station;
    int time;
    int trains;
    
    Event (int _time, char _station, int _trains)
        : station (_station), time (_time), trains (_trains) { };
    
    bool before (const Event& ev) const {
        if (this->time < ev.time) return true;
        else if (this->time > ev.time) return false;
        else return this->trains > ev.trains;
    }
    
    bool operator< (const Event& ev) const {
        return ev.before (*this);
    }
};

inline int read_time (std::istream& in) {
    int hours, minutes;
    in >> hours;
    in.ignore (1, ':');
    in >> minutes;
    return minutes + (hours * 60);
}

int main () {
    
    int cases;
    std::cin >> cases;
    
    std::priority_queue<Event> events;
    
    for (int case_num=1; case_num<=cases; ++case_num) {
        
        int turnaround;
        std::cin >> turnaround;
        
        int A_departures, B_departures;
        std::cin >> A_departures >> B_departures;
        
        char from = 'A', to = 'B';
        
        for (int i=-A_departures; i<B_departures; ++i) {
            
            if (i == 0) std::swap (from, to);
            
            int departure = read_time (std::cin);
            int arrival = read_time (std::cin);
            
            events.push (Event (departure, from, -1));
            events.push (Event (arrival+turnaround, to, +1));
        }
        
        int A_available = 0, B_available = 0;
        int A_required = 0, B_required = 0;
        
        while (!events.empty()) {
            
            if (events.top().station == 'A') {
                
                A_available += events.top().trains;
                
                if (A_available < 0) {
                    A_required -= A_available;
                    A_available = 0;
                }
            }
            else {
                
                B_available += events.top().trains;
                
                if (B_available < 0) {
                    B_required -= B_available;
                    B_available = 0;
                }
            }
            
            events.pop();
        }
        
        std::cout << "Case #" << case_num << ": "
                  << A_required << ' ' << B_required << std::endl;
    }
}
