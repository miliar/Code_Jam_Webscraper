#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

typedef vector<int> IntVec;
typedef unsigned long long ull;


// find index of last element of "vec" which is <= "val".
// "vec" is supposed to be sorted.
// if all elements of "vec" are > "val", return -1
template<class T> int VecLastNotBiggerThan(const std::vector<T>& vec, T val)
{
    int len = vec.size();
    if (len == 0 || val < vec[0])    // first member > val => return -1
        return -1;
    if (!(val < vec[len-1]))        // last member <= val => return size-1
        return len-1;

    // now vec[0] <= val, vec[len-1] > val

    int i1 = 0, i2 = len-1;

    // now and later, vec[i1] <= val, vec[i2] > val

    while (i2-i1 > 1)
    {
        int iMid = (i1+i2)/2;
        if (val < vec[iMid])
            i2 = iMid;
        else
            i1 = iMid;
    }

    return i1;
}


int NextIndex(const vector<ull>& vCumSum, ull sum, int capacity, int i) {
    int len = vCumSum.size();
    ull cur = i == 0 ? 0 : vCumSum[i-1];
    ull target = cur + capacity;
    int lastIndex;
    if (sum >= target) {
	lastIndex = VecLastNotBiggerThan(vCumSum, target);
	assert(lastIndex >= i - 1);
    } else {
	lastIndex = VecLastNotBiggerThan(vCumSum, target - sum);
	assert(lastIndex < i);
	lastIndex += len;
    }
    return lastIndex + 1;
}


ull Profit(const IntVec& v, int nRuns, ull capacity) {
    int len = v.size();
    vector<ull> vCumSum(len);
    ull sum = 0;
    forall (i, len) {
	sum += v[i];
	vCumSum[i] = sum;
    }
    if (sum <= capacity)
	return sum * (ull)nRuns;

    int ind = 0;
    int cRounds = 0;
    IntVec vHistRuns(len, -1);
    IntVec vHistRounds(len, -1);
    int cRuns = 0;
    while (cRuns < nRuns) {
	vHistRuns[ind] = cRuns;
	vHistRounds[ind] = cRounds;

	ind = NextIndex(vCumSum, sum, capacity, ind);
	assert(ind >= 0);
	if (ind >= len) {
	    ind -= len;
	    cRounds++;
	}
	assert(0 <= ind && ind < len);
	cRuns++;

	int oldRuns = vHistRuns[ind];
	if (oldRuns >= 0) {
	    assert(cRuns > oldRuns);
	    int runs = cRuns - oldRuns;
	    int rounds = cRounds - vHistRounds[ind];
	    int runsLeft = nRuns - cRuns;
	    int nCycles = runsLeft / runs;
	    cRuns += nCycles * runs;
	    cRounds += nCycles * rounds;
	}
    }
    ull profit = sum * cRounds;
    if (ind > 0)
	profit += vCumSum[ind-1];
    return profit;
}


int main() {
    int nTests;
    cin >> nTests;
    for (int iTest=1; iTest<=nTests; iTest++) {
	// read R k N
	int nRuns, capacity, len;
	cin >> nRuns >> capacity >> len;

	// read vec
	IntVec v(len);
	forall (i, len)
	    cin >> v[i];

	printf("Case #%d: %llu\n", iTest, Profit(v, nRuns, capacity));
    }
}
