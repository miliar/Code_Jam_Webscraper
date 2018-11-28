#include <ios>
#include <fstream>
#include <string>
#include <queue>
#include <set>


int main(void)
{
	std::ifstream inf("A-large.in.txt");
	std::ofstream outf("out.txt");

	if (inf.bad() || outf.bad())
	{
		printf("Error: can't open the file\n");
		return -1;
	}

	std::string buffer;
	std::getline(inf, buffer);

	const int case_count = atoi(buffer.c_str());
	for (int case_index = 0 ; case_index < case_count ; ++case_index)
	{
		std::getline(inf, buffer);
		const int engin_count = atoi(buffer.c_str());

		std::set<std::string> engine_list;
		for (int index = 0 ; index < engin_count ; ++index)
		{
			std::getline(inf, buffer);
			engine_list.insert(buffer);
		}

		std::getline(inf, buffer);
		const int query_count = atoi(buffer.c_str());

		std::queue<std::string> query_list;
		for (int index = 0 ; index < query_count ; ++index)
		{
			std::getline(inf, buffer);
			if (index == 0 || (query_list.size() > 0 && query_list.back() != buffer))
				query_list.push(buffer);
		}

		int change_count = 0;
		std::set<std::string> clone(engine_list);

		const int each_count = query_list.size();
		for (int index = 0 ; index < each_count ; ++index)
		{
			std::set<std::string>::iterator itr = clone.find(query_list.front());
			if (itr != clone.end())
			{
				clone.erase(itr);

				if (clone.empty())
				{
					++change_count;
					clone = engine_list;

					itr = clone.find(query_list.front());
					clone.erase(itr);
				}
			}
			query_list.pop();
		}

		outf << "Case #" << case_index + 1 << ": " << change_count << std::endl;
	}

	outf.close();
	inf.close();

	return 0;
}