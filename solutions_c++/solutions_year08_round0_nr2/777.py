#include <iostream>
#include <sstream>
#include <string>
#include <list>

using namespace std;

string addMinutes(string time, int minutes)
{
    int hour, minute;
    istringstream istream(time);
    ostringstream ostream;
    char temp;
    istream >> hour >> temp >> minute;
    minutes+=minute;
    hour += minutes/60;
    minute = minutes%60;

    if(hour < 10)
        ostream << 0;

    ostream << hour << ":";

    if(minute < 10)
        ostream << 0;
    ostream << minute;


    return ostream.str();
}

int main (int argc, char ** argv)
{
    int N, NA, NB, T, i, j;
    list<string> Ad, Af, Bd, Bf;
    list<string>::reverse_iterator itr_a, itr_b;
    string temp;

    cin >> N;
    for(i = 0; i < N; i++)
    {
        Ad.clear();
        Af.clear();
        Bd.clear();
        Bf.clear();
        cin >> T >> NA >> NB;

        for(j = 0; j < NA; j++)
        {
            cin >> temp;
            Ad.push_back(temp);
            cin >> temp;
            Bf.push_back(addMinutes(temp, T));
        }

        for(j = 0; j < NB; j++)
        {
            cin >> temp;
            Bd.push_back(temp);
            cin >> temp;
            Af.push_back(addMinutes(temp, T));
        }
        Ad.sort();
        Af.sort();
        Bd.sort();
        Bf.sort();
        while(Af.size() && Ad.size())
        {
            itr_a = Af.rbegin();
            itr_b = Ad.rbegin();
            if(*itr_a <= *itr_b)
            {
                Ad.erase(--itr_b.base());
            }
            Af.erase(--itr_a.base());
        }

        while(Bf.size() && Bd.size())
        {
            itr_a = Bf.rbegin();
            itr_b = Bd.rbegin();
            if(*itr_a <= *itr_b)
            {
                Bd.erase(--itr_b.base());
            }
            Bf.erase(--itr_a.base());
        }


        cout << "Case #" << i+1 << ": " << Ad.size() << " " << Bd.size() << endl;
    }

    return 0;
}
