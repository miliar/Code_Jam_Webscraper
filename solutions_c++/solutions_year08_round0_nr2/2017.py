#include<iostream>
#include<vector>
#include<string>
#include<list>
#include<algorithm>

using namespace std;

struct Time
{
    int min, sec;
    bool operator < (const Time& other) const
    {
	    if(min<other.min)
		    return true;
	    else if (min == other.min && sec < other.sec)
		    return true;

	    return false;
    }

    bool operator == (const Time& other) const
    {
	if(min == other.min && sec == other.sec)
		return true;
	return false;
    }

    bool operator <= (const Time& other) const
    {
	    if(*this<other || *this==other)
		    return true;
	    else return false;
    }

    friend ostream& operator << (ostream& cout, const Time& time)
    {
	    cout << time.min <<":" << time.sec;
    }
};


Time operator + (const Time& time, int turnarround)
{
	Time newTime;
	int tempSec;

 	tempSec = time.sec + turnarround;
        newTime.sec = tempSec % 60;
        newTime.min = time.min + tempSec/60;

	return newTime;
}

class Trip
{
    public:
	Time depart, arrival;
	char leave;

	bool operator < (const Trip& other) const
	{
	    if ( depart < other.depart )
		    return true;
	    else if (depart == other.depart && arrival < other.arrival)
		    return true;
	    return false;
	}
};

void readTrips(list<Trip>& trips, char leave)
{
	    string timeStr;
	    int min, sec;
	    Trip trip;

	    cin>>timeStr;
	    trip.depart.min = (timeStr[0]-'0') * 10 + timeStr[1]-'0';
	    trip.depart.sec = (timeStr[3]-'0') * 10 + timeStr[4]-'0';
	   
	    cin>>timeStr; 
	    trip.arrival.min = (timeStr[0]-'0') * 10 + timeStr[1]-'0';
	    trip.arrival.sec = (timeStr[3]-'0') * 10 + timeStr[4]-'0';
	    trip.leave = leave;
	    trips.push_back(trip);
}

int main()
{
    int caseNum, T, NA, NB,num=0;

    cin>>caseNum;

    while(caseNum--)
    {
	list<Trip> trips;
	int A=0,B=0;

	cin>>T>>NA>>NB;
	for(int i = 0; i< NA; i++)
	    readTrips(trips, 'A');

	for(int i = 0; i< NB; i++)
	    readTrips(trips, 'B');

	trips.sort();

	while(!trips.empty())
	{
	    list<Trip>::iterator tempIterator;
	    Time newDepart = trips.front().arrival + T;
	    char newLeave = trips.front().leave;

	    tempIterator = trips.erase(trips.begin());

	    if(newLeave == 'A' )
		    A++;
	    else B++;

	    while (tempIterator!=trips.end())
	    {
		if(newDepart <= (*tempIterator).depart && newLeave != (*tempIterator).leave)
		{   
		    newDepart = (*tempIterator).arrival + T;
		    newLeave = (*tempIterator).leave;
		    tempIterator = trips.erase(tempIterator);
		}
		else tempIterator++;	
	    }
	}

	cout << "Case #" << ++num << ": " << A << " " << B << endl;
    }

    return 0;
}
