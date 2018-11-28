//Google Code Jam Solution Candies Class (candies.h)

#include <vector>

class Candies {
	private:
		std::vector<unsigned> candyValues;
		std::vector<bool> combination;

	public:
		Candies(const std::vector<unsigned> &c)
			: candyValues(c), combination(candyValues.size(), true) {}

		unsigned share();
		bool nextCombination(unsigned index = 0u);
};

