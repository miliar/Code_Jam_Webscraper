#include <iostream>
#include <vector>
#include <sstream>

void Work(unsigned i);

int main()
{
	unsigned cases;
	std::cin >> cases;
	for (unsigned i = 1; i<= cases; i++)
	{
		Work(i);
	}
	return 0;
}

unsigned OUT_OF_RANGE = -1;
struct Animal : public std::vector<std::string>
{
	std::string name;

	unsigned find(std::string& Keyword)
	{
		//std::cerr << "Finding:" << Keyword << " size(" << size() << ")" << std::endl;
		for (int i = 0; i < size(); i++)
		{
			if (operator[](i)==Keyword)
			{
				//std::cerr << "Found" << std::endl;
				return i;
			}
		}
		//std::cerr << "Not Found" << std::endl;
		return OUT_OF_RANGE;
	}
};

void GetTreeString(std::string& Output);
void GetAnimals(std::vector<Animal>& Output);
double HandleTree(std::string& Data, Animal& myAnimal);
double HandleNode(std::istringstream& iss, Animal& myAnimal);

void Work(unsigned i)
{
	std::string RawTree;
	std::vector<Animal> Animals;

	GetTreeString(RawTree);
	GetAnimals(Animals);

	std::cout << "Case #" << i << ":" << std::endl;

	for (int i = 0; i < Animals.size(); i++)
	{
		//std::cerr << "Handling animal " << i << ": " << Animals[i].name << std::endl;
		double prob = HandleTree(RawTree, Animals[i]);
		std::cout << std::fixed << prob << std::endl;
	}

//	std::cout << RawTree << std::endl;

}

void GetTreeString(std::string& Output)
{
	Output.clear();
	unsigned lines;
	std::cin >> lines;
	std::cin.ignore(); // New Line
	for (unsigned i = 0; i < lines; i++)
	{
		std::string Line;
		std::getline(std::cin, Line);
		Output += Line;
	}
}

void GetAnimals(std::vector<Animal>& Output)
{
	Output.clear();

	unsigned n_Animals;
	std::cin >> n_Animals;
	std::cin.ignore(); // New Line
	for (unsigned i = 0; i < n_Animals; i++)
	{ 
		Animal myAnimal;
		std::string buf;
		std::getline(std::cin, buf);
		std::istringstream iss(buf);

		iss >> myAnimal.name;

		unsigned n_Chartics;
		iss >> n_Chartics;
		for (unsigned j = 0; j < n_Chartics; j++)
		{
			iss >> buf;
			myAnimal.push_back(buf);
		}
		Output.push_back(myAnimal);
	}
}

double HandleTree(std::string& Data, Animal& myAnimal)
{
	std::istringstream iss(Data);
	return HandleNode(iss, myAnimal);
}


void igsp(std::istringstream& iss) // IgnoreSpace
{
	while (iss.peek() == ' ')
	{
		iss.ignore();
	}
}

void IgnoreNode(std::istringstream& iss)
{
	//std::cerr << "IgnoreNode()" << std::endl;
	igsp(iss);
	unsigned par = 0;
	while (true)
	{
		char buf;
		iss >> buf;
		if (buf == '(')
			par++;
		else if (buf == ')')
			par--;
		if (par == 0)
			break;
	}
	//std::cerr << "IgnoreNode()ed" << std::endl;
}

double HandleNode(std::istringstream& iss, Animal& myAnimal)
{
	//std::cerr << "HandleNode()" << std::endl;
	double prob = 1;
	igsp(iss);
	iss.ignore(); // (

	igsp(iss);

	double weight;
	std::string chartics;
	iss >> weight;
	//std::cerr << "weight:" << weight << std::endl;
	prob *= weight;
	igsp(iss);
	if (iss.peek() != '(' && iss.peek() != ')')
		iss >> chartics;
	else if (iss.peek() == ')')
	{
		iss.ignore(); // )
		return prob;
	} else {
		throw( "ERROR AT 160" );
	}
	if (myAnimal.find(chartics) == OUT_OF_RANGE)
		IgnoreNode(iss);

	prob *= HandleNode(iss, myAnimal);

	iss.ignore(); // )
	return prob;
}
