#include <iostream>
#include <fstream>
#include <algorithm>
#include <conio.h>
#include <vector>
#include <numeric>
#include <list>

typedef unsigned int cval;
typedef unsigned int uint;

//SORRY FOR MY ENGLISH

cval xor(int one, int two)
{
	return one^two;
}

/*
First, what math does the youngest use? He's doesn't do add, he does XOR obviously.

Let's look at the whole pile and count 1 at each binary line.

Now, we have only two options: amount of 1(true) could be odd or even. Rest doesn't matter.
Doing xor on two numbers means doing xor on each of their didgits.
*If you got yourself different result on any line (like if you got 1 and 0 in the very beggining) 
you got two different numbers.
Xor on 0 and 1 gives 1 so it's only 1 that matters.
**Odd amount of 1 gives 1 in result. 
***Even gives 0 in result.

Odd can be divided in odd and even.
Even can be divided in (even and even) or (odd and odd). 

Therefore pile with odd amount of 1 will inevitably give two different digits as a line result 
for odd and even piles will give 1 and 0 after xor'ing all digits on the line (**,***).

****Therefore pile with even amount of 1 will inevitably give two equal digits as a line result
for odd and odd pile will give 1 and 1 and even and even piles will give 0 and 0 after xoring all digits on the line (**,***).

To get a result of equal numbers, each line must have even amount of 1 (*,****).
If it does, it means that a1^a2^..^an = 0
*/
bool isPossible(cval* arr, uint size)
{
	cval weGot = 0;
	weGot = std::accumulate(arr,arr+size,0,xor);
	if(weGot == 0)
		return true;
	else
		return false;
}

cval* readCandyLine(std::ifstream& input, uint howMuch)
{
	cval* arr = new cval[1000];
	while(howMuch--)
	{
		input >> arr[howMuch];
	}
	return arr;
}

/*
No matter how you divide (a1^a2^..^an = 0), you can't get not equal numbers after xoring piles (****)
So let's give up smallest candy (CRUELTY)
*/
cval maxPile(cval* arr, uint size)
{
	cval minCandy = *std::min_element(arr,arr+size);
	cval candyTotal = std::accumulate(arr,arr+size,0);
	cval maxPile = candyTotal - minCandy;
	return maxPile;
}

int main()
{
	uint cases = 0;
	uint candyAmount = 0;
	//open input and output
	std::ifstream input("C:\\temp\\c-large-brothers.in");
	std::ofstream output("C:\\temp\\c-large-brothers.out");
	//read T
	input>>cases;
	uint i = 0;
	//go through whole file
	while(i++ != cases)
	{
		//in another case read N
		input>>candyAmount;
		//get all numbers from line
		cval* candyArr = readCandyLine(input,candyAmount);
		//is it possible?
		bool possible = isPossible(candyArr,candyAmount);
		//ok, calculate max pile
		if(possible)
		{
			output<<"Case #"<<i<<": "<<maxPile(candyArr,candyAmount)<<std::endl;
		}
		else
		{
			output<<"Case #"<<i<<": NO"<<std::endl;
		}
	}
	//so i don't have to wait anymore? Swell
	std::cout<<"Done!";
	_getch();
	return 0;
}