#include <fstream>
#include <map>
#include <vector>
#include <set>

class CyclicBufferHelper 
{
public:
	CyclicBufferHelper(const std::vector<int>& buf, int base) 
		: m_buf(buf)
		, m_base(buf.begin()+base)
		, m_count(0)
		, m_init_index(base)
	{}

	int get_value() const 
	{
		if (m_base == m_buf.end()) 
			m_base = m_buf.begin();

		int ret = *m_base;

		++m_base;
		++m_count;

		return ret;
	}

	int get_index() const 
	{
		return m_base - m_buf.begin() - 1;
	}

	int get_init_index() const { return m_init_index; }

	bool is_end() const { return m_count >= m_buf.size(); }

private:
	const std::vector<int>& m_buf;
	mutable std::vector<int>::const_iterator m_base;
	mutable int m_count;
	const int m_init_index;
};

class Value
{
public:
	Value(int index = 0, int cost = 0) : index(index), cost(cost) {}

	int index;
	int cost;
};

int main(int argc, char* argv[])
{
	std::ifstream input_file("in.txt");
	std::ofstream output_file("out.txt");

	int count_tests = 0;
	input_file >> count_tests;

	int max_hold = 0;
	int count_rides = 0;
	int count_groups = 0;

	std::vector<int> groups;
	groups.reserve(1000);

	for (int i = 0; i < count_tests; ++i)
	{
		input_file >> count_rides >> max_hold >> count_groups;

		for (int j = 0; j < count_groups; ++j)
		{
			int val = 0;
			input_file >> val;
			groups.push_back(val);
		}
		//////////////////////////////////////////////////////////////////////////

		std::vector<Value> values;
		std::set<int> set;
		int index = 0;

		while (true)
		{
			CyclicBufferHelper cyclic(groups, index);

			int count_people = 0;
			while (!cyclic.is_end())
			{
				int new_value = cyclic.get_value();

				if (count_people + new_value <= max_hold)
					count_people += new_value;
				else
					break;
			}

			values.push_back(Value(cyclic.get_init_index(), count_people));

			index = cyclic.get_index();

			if (set.find(index) == set.end() && index != cyclic.get_init_index())
				set.insert(cyclic.get_init_index());
			else
				break;
		}

		std::vector<Value> first_part;
		std::vector<Value> last_part;
		for (std::vector<Value>::iterator it = values.begin(), end = values.end(); it != end; ++it)
		{
			if (it->index == index)
			{
				first_part.assign(values.begin(), it);
				last_part.assign(it, values.end());

				break;
			}
		}

		int total_sum = 0;

		for (std::vector<Value>::iterator it = first_part.begin(), end = first_part.end(); it != end && count_rides > 0; ++it, --count_rides)
			total_sum += it->cost;

		if (count_rides > 0)
		{
			int temp_sum = 0;
			for (std::vector<Value>::iterator it = last_part.begin(), end = last_part.end(); it != end; ++it)
				temp_sum += it->cost;

			total_sum += (count_rides/last_part.size()*temp_sum);
			int cnt = count_rides%last_part.size();
			for (int j = 0; j < cnt; ++j)
				total_sum += last_part[j].cost;
		}

		//////////////////////////////////////////////////////////////////////////
		output_file << "Case #" << i+1 << ": ";

		output_file << total_sum << std::endl;

		groups.clear();
	}

	input_file.close();
	output_file.close();

	return 0;
}
