#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

class Time
{
public:
    Time(string str);
    Time operator +(int rhs);
    bool operator >= (Time rhs);
    bool operator < (Time rhs);
    void display()
    {
        cout << hour << ":" << minute << endl;
    }

private:
    int hour;
    int minute;
};

Time::Time(string str)
{
    stringstream sss;
    sss << str.substr(0, 2);
    sss >> hour;
    stringstream ddd;
    ddd << str.substr(3, 2);
    ddd >> minute;
}

Time Time::operator +(int rhs)
{
    minute += rhs;
    hour += (minute / 60);
    minute %= 60;
    return *this;
}

bool Time::operator >= (Time rhs)
{
    if (hour > rhs.hour)
        return true;
    else if (hour == rhs.hour && minute >= rhs.minute)
        return true;
    return false;
}

bool Time::operator < (Time rhs)
{
    return !(*this >= rhs);
}


void sort(vector<Time>& v)
{
    for (int i=0; i<(int)v.size()-1; ++i)
    {
        for (int j=i+1; j<v.size(); ++j)
        {
            if (v[j] < v[i])
            {
                Time t(v[i]);
                v[i] = v[j];
                v[j] = t;
            }
        }
    }
}

int main(int argc, char** argv)
{
    /*
    Time t("09:57");
    t.display();
    t+60;
    t.display();
    cout << (Time("09:05") >= Time("09:07")) << endl;
    */


    ifstream in(argv[1]);
    int testnum;
    in >> testnum;

    for (int i=0; i<testnum; ++i)
    {
        int T;
        in >> T;
        int NA, NB;
        in >> NA >> NB;
        vector<Time> Abegin;
        vector<Time> Aend;
        vector<Time> Bbegin;
        vector<Time> Bend;

        int ra = NA;
        int rb = NB;

        for (int j=0; j<NA; ++j)
        {
            string begin, end;
            in >> begin >> end;
            Abegin.push_back(Time(begin));
            Aend.push_back(Time(end) + T);
        }

        for (int j=0; j<NB; ++j)
        {
            string begin, end;
            in >> begin >> end;
            Bbegin.push_back(Time(begin));
            Bend.push_back(Time(end) + T);
        }

        /*
        for (int k=0; k<Abegin.size(); ++k)
            Abegin[k].display();
        for (int k=0; k<Bbegin.size(); ++k)
            Bbegin[k].display();
        */

        sort(Abegin);
        sort(Aend);
        sort(Bbegin);
        sort(Bend);

        /*
        for (int k=0; k<Abegin.size(); ++k)
            Abegin[k].display();
        for (int k=0; k<Bbegin.size(); ++k)
            Bbegin[k].display();
        */

        vector<Time> Bendcopy(Bend);
        for (int n=0; n<NA; ++n)
        {
            for (int m=0; m<Bendcopy.size(); ++m)
            {
                if (Abegin[n] >= Bendcopy[m])
                {
                    --ra;
                    Bendcopy.erase(Bendcopy.begin()+m);
                    break;
                }
            }
        }

        vector<Time> Aendcopy(Aend);
        for (int m=0; m<NB; ++m)
        {
            for (int n=0; n<Aendcopy.size(); ++n)
            {
                if (Bbegin[m] >= Aendcopy[n])
                {
                    --rb;
                    Aendcopy.erase(Aendcopy.begin() + n);
                    break;
                }
            }
        }

        cout << "Case #" << i+1 << ": " << ra << " " << rb << endl; 
    }
}
