#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <set>
#include <utility>
using namespace std;

#ifndef EXIT_SUCCESS
#define EXIT_SUCCESS 0
#endif
#ifndef EXIT_FAILURE
#define EXIT_FAILURE 1
#endif

typedef unsigned int uint;
typedef unsigned long ulong;
typedef uint T_TYPE;
typedef uint N_TYPE;
typedef ulong R_TYPE;
typedef ulong K_TYPE;
typedef K_TYPE G_TYPE;
typedef vector<G_TYPE> G_VECTOR;
typedef K_TYPE RESULT_TYPE;
typedef set<N_TYPE> N_SET;
typedef pair<N_TYPE,RESULT_TYPE> RIDE_TYPE;
typedef vector<RIDE_TYPE> RIDE_VECTOR;

static const char defaultInput[] = "Example.in";
static const char defaultOutput[] = "Default.out";

static const string separator = " ";

template<class T>
T StringTo(const string input)
{
	istringstream buffer(input);
	T out;
	buffer >> out;
	return out;
}

bool ParseToRKN(const string input, R_TYPE& r, K_TYPE& k, N_TYPE& n)
{
	try
	{
		size_t firstPos = input.find(separator), secondPos = input.find(separator, firstPos + 1);
		string rStr = input.substr(0,firstPos), kStr = input.substr(firstPos + 1,secondPos - (firstPos + 1)), nStr = input.substr(secondPos + 1);
		r = StringTo<R_TYPE>(rStr);
		k = StringTo<K_TYPE>(kStr);
		n = StringTo<N_TYPE>(nStr);
	}
	catch(...)
	{
		return false;
	}
	return true;
}

N_TYPE AdmitRiders(const K_TYPE& maxRiders, const G_VECTOR& groups, N_TYPE& offset)
{
	//modifies offset, returns number of riders
	G_TYPE riders = 0, nextGroup;
	offset %= groups.size();
	N_TYPE initialOffset = offset;
	while(riders < maxRiders)
	{
		nextGroup = groups.at(offset);
		if(K_TYPE(riders) + K_TYPE(nextGroup) <= maxRiders)
		{
			//so we can admit them
			riders += nextGroup;
			++offset %= groups.size();//increment then modulus
			if(offset == initialOffset)
			{
				//we've admitted everyone in the queue
				break;
			}
		}
		else
		{
			break;
		}
	}//we have two of these for redundancy purposes
	return riders;
}

N_TYPE FirstOccurrenceOfOffset(const RIDE_VECTOR& storage, const N_TYPE& offset = 0)
{
	for(N_TYPE i = 0;i < (N_TYPE) storage.size();i++)
	{
		if(storage.at(i).first == offset)
		{
			return i;
		}
	}
	throw("Offset not found");
}

RESULT_TYPE IncomeFromRange(const RIDE_VECTOR& storage, const R_TYPE& first = 0, const R_TYPE& last = ~0)
{
	RESULT_TYPE result = 0;
	R_TYPE boundFirst = max(first,R_TYPE(0)), boundLast = min(last,R_TYPE(storage.size() - 1));
	for(R_TYPE i = boundFirst;i <= boundLast;i++)
	{
		result += storage.at(i).second;
	}
	return result;
}

RESULT_TYPE CalculateIncome(const R_TYPE& numRides, const G_VECTOR& groups, const K_TYPE& maxRiders)
{
	RESULT_TYPE result = 0;
	R_TYPE count = 0;
	N_TYPE offset = 0, newOffset;
	N_SET offsetLookup = N_SET();
	RIDE_TYPE offsetResult = RIDE_TYPE();
	RIDE_VECTOR offsetStorage = RIDE_VECTOR();
	RESULT_TYPE income;

	bool cycling = false;
	N_TYPE cycleStart = 0, cycleLength = 0;
	RESULT_TYPE precycleIncome = 0, cycleIncome = 0, postcycleIncome = 0;

	//general principle is that we iterate until we find a previously-seen offset
	//we then have a cycle that starts at the first occurrence of that offset
	//and continues until where we are then at; we can then extrapolate by multiplying
	//this cycle until another cycle would run us over the limit, r.
	//we then fill the remainder one at a time until we're done
	//since 1 <= N <= 1000, we are guaranteed a fairly short cycle (compared to naive simulation especially so)
	//naive complexity O(R*k), my complexity O(N)

	//so, assuming we find a cycle:
	//result = sum(store[0], ..., store[cycleStart - 1]) + maxCycles*sum(store[cycleStart], ..., store[cycleStart + cycleLength - 1])
	//													+ sum(store[cycleStart], ..., store[cycleStart + remainder]);***
	//where maxCycles = floor((numRides - cycleStart)/cycleLength) and remainder = (numRides - cycleStart) - (maxCycles*cycleLength);
	//***true in the general case cycleStart != 0, remainder != 0; omit the first or the last section respectively otherwise


	while(count < numRides)
	{
		cout << "  " << numRides << ", " << groups.size() << ", " << maxRiders;
		income = AdmitRiders(maxRiders, groups, newOffset = offset);//newOffset is passed after being set equal to the previous offset

		if(!offsetLookup.insert(offset).second)
		{
			//the offset has already occurred, so we have a cycle!
			cycleStart = FirstOccurrenceOfOffset(offsetStorage, offset);
			cycleLength = count - cycleStart;
			cycleIncome = IncomeFromRange(offsetStorage, cycleStart, cycleStart + cycleLength - 1);
			cycling = true;
			break;
		}
		offsetResult = RIDE_TYPE(offset, income);
		offsetStorage.push_back(offsetResult);
		offset = newOffset;
		count++;
	}
	if(!cycling)
	{
		result = IncomeFromRange(offsetStorage);
	}
	else
	{
		if(cycleStart > 0)
		{
			precycleIncome = IncomeFromRange(offsetStorage, 0, cycleStart - 1);
		}
		else
		{
			//we could do both branches in one, but it wouldn't play nicely with unsigned values and cycleStart == 0
			precycleIncome = 0;
		}
		R_TYPE maxCycles = (numRides - cycleStart)/cycleLength, remainder = (numRides - cycleStart) - (maxCycles*cycleLength);
							//not floored because R_TYPE is always an integer type
		if(remainder > 0)
		{
			postcycleIncome = IncomeFromRange(offsetStorage, cycleStart, cycleStart + remainder - 1);
		}
		else
		{
			//as above, but for cycleStart == remainder == 0
			postcycleIncome = 0;
		}
		result = precycleIncome + maxCycles*cycleIncome + postcycleIncome;
	}

	return result;
}

int main(int argc, char* argv[])
{
	ifstream file;
	ofstream output;
	bool inOpened = false, outOpened = false;
	//argv[0] is the executable path, argv[1] is the target input
	if(argc >= 2)
	{
		file.open(argv[1]);
		if(file)
		{
			inOpened = true;
		}
		if(argc >= 3)
		{
			output.open(argv[2]);
			if(output)
			{
				outOpened = true;
			}
		}
	}
	if(!inOpened)
	{
		file.open(defaultInput);
		if(file)
		{
			inOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}
	if(!outOpened)
	{
		output.open(defaultOutput);
		if(output)
		{
			outOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}

	string tStr, line, groupLine;
	T_TYPE T;//number of trials
	N_TYPE N;//number of groups in trial
	R_TYPE R;//number of rides in trial
	K_TYPE K;//number of seats in trial
	vector<G_TYPE> groups;//number of individuals in groups in trial
	RESULT_TYPE result;

	size_t groupLineOldOffset, groupLineNewOffset;

	getline(file,tStr);
	T = StringTo<T_TYPE>(tStr);
	
	for(T_TYPE i = 0;i < T;i++)
	{
		groups.clear();
		getline(file,line);
		if(!ParseToRKN(line, R, K, N))
		{
			return EXIT_FAILURE;
		}
		groups.reserve(N);
		getline(file,groupLine);
		groupLineOldOffset = 0;
		while(groups.size() < N)
		{
			groupLineNewOffset = groupLine.find(separator, groupLineOldOffset);
			groups.push_back(StringTo<G_TYPE>(groupLine.substr(groupLineOldOffset, groupLineNewOffset - groupLineOldOffset)));
			groupLineOldOffset = groupLineNewOffset + 1;
		}
		cout << "Starting " << i << "\n";
		result = CalculateIncome(R, groups, K);
		output << "Case #" << (i + 1) << ": " << result;
		if(i < T - 1)
		{
			//isn't the last one
			output << "\n";
		}
	}

	file.close();
	output.close();

	return EXIT_SUCCESS;
}