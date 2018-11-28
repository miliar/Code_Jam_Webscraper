#include <algorithm>
#include <iostream>
#include <queue>
#include <stack>
#include <vector>


using namespace std;


class Hour
{
    public:

        int minutes;

        Hour(int min = 0) : minutes(min)
        {
        }

        void read(void)
        {
            int hour, min;
            char sep;

            cin >> ws >> hour >> sep >> min;
            minutes = hour * 60 + min;
        }

        void write(void) const
        {
            cout << minutes / 60 << ":" << minutes % 60;
        }

        Hour operator+ (const Hour& hour) const
        {
            int min = (minutes + hour.minutes);
            return Hour(min > 1440 ? min - 1440 : min);
        }

        Hour operator+ (int mins) const
        {
            int min = (minutes + mins);
            return Hour(min > 1440 ? min - 1440 : min);
        }

        Hour operator- (const Hour& hour) const
        {
            int min = (minutes + hour.minutes);
            return Hour(min < 0 ? 1440 - min : min);
        }

        bool operator> (const Hour& hour) const
        {
            return minutes > hour.minutes;
        }

        bool operator<= (const Hour& hour) const
        {
            return minutes <= hour.minutes;
        }
};


class Travel
{
    public:

        Hour departure, arrival;

        void read(void)
        {
            departure.read();
            arrival.read();
        }

        bool operator> (const Travel& travel) const
        {
            return departure > travel.departure;
        }
};


typedef priority_queue<Travel, vector<Travel>, greater<Travel> > TimeTable;
typedef stack<Travel> TravelStack;


class Instance
{
    public:

        int turnaround, count_a, count_b;
        TimeTable station_a, station_b;

        void read(void)
        {
            cin >> ws >> turnaround;
            int size_a, size_b;
            cin >> ws >> size_a >> size_b;

            for(int i = 0; i < size_a; i++) {
                Travel travel;
                travel.read();
                station_a.push(travel);
            }

            for(int i = 0; i < size_b; i++) {
                Travel travel;
                travel.read();
                station_b.push(travel);
            }

            solve();
        }

        void solve(void)
        {
            count_a = count_b = 0;

            while(!station_a.empty() || !station_b.empty()) {
                if(station_a.empty()) {
                    count_b += station_b.size();
                    break;
                }

                if(station_b.empty()) {
                    count_a += station_a.size();
                    break;
                }

                if(station_a.top() > station_b.top()) {
                    count_b++;
                    departing_train(station_b, station_a);
                }
                else {
                    count_a++;
                    departing_train(station_a, station_b);
                }
            }
        }

        void departing_train(TimeTable& station_x, TimeTable& station_y)
        {
            TravelStack travel_stack;
            Travel travel = station_x.top();
            station_x.pop();

            while(!station_y.empty())
                if((travel.arrival + turnaround) <= station_y.top().departure) {
                    departing_train(station_y, station_x);
                    break;
                }
                else {
                    travel_stack.push(station_y.top());
                    station_y.pop();
                }

            while(!travel_stack.empty()) {
                station_y.push(travel_stack.top());
                travel_stack.pop();
            }
        }
};


class Problem
{
    public:

        int size;

        Problem()
        {
            cin >> ws >> size;
            for(int i = 0; i < size; i++) {
                Instance instance;
                instance.read();
                cout << "Case #" << (i + 1) << ": " << instance.count_a << " " << instance.count_b << endl;
            }
        }
};


int main()
{
    Problem();
    return 0;
}
