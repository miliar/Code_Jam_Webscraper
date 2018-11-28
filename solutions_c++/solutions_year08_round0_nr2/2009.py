



#include <iostream>
#include <fstream>

#include <set>

using namespace std;

struct train_departure_t
{
	unsigned int departure_hours;
	unsigned int departure_minuts;

	train_departure_t(){}
	train_departure_t(
		const unsigned int _departure_hours,
		const unsigned int _departure_minuts
		    ) : 
		departure_hours(_departure_hours),
		departure_minuts(_departure_minuts) {}
};

struct train_trip_t
{
	train_departure_t departure;
	unsigned int arrival_hours;
	unsigned int arrival_minuts;

	train_trip_t(){}

	train_trip_t(
		const train_departure_t& _departure,
		const unsigned int _arrival_hours,
		const unsigned int _arrival_minuts
		    ) : 
		departure(_departure),
		arrival_hours(_arrival_hours),
		arrival_minuts(_arrival_minuts) {}
};

bool train_departure_compare_function (train_departure_t lhs, train_departure_t rhs)
{
	if (lhs.departure_hours < rhs.departure_hours)
	{
		return true;
	}
	else
	{
		return lhs.departure_minuts < rhs.departure_minuts;
	}
}

/*
inline bool operator < (const train_trip_t& lhs, const train_trip_t& rhs)
{
	if (lhs.departure_hours < rhs.departure_hours)
	{
		return true;
	}
	else
	{
		return lhs.departure_minuts < rhs.departure_minuts;
	}
}
*/

namespace std
{

bool inline operator < (const train_departure_t& lhs, const train_departure_t& rhs)
{
	if (lhs.departure_hours == rhs.departure_hours)
	{
		return lhs.departure_minuts < rhs.departure_minuts;
	}
	else
	{
		return lhs.departure_hours < rhs.departure_hours;
	}
}


inline bool operator < (const train_trip_t& lhs, const train_trip_t& rhs)
{
	return lhs.departure < rhs.departure;
}

inline train_departure_t operator + (const train_departure_t& lhs, const unsigned int rhs)
{
	train_departure_t new_departure = lhs;

	if (lhs.departure_minuts + rhs < 60)
	{
		new_departure.departure_minuts += rhs;
		return new_departure;
	}
	else
	{
		new_departure.departure_hours += (lhs.departure_minuts + rhs)/60;
		new_departure.departure_minuts = (lhs.departure_minuts + rhs)%60;
		return new_departure;
	}
}

}

int main(int argc, char *argv[])
{
	unsigned int N, T, NA, NB;
	
	std::ifstream ifstr("B-large.in");
	std::ofstream ofstr("B-large.out", std::ios::out | std::ios::trunc);

	ifstr >> N;

	std::string line;
	std::getline(ifstr, line); // sorry for this

	std::cout << "\nN: " << N; 

	for (
	     unsigned int i = 0;
	     i < N;
	     ++i
	    )
	{
 		std::multiset<train_trip_t> a_to_b_trips, b_to_a_trips;
 		std::multiset<train_departure_t> a_trains_pool, b_trains_pool;

		ifstr >> T;
		std::getline(ifstr, line);

		ifstr >> NA >> NB;
		std::getline(ifstr, line);

		// read trips from A to B
		for (
		     unsigned int j = 0;
		     j < NA;
		     ++j
		    )
		{
			std::getline(ifstr, line);
			train_departure_t train_departure(
					(unsigned int)atoi(line.substr(0,2).c_str()),
					(unsigned int)atoi(line.substr(3,2).c_str())
							 );

			train_trip_t train_trip(
					 train_departure,
					(unsigned int)atoi(line.substr(6,2).c_str()),
					(unsigned int)atoi(line.substr(9,2).c_str())
					       );

			a_to_b_trips.insert(train_trip);
		}

		// read trips from B to A
		for (
		     unsigned int j = 0;
		     j < NB;
		     ++j
		    )
		{
			std::getline(ifstr, line);
			train_departure_t train_departure(
					(unsigned int)atoi(line.substr(0,2).c_str()),
					(unsigned int)atoi(line.substr(3,2).c_str())
							 );

			train_trip_t train_trip(
					 train_departure,
					(unsigned int)atoi(line.substr(6,2).c_str()),
					(unsigned int)atoi(line.substr(9,2).c_str())
					       );

			b_to_a_trips.insert(train_trip);
		}

		unsigned int trains_from_a_count = 0, trains_from_b_count = 0;

		while (!a_to_b_trips.empty() || !b_to_a_trips.empty())
		{
			bool have_trip_from_a = !a_to_b_trips.empty();
			bool have_trip_from_b = !b_to_a_trips.empty();

			train_trip_t nearest_trip_from_a, nearest_trip_from_b;
			if (have_trip_from_a)
			{
				nearest_trip_from_a = *a_to_b_trips.begin();
			}
			if (have_trip_from_b)
			{
				nearest_trip_from_b = *b_to_a_trips.begin();
			}

			
			if (have_trip_from_a && have_trip_from_b)
			{
				if (nearest_trip_from_a.departure < nearest_trip_from_b.departure)
				{
					// departure train from a

					train_departure_t new_departure(nearest_trip_from_a.arrival_hours,
									nearest_trip_from_a.arrival_minuts);
					new_departure = new_departure + T;
					b_trains_pool.insert(new_departure);

					a_to_b_trips.erase(a_to_b_trips.begin());					

					if (a_trains_pool.empty() || nearest_trip_from_a.departure < *(a_trains_pool.begin()) )
					{
						++trains_from_a_count;
					}
					else
					{
						a_trains_pool.erase(a_trains_pool.begin());	
					}

					continue;
				}
				else
				{
					// departure train from b

					train_departure_t new_departure(nearest_trip_from_b.arrival_hours,
									nearest_trip_from_b.arrival_minuts);
					new_departure = new_departure + T;

					a_trains_pool.insert(new_departure);

					b_to_a_trips.erase(b_to_a_trips.begin());					

					if (b_trains_pool.empty() || nearest_trip_from_b.departure < *(b_trains_pool.begin()) )
					{
						++trains_from_b_count;
					}
					else
					{
						b_trains_pool.erase(b_trains_pool.begin());	
					}

					continue;
				}
			}
			

			if (have_trip_from_a && !have_trip_from_b)
			{
				// departure train from a

				train_departure_t new_departure(nearest_trip_from_a.arrival_hours,
								nearest_trip_from_a.arrival_minuts);
				new_departure = new_departure + T;
				b_trains_pool.insert(new_departure);

				a_to_b_trips.erase(a_to_b_trips.begin());					

				if (a_trains_pool.empty() || nearest_trip_from_a.departure < *(a_trains_pool.begin()) )
				{
					++trains_from_a_count;
				}
				else
				{
					a_trains_pool.erase(a_trains_pool.begin());	
				}

				continue;
			}

			if (have_trip_from_b && !have_trip_from_a)
			{
				// departure train from b

				train_departure_t new_departure(nearest_trip_from_b.arrival_hours,
									nearest_trip_from_b.arrival_minuts);
				new_departure = new_departure + T;
				a_trains_pool.insert(new_departure);

				b_to_a_trips.erase(b_to_a_trips.begin());					

				if (b_trains_pool.empty() || nearest_trip_from_b.departure < *(b_trains_pool.begin()) )
				{
					++trains_from_b_count;
				}
				else
				{
					b_trains_pool.erase(b_trains_pool.begin());	
				}

				continue;
			}
		}

		ofstr << "Case #" << i+1 << ": " << trains_from_a_count << " " << trains_from_b_count << std::endl;
	}

	ifstr.close();
	ofstr.close();

	return 0;
}
