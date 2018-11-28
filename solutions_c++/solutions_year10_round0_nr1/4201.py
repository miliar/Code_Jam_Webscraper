#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>

class snapper
{
public:
	bool state;
	bool powered;
	bool light;
	snapper* next;
	
	void init_snapper()
	{
		next = new snapper();
	}
	
	snapper() : state(false), powered(false), light(false) {}
	snapper(bool s, bool p) : state(s), powered(p), light(false) {}
	snapper(bool s, bool p, bool l) : state(s), powered(p), light(l) {}
	
	~snapper()
	{
		delete next;
	}
	
	void power_up()
	{
		if (!light)
		{
			if (state && powered)
				next->powered = true;
			else
				next->powered = false;
			next->power_up();
		}
	}
	
	void snap()
	{
		if (powered && !light)
		{
			next->snap();
			state = !state;
		}
	}
	
	void print()
	{
		if (!light)
		{
			if (state)	std::cout << "O";
			else				std::cout << "X";
			if (next->powered)  std::cout << "=";
			else								std::cout << "-";
			next->print();
		}
		else
		{
			if (powered)	std::cout << "L";
			else					std::cout << "l";
			std::cout << "\n";
		}
	}
};

int cin_int()
{
	std::string str;
	std::cin >> str;
	return boost::lexical_cast<int>(str);
}

int main()
{
	int cases = cin_int();
	int numSnappers, numSnaps;
	for (unsigned int i=1; i<=cases; ++i)
	{
		numSnappers = cin_int();
		numSnaps = cin_int();
		
		snapper* current = new snapper();
		snapper* source = new snapper();
		snapper* light = new snapper(false, false, true);
		
		source->powered = true;
		current = source;
		
		for (int j=0; j<numSnappers-1; ++j)
		{
			snapper* s = new snapper();
			current->next = s;
			current = current->next;
		}
		current->next = light;
		
		for (int j=0; j<numSnaps; ++j)
		{
			source->snap();
			source->power_up();
			//source->print();
		}
		
		std::cout << "Case #" << i << ": ";
		if (light->powered)
			std::cout << "ON";
		else
			std::cout << "OFF";
		std::cout << "\n";
	}
	return 0;
}
