#include <iostream>
#include <map>
#include <set>
#include <list>

struct ElementInfo
{
	std::set<char> opposed;
	std::map<char, char> combines;
};

std::list<char> run_magicks(std::list<char>& input, std::map<char, ElementInfo>& elements)
{
	std::list<char> output;
	
	char last_element = 0;
	for (auto i = input.begin(); i != input.end(); i++)
	{
		if (last_element > 0)
		{
			if (elements[last_element].combines.count(*i))
			{
				last_element = elements[last_element].combines[*i];
				output.pop_back();
				output.push_back(last_element);
				continue;
			}
		}
		
		bool cleared = false;
		
		for (auto j = output.begin(); j != output.end(); j++)
		{
			if (elements[*i].opposed.count(*j))
			{
				output.clear();
				last_element = 0;
				cleared = true;
				break;
			}
		}
		
		if (!cleared) {last_element = *i; output.push_back(*i);}
	}
	
	return output;
}

void get_magicks()
{
	int num_combines = 0;
	std::cin >> num_combines;
	
	std::map<char, ElementInfo> elements;
	
	for (num_combines; num_combines > 0; num_combines--)
	{
		char b1;
		char b2;
		char result;
		
		std::cin >> b1 >> b2 >> result;
		
		elements[b1].combines[b2] = result;
		elements[b2].combines[b1] = result;
	}
	
	int num_opposed = 0;
	std::cin >> num_opposed;
	
	for (num_opposed; num_opposed > 0; num_opposed--)
	{
		char b1;
		char b2;
		
		std::cin >> b1 >> b2;
		
		elements[b1].opposed.insert(b2);
		elements[b2].opposed.insert(b1);
	}
	
	int num_inputs = 0;
	std::cin >> num_inputs;
	
	std::list<char> inputs;
	
	for (num_inputs; num_inputs > 0; num_inputs--)
	{
		char element;
		std::cin >> element;
		inputs.push_back(element);
	}
	
	std::list<char> output = run_magicks(inputs, elements);
	
	std::cout << "[";
	for (auto i = output.begin(); i != output.end();i)
	{
		std::cout << *i;
		if (++i != output.end()) {std::cout << ", ";}
	}
	std::cout << "]";
}

int main()
{
	unsigned int num_tests = 0;
	std::cin >> num_tests;
	
	for (int i = 1; i <= num_tests; i++)
	{
		std::cout << "Case #" << i << ": ";
		get_magicks();
		std::cout << std::endl;
	}
	
	return 0;
}
