#include <iostream>
#include <queue>

using namespace std;

struct googler
{
	int average;
	int remainder;

	googler(int Average,
		int Remainder)
		{
			this->average = Average;
			this->remainder = Remainder;
		}

	bool operator<(const googler &other) const
	{	return (this->average > other.average);    }
};

int main()
{
	int T, N, S, p;
	int make_it;
	int temp;
	googler token_dancer(0,0);
	priority_queue<googler> dancers;	

	//Get the number of test cases
	cin >> T;

	//For each test case
	for(int w = 0; w<T; ++w)
	{
		//Reset the number of Googlers who cut it
		make_it = 0;

		//Get the number of Googlers, surprising triplets, and best result
		cin >> N >> S >> p;
		
		//Get the total results
		for(int i = 0; i<N; ++i)
		{
			cin >> temp;
			dancers.push(googler(temp/3, temp%3));
		}

		//For each Googler whose average already cuts it, we don't bother
		while(!dancers.empty())
		{
			if(((googler)dancers.top()).average >= p)
			{
				dancers.pop();
				++make_it;
			}
			//Stop the loop when we find one whose average doesn't make it by itself anymore
			else
				break;
		}

		//For each Googler who needs a push
		while(!dancers.empty())
		{
			token_dancer = dancers.top();
			dancers.pop();

			//We have three possible remainders of the division by 3
			switch(token_dancer.remainder)
			{
			case 0:
				//If we have Ss left to give, and they're worth giving
				if(S > 0 && (token_dancer.average+1) >= p && token_dancer.average != 0 && token_dancer.average != 10)
				{
					//We add 1 to the result (we are actually lowering one of the judges' scores by 1 and increasing another by 1)
					++token_dancer.average;

					//And we take away one of the Ss
					--S;
				}
				break;

			case 1:
				//Check if the remainder is enough for him to make it
				++token_dancer.average;

				//If it has a remainder of 1, it can't be surprising

				//If it's not, and we hace Ss to give, and it will make a difference, give it
/*				else if((token_dancer.average > p) && (S > 0) && ((token_dancer.average+1)==p))
				{
					//We give it its remainder + the possibility of one being 2 apart from the others
					++token_dancer.average;

					//And take away one of the Ss
					--S;
					}*/
				break;

			case 2:
				//Check if the remainder is enough for him to make it
				++token_dancer.average;

				//If it's not, and we hace Ss to give, give it
				if((token_dancer.average < p) && (S > 0) && ((token_dancer.average+1)==p))
				{
					//We give it its remainder + the possibility of one being 2 apart from the others
					++token_dancer.average;

					//And take away one of the Ss
					--S;
				}
				break;

			default:
				break;
			}

			//If we've made the dancer have over 10 points, make him have 10
			if(token_dancer.average > 10)
				token_dancer.average = 10;

			//If he makes it now, add it
			if(token_dancer.average >= p)
			        ++make_it;
		}

		//Print the answer
		cout << "Case #" << w+1 << ": " << make_it << endl;
	}

}
