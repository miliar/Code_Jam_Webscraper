#include <iostream>
#include <fstream>
#include <map>
#include <set>

//#define DEBUG

class TrainInfo
{
public:
    TrainInfo(int depart_, int arrive_)
	: depart(depart_),
	  arrive(arrive_)
	{}

    bool operator<(const TrainInfo& rhs) const
	{
	    if (depart != rhs.depart)
		return depart < rhs.depart;
	    return arrive < rhs.arrive;
	}

    friend std::ostream& operator<<(std::ostream& os, const TrainInfo& train);

    int depart;
    int arrive;
};

std::ostream& operator<<(std::ostream& os, const TrainInfo& train)
{
    os << train.depart / 60 << ":" << train.depart % 60 << " "
       << train.arrive / 60 << ":" << train.arrive % 60;
    return os;
}

int main()
{
    int numTestCases = 0;
    std::cin >> numTestCases;

    typedef std::multiset<TrainInfo> TrainMap;
    typedef TrainMap::iterator TMI;
    typedef std::multiset<int> TrainAvailMap;
    typedef TrainAvailMap::iterator TAMI;

    char colon;

    for (int i = 0; i < numTestCases; ++i)
    {
	int numStartingA = 0;
	int numStartingB = 0;

	int turnAroundTime = 0;
	std::cin >> turnAroundTime;
#if defined(DEBUG)
	std::cout << "Turnaround: " << turnAroundTime << std::endl;
#endif

	int numTrainsA = 0;
	std::cin >> numTrainsA;

	int numTrainsB = 0;
	std::cin >> numTrainsB;

	TrainMap scheduledA;
	for (int j = 0; j < numTrainsA; ++j)
	{
	    int departureHour = 0;
	    int departureMin = 0;
	    int arrivalHour = 0;
	    int arrivalMin = 0;
	    std::cin >> departureHour >> colon >> departureMin >> arrivalHour >> colon >> arrivalMin;
	    int departure = departureHour * 60 + departureMin;
	    int arrival = arrivalHour * 60 + arrivalMin;
	    scheduledA.insert(TrainInfo(departure, arrival));
	}

	TrainMap scheduledB;
	for (int j = 0; j < numTrainsB; ++j)
	{
	    int departureHour = 0;
	    int departureMin = 0;
	    int arrivalHour = 0;
	    int arrivalMin = 0;
	    std::cin >> departureHour >> colon >> departureMin >> arrivalHour >> colon >> arrivalMin;
	    int departure = departureHour * 60 + departureMin;
	    int arrival = arrivalHour * 60 + arrivalMin;
	    scheduledB.insert(TrainInfo(departure, arrival));
	}

	TrainAvailMap availableA, availableB;
	TMI iterA = scheduledA.begin();
	TMI iterB = scheduledB.begin();

	while ((iterA != scheduledA.end()) || (iterB != scheduledB.end()))
	{
	    TrainInfo trainA(24 * 60, 24 * 60);
	    TrainInfo trainB(24 * 60, 24 * 60);

	    if (iterA != scheduledA.end())
	    {
		trainA = *iterA;
	    }

	    if (iterB != scheduledB.end())
	    {
		trainB = *iterB;
	    }

	    if (trainA < trainB)
	    {
#if defined(DEBUG)
		std::cout << trainA;
#endif
		TAMI availItr = availableA.begin();
		if ((availItr != availableA.end()) &&
		    (*availItr <= trainA.depart))
		{
		    
		    availableA.erase(availItr);
		}
		else	
		{
#if defined(DEBUG)
		    std::cout << "*";
#endif
		    ++numStartingA;
		}
		availableB.insert(trainA.arrive + turnAroundTime);
		++iterA;
	    }
	    else
	    {
#if defined(DEBUG)
		std::cout << "                    " << trainB;
#endif
		TAMI availItr = availableB.begin();
		if ((availItr != availableB.end()) &&
		    (*availItr <= trainB.depart))
		{
		    availableB.erase(availItr);
		}
		else	
		{
#if defined(DEBUG)
		    std::cout << "*";
#endif
		    ++numStartingB;
		}
		availableA.insert(trainB.arrive + turnAroundTime);
		++iterB;
	    }
#if defined(DEBUG)
	    std::cout << std::endl;
#endif
	}

	std::cout << "Case #" << i+1 << ": " << numStartingA << " " << numStartingB << std::endl;
#if defined(DEBUG)
	std::cout << std::endl;
#endif
    }

    return 0;
}
