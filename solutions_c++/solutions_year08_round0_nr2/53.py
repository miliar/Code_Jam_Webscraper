#include <iostream>
#include <fstream>
#include <string>

std::ifstream in("train.in");
std::ofstream out("train.out");

int cases;

int turnaround;
int curr_a, curr_b;
int trips_a, trips_b;

enum event_type
{
    leave_a, leave_b, arrive_a, arrive_b,
};

struct event_t
{
    event_type type;
    int time;
} events[400];
int event_count;

bool operator<(const event_t& a, const event_t& b)
{
    if (a.time == b.time)
        return (a.type == arrive_a || a.type == arrive_b);
    return a.time < b.time;
}

int read_time()
{
    std::string s;
    in >> s;

    return ((s[0]-'0')*10+(s[1]-'0')) * 60 +
           ((s[3]-'0')*10+(s[4]-'0'));
}

void process(int& min_a, int& min_b)
{
    in >> turnaround >> trips_a >> trips_b;

    event_count = 0;

    for (int i = 0; i < trips_a; i++) {
        events[event_count].type = leave_a;
        events[event_count].time = read_time();
        event_count++;
        events[event_count].type = arrive_b;
        events[event_count].time = read_time() + turnaround;
        event_count++;
    }

    for (int i = 0; i < trips_b; i++) {
        events[event_count].type = leave_b;
        events[event_count].time = read_time();
        event_count++;
        events[event_count].type = arrive_a;
        events[event_count].time = read_time() + turnaround;
        event_count++;
    }

    std::sort(events, events + event_count);

    for (int i = 0; i <= trips_a + trips_b; i++)
    for (min_a = 0; min_a <= i; min_a++) {
        min_b = i - min_a;
        curr_a = min_a;
        curr_b = min_b;

        bool fail = false;
        for (int i = 0; i < event_count; i++) {
            switch (events[i].type) {
                case arrive_a:
                    curr_a++;
                    break;
                case arrive_b:
                    curr_b++;
                    break;
                case leave_a:
                    if (curr_a-- == 0)
                        fail = true;
                    break;
                case leave_b:
                    if (curr_b-- == 0)
                        fail = true;
                    break;
            }
            if (fail)
                break;
        }
        if (!fail)
            return;
    }
}

int main()
{
    in >> cases;

    for (int i = 0; i < cases; i++) {
        int a, b;
        process(a, b);
        out << "Case #" << i + 1 << ": " << a << " " << b << "\n"; 
    }
    
    return 0;
}

