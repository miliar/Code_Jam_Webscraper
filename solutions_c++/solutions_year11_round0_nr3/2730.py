#include <iostream>
#include <list>


using namespace std;


void pick(const list<int>& pile1, const list<int>& pile2, int last, int& best);
int checkVal(const list<int>& pile1, const list<int>& pile2);


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Obtain the number of pieces of candy for the current test case
		int N;
		cin >> N;
		
		// Obtain the value of each piece of candy and
		// sort the value list in descending order
		list<int> candies;
		candies.resize(N);
		list<int>::iterator it = candies.begin();
		for (int j = 0; j < N; j++) {
			int C;
			cin >> C;
			*it = C;
			it++;
		}
		candies.sort();
		candies.reverse();
		
		// Use recursive candy picking functions to determine best distribution
		int best = 0;
		list<int> candiesSean;
		pick(candies, candiesSean, 0, best);
		
		// Provide the best case result or indicate
		// if desired candy allocation is impossible
		cout << "Case #" << i + 1 << ": ";
		if (best > 0)
			cout << best << endl;
		else
			cout << "NO" << endl;
		
	}
	
	return 0;
}

void pick(const list<int>& pile1, const list<int>& pile2, int last, int& best)
{
	int n = pile1.size();
	if (n < 1)
		return;
	for (int i = last; i < n; i++) {
		
		// Position the iterator to the next candidate value for picking
		list<int> newPile1 = pile1;
		list<int>::iterator i1 = newPile1.begin();
		for (int j = 0; j < i; j++)
			i1++;
		
		// Abort if highest possible sum (achieved by picking all remaining
		// candidate candies) can't best the current best value
		int hps = 0;
		list<int>::const_iterator i2 = pile2.begin();
		list<int>::const_iterator s2 = pile2.end();
		while (i2 != s2) {
			hps += *i2;
			i2++;
		}
		list<int>::iterator i3 = i1;
		list<int>::iterator s3 = newPile1.end();
		while (i3 != s3) {
			hps += *i3;
			i3++;
		}
		if (hps <= best)
			return;
		
		// Transfer the picked candy from the first pile to the second pile
		list<int> newPile2 = pile2;
		newPile2.push_back(*i1);
		newPile1.erase(i1);
		
		// Continue to the next pick
		pick(newPile1, newPile2, i, best);
	}
	
	// Check the values for the candy piles and
	// update the best value if applicable
	n = pile2.size();
	if (n > 0) {
		int value = checkVal(pile1, pile2);
		if (value > best)
			best = value;
	}
}

int checkVal(const list<int>& pile1, const list<int>& pile2)
{
	// Perform an XOR summation on the first pile
	int xor1 = 0;
	list<int>::const_iterator it   = pile1.begin();
	list<int>::const_iterator stop = pile1.end();
	while (it != stop) {
		xor1 ^= *it;
		it++;
	}

	// Perform an XOR summation and a simple summation on the second pile
	int xor2 = 0;
	int sum2 = 0;
	it   = pile2.begin();
	stop = pile2.end();
	while (it != stop) {
		xor2 ^= *it;
		sum2 += *it;
		it++;
	}

	// Provide the second pile simple summation value
	// if the 2 XOR summation values are equal
	if (xor1 == xor2)
		return sum2;
	else
		return 0;
}
