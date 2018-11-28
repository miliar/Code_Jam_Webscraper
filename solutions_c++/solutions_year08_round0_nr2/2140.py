/**
 *	main.cpp
 *
 *	-- Train Timetable --
 *
 *	Google Codejam 2008 Qauls
 *
 *	Themistoklis Bourdenas
 *	July 2008
 */
#include <boost/foreach.hpp>
#include <boost/bind.hpp>

#include <iostream>
#include <fstream>
#include <functional>
#include <algorithm>
#include <vector>
#include <set>

#include <cassert>

namespace codejam
{
	//------------------------------
	//-- struct Time

	struct Time
	{
		Time(void)
			: hh(0), mm(0) {}
		Time(short hh, short mm)
			: hh(hh), mm(mm) {}

		bool operator <(const Time& right) const {
			if (this->hh < right.hh)
				return true;
			else if (this->hh == right.hh)
				return this->mm < right.mm;
			else
				return false;
		}

		bool operator <=(const Time& right) const {
			return *this < right || *this == right;
		}

		bool operator ==(const Time& right) const {
			return this->hh == right.hh && this->mm == right.mm;
		}

		Time operator +(const Time& right) const {
			return Time(
				(this->hh + right.hh) + (this->mm + right.mm > 60 ? 1 : 0),
				(this->mm + right.mm) % 60
			);
		}

		Time operator -(const Time& right) const {
			assert(right < *this);
			return Time(
				(this->hh - right.hh) - (this->mm < right.mm ? 1 : 0),
				(this->mm > right.mm) ? this->mm - right.mm : 60 - (right.mm - this->mm)
			);
		}

		short hh;
		short mm;
	};

	template <class Out>
	Out& operator <<(Out& out, const Time& time) {
		return out << time.hh << ":" << time.mm;
	}


	//------------------------------
	//-- class Trip

	class Trip
	{
	public:
		Trip(const Time& dep, const Time& arr, int turnaround)
			: dep(dep), arr(arr), turnAround(Time(turnaround / 60, turnaround % 60)) { assert(dep < arr); }

		const Time& Departure(void) const { return dep; }
		const Time& Arrival(void) const { return arr; }
		const Time& TurnAround(void) const { return turnAround; }

		Time Duration(void) const { return arr - dep; }
		Time Available(void) const { return arr + turnAround; }

	private:
		Time dep;
		Time arr;
		Time turnAround;
	};

	struct earlier
		: public std::binary_function<Trip, Trip, bool>
	{
		bool operator()(const Trip& left, const Trip& right) const {
			if (left.Departure() < right.Departure())
				return true;
			else if (left.Departure() == right.Departure())
				return left.Arrival() < right.Arrival();
			else return false;
		}
	};
	typedef std::multiset<Trip, earlier> TripSchedule;


	//------------------------------
	//-- struct Case

	struct Case
	{
		int turnaround;
		int tripsFromA;
		int tripsFromB;

		TripSchedule a2b;
		TripSchedule b2a;
	};

	typedef std::vector<Case> CaseVector;

	//-----------------------------------------------------------------------


	//-------------------------------------------------------//
	//---- free functions -----------------------------------//

	CaseVector ParseInput(const std::string& file)
	{
		CaseVector cases;

		std::ifstream in(file.c_str());

		if (!in.bad())
		{
			size_t ncases;
			in >> ncases;
			
			for (size_t i=0; i < ncases; ++i)
				//< parse case
			{
				Case c;
				in >> c.turnaround >> c.tripsFromA >> c.tripsFromB;

				for (int j=0; j < c.tripsFromA; ++j)
				{
					char s;
					short hh0, hh1, mm0, mm1;
					in >> hh0 >> s >>  mm0 >> hh1 >> s >> mm1;
					c.a2b.insert(Trip(Time(hh0, mm0), Time(hh1, mm1), c.turnaround));
				}

				for (int j=0; j < c.tripsFromB; ++j)
				{
					char s;
					short hh0, hh1, mm0, mm1;
					in >> hh0 >> s >>  mm0 >> hh1 >> s >> mm1;
					c.b2a.insert(Trip(Time(hh0, mm0), Time(hh1, mm1), c.turnaround));
				}
				cases.push_back(c);
			}
		}

		return cases;
	}

	//-----------------------------------------------------------------------

	void AllocateTripsA2B(Case& ctx, const Trip& trip);
	void AllocateTripsB2A(Case& ctx, const Trip& trip);

	void SolveCase(const Case& context, std::ofstream& out)
	{
		static int ncase=0;
		size_t NA=0, NB=0;

		Case ctx = context;

		while (!ctx.a2b.empty() || !ctx.b2a.empty())
		{
			if (
				(!ctx.a2b.empty() && !ctx.b2a.empty() && earlier()(*ctx.a2b.begin(), *ctx.b2a.begin()))	||
				ctx.b2a.empty())
			{
				++NA;

				Trip trip = *ctx.a2b.begin();
				ctx.a2b.erase(ctx.a2b.begin());
				AllocateTripsA2B(ctx, trip);
			}
			else if (
				(!ctx.a2b.empty() && !ctx.b2a.empty() && earlier()(*ctx.b2a.begin(), *ctx.a2b.begin()))	||
				ctx.a2b.empty())
			{
				++NB;

				Trip trip = *ctx.b2a.begin();
				ctx.b2a.erase(ctx.b2a.begin());
				AllocateTripsB2A(ctx, trip);
			}
			else
				break;
		}

		//std::cout << "Case #" << ++ncase << ": " << NA << " " << NB << std::endl;
		out << "Case #" << ++ncase << ": " << NA << " " << NB << std::endl;
	}

	void AllocateTripsA2B(Case& ctx, const Trip& trip)
	{		
		BOOST_FOREACH(const Trip& next, ctx.b2a)
		{
			if (trip.Available() <= next.Departure()) {
				Trip copy = next;
				ctx.b2a.erase(next);
				AllocateTripsB2A(ctx, copy);
				break;
			}
		}
	}

	void AllocateTripsB2A(Case& ctx, const Trip& trip)
	{
		BOOST_FOREACH(const Trip& next, ctx.a2b)
		{
			if (trip.Available() <= next.Departure()) {
				Trip copy = next;
				ctx.a2b.erase(next);
				AllocateTripsA2B(ctx, copy);
				break;
			}
		}
	}

	//-----------------------------------------------------------------------

	void Run(const std::string& file)
	{
		CaseVector cases = ParseInput(file);

		std::ofstream out("output.txt");

		BOOST_FOREACH(const Case& ctx, cases)
			SolveCase(ctx, out);
		//std::for_each(
		//	cases.begin(),
		//	cases.end(),
		//	boost::bind<void>(&SolveCase, out)
		//);

		out.close();
	}

	//-----------------------------------------------------------------------
}

//-----------------------------------------------------------------------

//-------------------------------------------------------//
//---- main ---------------------------------------------//

int main(int argc, char* argv[])
{
	//if (argc < 2)
	//	std::cout << "Please provide input file" << std::endl;

	codejam::Run("input.txt");

	return 0;
}

//-----------------------------------------------------------------------
