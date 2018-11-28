#include <iostream>
#include <vector>
using namespace std;


typedef unsigned int uint;

bool is_first_recycled(uint begin, uint number, uint recycled)
{
	if(recycled < number && recycled >= begin)
		return false;
	return true;
}

uint integer_div(uint n, uint divider)
{
	uint result= ((n - (n % divider))/divider);
	//cout<<"n = "<<n <<" div:"<<divider << " result:"<< result<< std::endl;;
	return result;
}

uint get_ten_power_of(uint n)
{
	if(n < 10)
		return 1;
	uint ten_power = 1;
	while((n = integer_div(n, 10)) > 0)
		ten_power *= 10;
	return ten_power;
}

uint solve(uint begin, uint end)
{
	int recycled_count = 0;
	//vector< pair<uint, uint> > recycled_pairs;
	for (int i = begin; i <= end; ++i)
	{
		uint ten_power = 10;
		std::vector<uint> recycled_numbers;
		while(integer_div(i, ten_power) > 0)
		{
			uint number = i;
			uint last_digit = number % ten_power;
			number = (number - last_digit)/ten_power;
			//*10 cause we want to to put it before number
			uint recycled_number = last_digit*get_ten_power_of(number)*10 + number;

			if(recycled_number >= begin && recycled_number <= end && 
				i != recycled_number && is_first_recycled(begin, i, recycled_number) &&
				(recycled_numbers.end() == find(recycled_numbers.begin(), recycled_numbers.end(), recycled_number)))
			{
				//cout<< i << " --> "<< recycled_number << std::endl;
				// for_each(recycled_pairs.begin(), recycled_pairs.end(), ^(pair<uint, uint> p){
				// 	if((p.first == i && p.second == recycled_number) ||
				// 		(p.first == recycled_number && p.second == i))
				// 		cout<<"error"<<i<<" -->"<<recycled_number<<std::endl;
				// });
				//recycled_pairs.push_back(make_pair<uint, uint>(i, recycled_number));
				recycled_numbers.push_back(recycled_number);
				++recycled_count;
			}
			ten_power *= 10;
		}
	}
	return recycled_count;
}

int main()
{
	freopen("C-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tcCount;
    scanf("%d", &tcCount);
    for (int i = 1; i <= tcCount; ++i)
    {
    	uint begin;
    	uint end;
    	scanf("%d %d", &begin, &end);
    	cout<<"Case #"<<i<<": "<< solve(begin, end) <<std::endl;
    }
}