#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <functional>
#include <cmath>

using namespace std;

struct Coordinate
{
	int x;
	int y;
};

class ComparePosition
{
public:
	bool operator()(const Coordinate & l, const Coordinate & r) const
	{
		return l.x < r.x || (l.x == r.x && l.y < r.y);
	}
};

class CompareDirection
{
public:
	bool operator()(const Coordinate & l, const Coordinate & r) const
	{
		if (l.x == 0 && l.y == 0)
		{
			if (r.x != 0 || r.y != 0)
				return true;
			else
				return false;
		}

		if (r.x == 0 && r.y == 0)
		{
			if (l.x != 0 || l.y != 0)
				return false;
			else
				return true;
		}

		if (l.y < 0 && r.y > 0)
			return true;

		if (l.y > 0 && r.y < 0)
			return false;

		double cos1 = l.x / sqrt(1.0 * ((l.x * l.x) + (l.y * l.y)));
		double cos2 = r.x / sqrt(1.0 * ((r.x * r.x) + (r.y * r.y)));
		return  cos1 - cos2 < -0.0000001;
	}
};

int CalculateRange(const Coordinate & l, const Coordinate & r)
{
	return ceil(sqrt(1.0 * (l.x - r.x) * (l.x - r.x) + (l.y - r.y) * (l.y - r.y)));
}


struct Distance
{
	int up;
	int down;
	int left;
	int right;
};


class CaseInfo
{
public:
	Coordinate room;
	int range;
	Coordinate me;
	int how_many;

	friend istream & operator>>(istream & is, CaseInfo & info)
	{
		string line;
		getline(is, line);
		stringstream(line) >> info.room.y >> info.room.x >> info.range;

		for (int i=0; i<info.room.y; i++)
		{
			getline(is, line);
			int p = line.find('X');
			if (p != string::npos)
			{
				info.me.x = p;
				info.me.y = i;
			}
		}

		return is;
	}

	friend ostream & operator<<(ostream & os, const CaseInfo & info)
	{
		return os << info.how_many;
	}

	void ProcessCase()
	{
		map<Coordinate, Distance, ComparePosition> openned_images;
		set<Coordinate, ComparePosition> closed_image_positions;
		set<Coordinate, CompareDirection> closed_image_directions;

		Coordinate origin_position;
		origin_position.x = 0;
		origin_position.y = 0;
		Distance origin_distance;
		origin_distance.up = 2 * me.y - 1;
		origin_distance.down = 2 * (room.y - me.y) - 3;
		origin_distance.left = 2 * me.x - 1;
		origin_distance.right = 2 * (room.x - me.x) - 3;

		openned_images[origin_position] = origin_distance;

		do
		{
			const Coordinate current_position = openned_images.begin()->first;
			const Distance current_distance = openned_images.begin()->second;
			Coordinate current_direction;
			openned_images.erase(openned_images.begin());

			current_direction.x = current_position.x - origin_position.x;
			current_direction.y = current_position.y - origin_position.y;
			closed_image_positions.insert(current_position);
			closed_image_directions.insert(current_direction);

			Coordinate new_position;
			Distance new_distance;

			new_distance = current_distance;
			new_distance.up = current_distance.down;
			new_distance.down = current_distance.up;

			new_position.x = current_position.x;
			new_position.y = current_position.y + current_distance.up;
			if (CalculateRange(new_position, origin_position) <= range
				&& closed_image_positions.find(new_position) == closed_image_positions.end())
				openned_images[new_position] = new_distance;

			new_position.x = current_position.x;
			new_position.y = current_position.y - current_distance.down;
			if (CalculateRange(new_position, origin_position) <= range
				&& closed_image_positions.find(new_position) == closed_image_positions.end())
				openned_images[new_position] = new_distance;

			new_distance = current_distance;
			new_distance.left = current_distance.right;
			new_distance.right = current_distance.left;

			new_position.x = current_position.x - current_distance.left;
			new_position.y = current_position.y;
			if (CalculateRange(new_position, origin_position) <= range
				&& closed_image_positions.find(new_position) == closed_image_positions.end())
				openned_images[new_position] = new_distance;

			new_position.x = current_position.x + current_distance.right;
			new_position.y = current_position.y;
			if (CalculateRange(new_position, origin_position) <= range
				&& closed_image_positions.find(new_position) == closed_image_positions.end())
				openned_images[new_position] = new_distance;
		} while (!openned_images.empty());

		how_many = closed_image_directions.size() - 1;
	}
};


int main()
{
	ifstream ifs("D-small-attempt0.in");
	ofstream ofs("D-small-attempt0.out");

	string line;
	getline(ifs, line);

	int number = 1;
	CaseInfo case_info;
	while (ifs >> case_info)
	{
		case_info.ProcessCase();

		ofs << "Case #" << number++ << ": " << case_info << "\n";
	}

	return 0;
}
