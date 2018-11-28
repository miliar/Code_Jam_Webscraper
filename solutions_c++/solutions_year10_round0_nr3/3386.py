#include <iostream>
#include <fstream>
using namespace std;

struct nextcounter
{
	int cur; // 0 to 1000
	int start; // 0 to 999
};

typedef long long int NUM;

struct nextcounter my;

int isdupe(NUM combo[][2], int C) // C is the index not the length of the whole array
{
	int index = C;
	C--;
	for (int i=0;i<=C;i++)
	{
		if (combo[i][1] == combo[index][1])
			return i;
	}
	return -1;
}

NUM next(int N, NUM riders[]) // returns the "next" group of riders
{
	if (my.cur == N) // start over atht ebeginning of a cycle
		my.cur = 0;
	NUM temp = riders[my.cur];
	(my.cur)++;
	return temp;
}

NUM sum_upto(NUM combo[][2], NUM R)
{
	int sum = 0;
	for (int i=0;i<R;i++)
		sum += combo[i][0];
	return sum;
}

int main()
{
	ifstream in;
//	in.open("A-small-attemp0.in");
	in.open("C-small-attempt2.in");
	ofstream out;
	out.open("C-small-attemp2.out");
	my.cur = 0;
	int N, C = -1, z;
	bool exit = 0;
	
	NUM T, R, k, G, money = 0, count = 0, temp, bigger = 0;
	in >> T;
	for (int i=0;i<T;i++)
	{
		in >> R >> k >> N;
		NUM riders[N]; // the list of the line of riders
		NUM combo[N][2]; // first field is # of people, i.e. money
						// second field is starting index, used for cycle detection
		C = -1;
		for (int j=0;j<N;j++)
		{
			in >> riders[j];
			bigger += riders[j];
		}		
		if (bigger <= k)
			money = bigger * R;
		else {
			// generate all the subsets
			my.start = 0;
			my.cur = 0;
			count = 0;
			do
			{
				C++;
				combo[C][1] = my.start;
				do
				{
					temp = next(N, riders);
					if (count + temp > k) // adding the next group exceeds the limit
					{
						combo[C][0] = count;
						exit = 1;
						count = temp;
						if (my.cur != 0) // my.cur didn't wrap around yet
							my.start = my.cur - 1;
						else //my.cur wrapped around
							my.start = N - 1;
					}	
					else
						count += temp;							
				} while(!exit);
				exit = 0;
				z = isdupe(combo, C);
			} while(z == -1); // while there isn't any duplicates, keep going
			// at this opint you have an array from 0 to C-1 inclusive of all the possibilities where isdupe(combo[][1], C) to C are looped inclusive
			if (R > z)
			{
				R = R - z;
				money = sum_upto(combo, z);
				bigger = sum_upto(combo + z, C - z);
				money += bigger * (R / (C - z)) + sum_upto(combo + z, R % (C - z));
			}
			else
				money = sum_upto(combo, R);

		} // end else
		out << "Case #" << i+1 << ": " << money << endl;
		money = 0;
		bigger = 0;

	}
	return 0;	
}
