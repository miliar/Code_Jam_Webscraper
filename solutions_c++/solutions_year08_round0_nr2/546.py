//--------------------------------------------------------------------------------------------------
// Includes
//--------------------------------------------------------------------------------------------------
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cassert>
//--------------------------------------------------------------------------------------------------

class TimeMeasure
{
  public:
         /** @name Accessing **/
         //@{
         unsigned char amountOfMinutes(void) const
         {
             return _amountOfMinutes;
         }
         //@}

         /** @name Instance Creation/Destruction **/
         //@{
         TimeMeasure(unsigned int anAmountInMinutes)
             : _amountOfMinutes(anAmountInMinutes)
         {
             ;//Do Nothing
         }
         //@}

 private:
         //Instance Variables
         unsigned int _amountOfMinutes;
};

class TimeOfDay
{
  public:
         /** @name Aliases **/
         //@{
         typedef TimeOfDay selfClass;
         //@}

         /** @name Accessing **/
         //@{
         unsigned char hour(void) const
         {
             return _hour;
         }
         unsigned char minutes(void) const
         {
             return _minutes;
         }
         //@}

         /** @name Comparing **/
         //@{
         bool operator==(selfClass const& aTimeOfDay) const
         {
             return (this->hour() == aTimeOfDay.hour())
                 && (this->minutes() == aTimeOfDay.minutes());
         }
         bool operator<(selfClass const& aTimeOfDay) const
         {
             return (this->hour() < aTimeOfDay.hour())
                 || ((this->hour() == aTimeOfDay.hour())
                    && (this->minutes() < aTimeOfDay.minutes()));
         }
         //@}

         /** @name Time Arithmetics **/
         //@{
         selfClass operator+(TimeMeasure const& aTimeMeasure) const
         {
             unsigned int newMinutesNotRoundedT60 = this->minutes() + aTimeMeasure.amountOfMinutes();
             return TimeOfDay(this->hour() + (newMinutesNotRoundedT60 / 60), newMinutesNotRoundedT60 % 60);
         }
         //@}

         /** @name Instance Creation/Destruction **/
         //@{
         TimeOfDay(void)
             : _hour(),_minutes()
         {
             ;//Do Nothing
         }
         TimeOfDay(unsigned char anHour, unsigned char aMinutes)
             : _hour(anHour),
             _minutes(aMinutes)
         {
             assert(aMinutes < 60);
         }
         //@}

 private:
         //Instance Variables
         unsigned char _hour;
         unsigned char _minutes;
};

enum TrainEventTypes
{
    TrainDeparture,
    TrainReady
};

class TrainEvent
{
  public:
         /** @name Aliases **/
         //@{
         typedef TrainEvent selfClass;
         //@}

         /** @name Accessing **/
         //@{
         TrainEventTypes type(void) const
         {
             return _type;
         }
         TimeOfDay const& time(void) const
         {
             return _time;
         }
         //@}

         /** @name Comparing **/
         //@{
         bool operator<(selfClass const& aTrainEvent) const
         {
             return (this->time() < aTrainEvent.time())
                 || ((this->time() == aTrainEvent.time())
                    && (this->type() == TrainReady) && (aTrainEvent.type() == TrainDeparture));
         }
         //@}

         /** @name Instance Creation/Destruction **/
         //@{
         TrainEvent(TrainEventTypes aTrainEventType, TimeOfDay const& anEventTime)
             : _type(aTrainEventType), _time(anEventTime)
         {
             ;//Do Nothing
         }
         //@}

 private:
         //Instance Variables
         TimeOfDay       _time;
         TrainEventTypes _type;
};

namespace std
{

::std::istream& operator>>(::std::istream& anInputStream, TimeOfDay& aTimeOfDay)
{
    unsigned int anHour, aMinutes;
    anInputStream >> anHour;
    assert(anInputStream.get() == ':');
    anInputStream >> aMinutes;
    aTimeOfDay = TimeOfDay(anHour, aMinutes);
    return anInputStream;
}

}

typedef ::std::vector<TrainEvent> ListOfTrainEvents;

class TrainTimetableSolver
{
  public:
         /** @name Accessing **/
         //@{
         //@}

         /** @name Evaluating **/
         //@{
         unsigned int operator()(void)
         {
             ::std::sort(_stationTrainEvents.begin(), _stationTrainEvents.end());
             for(ListOfTrainEvents::const_iterator currentTrainEventIterator = _stationTrainEvents.begin();
                 currentTrainEventIterator != _stationTrainEvents.end(); ++currentTrainEventIterator)
             {
                 this->recalculateTrainsDeficitAfter(*currentTrainEventIterator);
             }
             return _maximumTrainsDeficitCount;
         }
         void recalculateTrainsDeficitAfter(TrainEvent const& aTrainEvent)
         {
             switch (aTrainEvent.type())
             {
                 case TrainDeparture:
                     ++_trainsDeficitCount;
                     _maximumTrainsDeficitCount = ::std::max(_maximumTrainsDeficitCount, _trainsDeficitCount);
                     break;
                 case TrainReady:
                     --_trainsDeficitCount;
                     break;
                 default:
                         assert(false);
             }
         }
         //@}

         /** @name Instance Creation/Destruction **/
         //@{
         TrainTimetableSolver(ListOfTrainEvents& aStationTrainEvents)
             : _stationTrainEvents(aStationTrainEvents),
             _maximumTrainsDeficitCount(),
             _trainsDeficitCount()
         {
             ;//Do Nothing
         }
         //@}

 private:
         //Instance Variables
         int                _trainsDeficitCount;
         int                _maximumTrainsDeficitCount;
         ListOfTrainEvents& _stationTrainEvents;
};

class TrainTimetable
{
  public:
         ListOfTrainEvents stationATrainEvents;
         ListOfTrainEvents stationBTrainEvents;
};

class TrainTimetableInputStreamParserAndSolutionWriter
{
  public:
         /** @name Evaluating **/
         //@{
         void operator()(void)
         {
             unsigned int numberOfCases;
             _inputStream >> numberOfCases;
             for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
             {
                 this->parseCase(caseIndex);
             }
         }
         void parseCase(unsigned int aCaseIndex)
         {
             TrainTimetable trainTimetable;
             unsigned int turnaroundTimeInMinutes;
             _inputStream >> turnaroundTimeInMinutes;
             TimeMeasure turnaroundTime(turnaroundTimeInMinutes);
             unsigned int numberOfTripsFromAtoB, numberOfTripsFromBtoA;
             _inputStream >> numberOfTripsFromAtoB >> numberOfTripsFromBtoA;

             unsigned int numberOfAllTrips = numberOfTripsFromAtoB + numberOfTripsFromBtoA;
             trainTimetable.stationATrainEvents.reserve(numberOfAllTrips);
             trainTimetable.stationBTrainEvents.reserve(numberOfAllTrips);
             this->parseNTripsAndAddDepartureAndReadyEventsTo(numberOfTripsFromAtoB, turnaroundTime,
                 trainTimetable.stationATrainEvents, trainTimetable.stationBTrainEvents);
             this->parseNTripsAndAddDepartureAndReadyEventsTo(numberOfTripsFromBtoA, turnaroundTime,
                 trainTimetable.stationBTrainEvents, trainTimetable.stationATrainEvents);

             this->solve(aCaseIndex, trainTimetable);
         }
         void parseNTripsAndAddDepartureAndReadyEventsTo(unsigned int aNumberOfTrips, TimeMeasure aTurnaroundTime,
             ListOfTrainEvents& aListOfTrainEventsToAddDepartureEvents, ListOfTrainEvents& aListOfTrainEventsToAddReadyEvents)
         {
             while (aNumberOfTrips != 0)
             {
                 TimeOfDay aDepartureTime, anArrivalTime;
                 _inputStream >> aDepartureTime >> anArrivalTime;
                 aListOfTrainEventsToAddDepartureEvents.push_back(TrainEvent(TrainDeparture, aDepartureTime));
                 aListOfTrainEventsToAddReadyEvents.push_back(TrainEvent(TrainReady, anArrivalTime + aTurnaroundTime));
                 --aNumberOfTrips;
             }
         }
         void solve(unsigned int aCaseIndex, TrainTimetable& aTrainTimetable)
         {
             unsigned int numberOfTrainsNeededStartingAtStationA = TrainTimetableSolver(aTrainTimetable.stationATrainEvents)();
             unsigned int numberOfTrainsNeededStartingAtStationB = TrainTimetableSolver(aTrainTimetable.stationBTrainEvents)();
             _outputStream << "Case #" << aCaseIndex << ": " << numberOfTrainsNeededStartingAtStationA
                 << " " << numberOfTrainsNeededStartingAtStationB << ::std::endl;
         }
         //@}

          /** @name Instance Creation/Destruction **/
         //@{
         TrainTimetableInputStreamParserAndSolutionWriter(::std::istream& anInputStream, ::std::ostream& anOutputStream)
             : _inputStream(anInputStream), _outputStream(anOutputStream)
         {
             ;//Do Nothing
         }
         //@}
private:
         //Instance Variables
         ::std::istream& _inputStream;
         ::std::ostream& _outputStream;
};

::std::string testCaseFileContents =
"2\n"
"5\n"
"3 2\n"
"09:00 12:00\n"
"10:00 13:00\n"
"11:00 12:30\n"
"12:02 15:00\n"
"09:00 10:30\n"
"2\n"
"2 0\n"
"09:00 09:01\n"
"12:00 12:02";

::std::string testCaseResultsFileContents =
"Case #1: 2 2\n"
"Case #2: 2 0\n";

void runTests(void)
{
    ::std::ostringstream anOutputStringStream;
    TrainTimetableInputStreamParserAndSolutionWriter(::std::istringstream(testCaseFileContents), anOutputStringStream)();
    ::std::string results = anOutputStringStream.str();
    assert(results == testCaseResultsFileContents);
}

void runFromFile(void)
{
    ::std::ifstream inputFileStream("input.txt");
    ::std::ofstream outputFileStream("output.txt");
    TrainTimetableInputStreamParserAndSolutionWriter(inputFileStream, outputFileStream)();
}

int main(int /*argc*/, char* /*argv*/[])
{
    /*runTests();*/
    runFromFile();
    return 0;
}
