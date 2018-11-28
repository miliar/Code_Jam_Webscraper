#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <sstream>
#include <stdexcept>

std::string change_ext(const std::string &name, const std::string &ext) 
{
	std::string::size_type pos = name.find_last_of('.');
	if (pos != std::string::npos) {
		std::string ret = name;
		ret.replace(pos, name.length() - pos, ext);
		return ret;
	} else throw std::runtime_error("change_ext: no extencion found.");
}

class arrival {
	unsigned int mHour, mMin;
	bool mArriving;
public:
	arrival() : mHour(0), mMin(0), mArriving(0) {}
	arrival(const unsigned int h, const unsigned int m) : mHour(h), mMin(m), mArriving(0) {};
	void arrives(const unsigned int m) {
		mArriving = true;
		mMin += m;
		if (mMin > 59) {
			mMin -= 59;
			mHour++;
		}
	}
	bool operator<(const arrival &o) const {
		if (mHour < o.mHour) return true;
		else if (mHour > o.mHour) return false;
		else if (mMin < o.mMin) return true;
		else if (mMin > o.mMin) return false;
		else if (mArriving) return true;
		else return false;
	}
	bool arriving() const { return mArriving; }
	friend std::istream &operator>>(std::istream &in, arrival &t);
	friend std::ostream &operator<<(std::ostream &in, const arrival &t);
};

template <typename T> T from_str(const std::string &s)
{
	std::istringstream in(s);
	T val;
	in >> val;
	return val;
}

std::istream &operator>>(std::istream &in, arrival &t)
{
	std::string tmp;
	in >> tmp;
	t = arrival(from_str<unsigned int>(tmp.substr(0, 2)), from_str<unsigned int>(tmp.substr(3)));
	return in;
}

std::ostream &operator<<(std::ostream &out, const arrival &t) { return out << t.mHour << ":" << t.mMin; }

typedef std::multiset<arrival> time_table;

void get_stations(time_table &from, time_table &to, std::istream &in, const unsigned int count, const unsigned int turnaround)
{
	for (unsigned int j = 0; j < count; ++j) {
		arrival t;
		in >> t;
		from.insert(t);
		in >> t;
		t.arrives(turnaround);
		to.insert(t);
	}
}

unsigned int get_needed(const time_table &station)
{
	unsigned int needed = 0, available = 0;
	for (time_table::const_iterator it = station.begin(); it != station.end(); ++it) {
		if (!it->arriving()) {
			if (available) --available;
			else ++needed;
		}	else ++available;
	}
	return needed;
}

int main(int argc, char **argv)
{
	if (argc < 2) {
		std::cout << "usage: " << argv[0] << " file." << std::endl;
		return 1;
	}

	std::ifstream in(argv[1]);
	if (!in.good()) {
		std::cout << "error: unable to open file " << argv[1] << "." << std::endl;
		return 2;
	}

	std::ofstream out(change_ext(argv[1], ".out").c_str());
	if (!out.good()) {
		std::cout << "error: unable to open file for output." << std::endl;
		return 3;
	}

	unsigned int cases;
	in >> cases;
	for (unsigned int i = 0; i < cases; ++i) {
		unsigned int turnaround, na, nb, count;
		in >> turnaround >> na >> nb;

		time_table station_a, station_b;
		get_stations(station_a, station_b, in, na, turnaround);
		get_stations(station_b, station_a, in, nb, turnaround);

		na = get_needed(station_a);
		nb = get_needed(station_b);

		out << "Case #" << (i + 1) << ": " << na << " " << nb << std::endl;
	}
}
