#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <map>

//#define DEBUG

void output(size_t a_trains, size_t b_trains, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << a_trains << " " << b_trains << std::endl;
}

// Keeps a sorted list of events (time, value). Pop will return
// one of the values at the given time.
class EventList
{
    public:
    EventList()
    {
    }

    void push(int time, int value) 
    {
        m_map.insert(std::pair<int, int>(time, value));
    }

    int pop(int time)
    {
        int result = 0;
        map_t::iterator iter = m_map.find(time);
        
        if (iter != m_map.end())
        {
            result = iter->second;
            m_map.erase(iter);
        }
        return result;
    }

    int pop_sum(int time)
    {
        int result = 0;
        map_t::iterator iter = m_map.find(time);
        
        while (iter != m_map.end())
        {
            result += iter->second;
            m_map.erase(iter);
            iter = m_map.find(time);
        }
        return result;
    }

#ifdef DEBUG
    static void test()
    {
        EventList e;
        e.push(0,  1);
        e.push(0,  2);
        e.push(1,  3);
        e.push(1,  4);
        e.push(99, 5);

        assert(e.pop(100) == 0);
        assert(e.pop(99) == 5);
        assert(e.pop(99) == 0);
        assert(e.pop_sum(0) == 3);
        assert(e.pop(1) + e.pop(1) == 7);
        assert(e.pop(1) == 0);
        assert(e.pop(0) == 0);
    }
#endif

    private:
    typedef std::multimap<int, int> map_t;
    map_t m_map;
};


class Timetable
{
    public:
    Timetable(size_t turnaround)
        : m_turnaround(turnaround)
    {
#ifdef DEBUG
        std::cout << "turnaround time: " << m_turnaround << std::endl;
#endif
    }

    void add_trip_ab(int start, int end)
    {
#ifdef DEBUG
        std::cout << "adding trip a->b: " << (start/60) << ":" << (start%60)
                                   << " " << (end/60) << ":" << (end%60)
                                   << std::endl;
#endif
        m_leave_a.push(start, end);
    }

    void add_trip_ba(int start, int end)
    {
#ifdef DEBUG
        std::cout << "adding trip b->a: " << (start/60) << ":" << (start%60)
                                   << " " << (end/60) << ":" << (end%60)
                                   << std::endl;
#endif
        m_leave_b.push(start, end);
    }

    static const int LAST_MINUTE = 23 * 60 + 59;

    // Algorithm -- go through each second of the day
    // trains that leave are sent to the future when they will 
    // be available. if no trains are available on a or b, the a/b result
    // is incremented
    void simulate(size_t& result_a, size_t& result_b)
    {
        result_a = result_b = 0;

        int a_avail = 0;
        int b_avail = 0;

        EventList arrive_a;
        EventList arrive_b;

        for (int minute = 0; minute < LAST_MINUTE; ++minute)
        {
            a_avail += arrive_a.pop_sum(minute);
            b_avail += arrive_b.pop_sum(minute);

            for (int arrival = m_leave_a.pop(minute);
                 arrival != 0;
                 arrival = m_leave_a.pop(minute))
            {
                if (!a_avail)
                    ++result_a;
                else
                    --a_avail;

                arrival += m_turnaround;
                arrive_b.push(arrival, 1);
            }

            for (int arrival = m_leave_b.pop(minute);
                 arrival != 0;
                 arrival = m_leave_b.pop(minute))
            {
                if (!b_avail)
                    ++result_b;
                else 
                    --b_avail;

                arrival += m_turnaround;
                arrive_a.push(arrival, 1);
            }
        }
    }

    private:
    size_t m_turnaround;
    EventList m_leave_a;
    EventList m_leave_b;
};

void get_time(size_t& hour, size_t& minute)
{
    char h1, h0, colon, m1, m0;
    std::cin >> h1 >> h0 >> colon >> m1 >> m0;

    hour = 10 * (h1 - '0') + (h0 - '0');
    minute = 10 * (m1 - '0') + (m0 - '0');
}

int main()
{
    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    EventList::test();

    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        size_t turnaround_time;
        std::cin >> turnaround_time;

        Timetable timetable(turnaround_time);

        size_t num_ab, num_ba;
        std::cin >> num_ab >> num_ba;

        for (size_t ab = 0; ab < num_ab; ++ab)
        {
            size_t start_hour, start_minute;
            size_t end_hour, end_minute;
            get_time(start_hour, start_minute);
            get_time(end_hour, end_minute);
            timetable.add_trip_ab(start_hour * 60 + start_minute, end_hour * 60 + end_minute);
        }

        for (size_t ba = 0; ba < num_ba; ++ba)
        {
            size_t start_hour, start_minute;
            size_t end_hour, end_minute;
            get_time(start_hour, start_minute);
            get_time(end_hour, end_minute);
            timetable.add_trip_ba(start_hour * 60 + start_minute, end_hour * 60 + end_minute);
        }

        size_t result_a, result_b;
        timetable.simulate(result_a, result_b);
        output(result_a, result_b, casex);
    }

    return 0;
}
