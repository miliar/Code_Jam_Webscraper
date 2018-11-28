#include <stdio.h>
#include <string>
#include <vector>

using std::string;
using std::vector;

enum station
{
 STATION_A,
 STATION_B
};

class trip
{
private:
 station departure_station;
 int departure_time, arrival_time;

public:
 trip(station d, int dep_time, int arr_time) { departure_station = d; departure_time = dep_time; arrival_time = arr_time; }
 int arrival() { return arrival_time; }
 int departure() { return departure_time; }
 station dep_station() { return departure_station; }

 bool isFinished(int t, int turnaround) {
                          if(t < arrival_time + turnaround)
                           return false;
                          else
                           return true;
                         }
 bool operator>(trip t) {
                         if(departure_time > t.departure_time)
                          return true;
                         else
                          return false;
                        }
 bool operator<(trip t) {
                         if(departure_time < t.departure_time)
                          return true;
                         else
                          return false;
                        }
 bool operator==(trip t) {
                          if(!(departure_station == t.departure_station))
                           return false;
                          if(!(departure_time == t.departure_time))
                           return false;
                          if(!(arrival_time == t.arrival_time))
                           return false;
                          return true;
                         }
};

class train
{
private:
 vector<trip> trips;
 station origin;

public:
 train(station s, trip t, int turnaround) { origin = s; addTrip(t, turnaround); }
 bool isOrigin(station s) { if(origin == s) return true; return false; }
 void setOrigin(station s) { origin = s; }
 bool addTrip(trip t, int turnaround) {
                                        if(trips.empty())
                                        {
                                         trips.push_back(t);
                                         origin = t.dep_station();
                                         return true;
                                        }

                                        vector<trip>::iterator it = trips.begin();
                                        if(t.dep_station() != trips.back().dep_station() && trips.back().isFinished(t.departure(), turnaround))
                                        {
                                         trips.push_back(t);
                                         return true;
                                        }
                                        return false;
                                       }
};

void main ()
{
 FILE* input_file;
 char filename[1024];
 string output = "";

 // Opening input file
 printf("Type the name of the input file: ");
 gets(filename);
 input_file = fopen(filename, "rt");
 while(!input_file)
 {
  printf("There's been a problem opening the input file. Type the name of the file again: ");
  gets(filename);
  input_file = fopen(filename, "rt");
 }

 // Reading input file and processing
 int case_num, NA, NB, hour_tmp, min_tmp, turnaround, trains_A = 0, trains_B = 0;
 char tmp[128];
 station origin;
 vector<train> trains;
 vector<train>::iterator train_iterator;
 vector<trip> trips;
 vector<trip>::iterator trips_iterator;

 fscanf(input_file, "%d\n", &case_num);

 for(int c = 0; c < case_num; c++)
 {
  fscanf(input_file, "%d\n", &turnaround);

  fscanf(input_file, "%d", &NA);
  fscanf(input_file, "%d", &NB);

  origin = STATION_A;
  for(int s = 0; s < NA; s++)
  {
   fscanf(input_file, "%d:%d ", &hour_tmp, &min_tmp);
   int dep_time = 60*hour_tmp + min_tmp;
   fscanf(input_file, "%d:%d\n", &hour_tmp, &min_tmp);
   int arr_time = 60*hour_tmp + min_tmp;

   if(trips.empty())
    trips.push_back(trip(origin, dep_time, arr_time));
   else
   {
    vector<trip>::iterator it = trips.begin();
    trip t(origin, dep_time, arr_time);
    while(it != trips.end())
    {
     if(t < *it)
      break;

     it++;
    }
    if(it == trips.end())
     trips.push_back(t);
    else
     trips.insert(it, t);
   }
  }

  origin = STATION_B;
  for(int s = 0; s < NB; s++)
  {
   fscanf(input_file, "%d:%d", &hour_tmp, &min_tmp);
   int dep_time = 60*hour_tmp + min_tmp;
   fscanf(input_file, "%d:%d\n", &hour_tmp, &min_tmp);
   int arr_time = 60*hour_tmp + min_tmp;

   if(trips.empty())
    trips.push_back(trip(origin, dep_time, arr_time));
   else
   {
    vector<trip>::iterator it = trips.begin();
    trip t(origin, dep_time, arr_time);
    while(it != trips.end())
    {
     if(t < *it)
      break;

     it++;
    }
    if(it == trips.end())
     trips.push_back(t);
    else
     trips.insert(it, t);
   }
  }

  for(trips_iterator = trips.begin(); trips_iterator != trips.end(); trips_iterator++)
  { 
   for(train_iterator = trains.begin(); train_iterator != trains.end(); train_iterator++)
   {
    if(train_iterator->addTrip(*trips_iterator, turnaround))
     break;
   }
   if(train_iterator == trains.end())
   {
    trains.push_back(train(trips_iterator->dep_station(), *trips_iterator, turnaround));
   }
  }

  // Checking number of trains
  for(train_iterator = trains.begin(); train_iterator != trains.end(); train_iterator++)
  {
   if(train_iterator->isOrigin(STATION_A))
    trains_A++;
   else
    trains_B++;
  }

  sprintf(tmp, "Case #%d: %d %d\n", c+1, trains_A, trains_B);
  output += tmp;
  trips.clear();
  trains.clear();
  trains_A = trains_B = 0;
 }

 // Writing output
 FILE* output_file = fopen("output3.txt", "wt");
 if(!output_file)
 {
  printf("There's been a problem creating the output file. The program will be finished without writing the output.");
  exit(0);
 }
 fprintf(output_file, "%s", output.c_str());

 fclose(output_file);
 fclose(input_file);
}