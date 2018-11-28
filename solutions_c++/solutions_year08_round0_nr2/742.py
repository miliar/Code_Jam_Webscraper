#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;
static   ifstream input ("exo2_input");


struct timespan
{
  int hour;
  int min;

  void Read (ifstream& in)
  {
    in >> hour;
    in.get(); // passe le ':'
    in >> min;
  }

  void add(int turnover)
  {
    min += turnover;
    hour += min / 60;
    min %= 60;
  }

  bool operator<(const timespan& t) const
  {
    return hour < t.hour || (hour == t.hour && min < t.min);
  }

  bool operator<=(const timespan& t) const
  {
    return hour < t.hour || (hour == t.hour && min <= t.min);
  }

};

struct Trip
{
  timespan start;
  timespan ready;
  Trip* prev;
  Trip* next;

  int id;

  Trip() : prev (0), next(0) {}

  void Read (ifstream& in, int trip_id)
  {
    start.Read(in);
    in.get(); // passe le ' '
    ready.Read(in);
    id = trip_id;
  }
  bool operator<(const Trip& t) const
  {
    return start < t.start;
  }
};

struct schedule
{
  int from_a;
  int from_b;
};

void remove_trip(Trip* trips, int& nb_trips, int index)
{
  --nb_trips;
  while (index < nb_trips)
    trips[index] = trips[index+1];
}


schedule solve_case(int nb_a_to_b, int nb_b_to_a, Trip* a_to_b, Trip* b_to_a, int turnover)
{
  schedule res;
  res.from_a = nb_a_to_b;
  res.from_b = nb_b_to_a;

  // Handle the turnover constraint
  for (int t = 0; t < nb_a_to_b; ++t)
    a_to_b[t].ready.add(turnover);
  for (int t = 0; t < nb_b_to_a; ++t)
    b_to_a[t].ready.add(turnover);

  sort(a_to_b, a_to_b + nb_a_to_b);
  sort(b_to_a, b_to_a + nb_b_to_a);

  int nb_changes;
  do
  {
    nb_changes = 0;
    for (int a = 0; a < nb_a_to_b; ++a)
      for (int b = 0; b < nb_b_to_a; ++b)
        if (a_to_b[a].ready <= b_to_a[b].start &&
            a_to_b[a].next == 0 && b_to_a[b].prev == 0)
        {
          res.from_b--;
          ++nb_changes;
          a_to_b[a].next = &b_to_a[b];
          b_to_a[b].prev = &a_to_b[a];
        }
        else if (b_to_a[b].ready <= a_to_b[a].start &&
                 b_to_a[b].next == 0 && a_to_b[a].prev == 0)
        {
          res.from_a--;
          ++nb_changes;
          b_to_a[b].next = &a_to_b[a];
          a_to_b[a].prev = &b_to_a[b];
        }

  }
  while (nb_changes);

  return res;
}



int main(int, char*)
{
  int nb_cases;
  int nb_a_to_b;
  int nb_b_to_a;
  int turnover;
  Trip* a_to_b;
  Trip* b_to_a;

  input >> nb_cases;
  for (int c = 0; c < nb_cases; ++c)
  {
    int nb_trips = 0;

    input >> turnover;
    input >> nb_a_to_b;
    a_to_b = new Trip[nb_a_to_b];
    input >> nb_b_to_a;
    b_to_a = new Trip[nb_b_to_a];

    for (int s = 0; s < nb_a_to_b; ++s)
      a_to_b[s].Read(input, nb_trips++);
    for (int s = 0; s < nb_b_to_a; ++s)
      b_to_a[s].Read(input, nb_trips++);

    schedule result = solve_case(nb_a_to_b, nb_b_to_a, a_to_b, b_to_a, turnover);
    cout << "Case #" << (c+1) << ": " << result.from_a << " " << result.from_b << endl;

    delete[] a_to_b;
    delete[] b_to_a;
  }

  input.close();

  return 0;
}
