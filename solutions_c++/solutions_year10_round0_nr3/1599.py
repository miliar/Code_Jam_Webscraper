#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int64;

int64 handle_case(ifstream& infile)
{
    int64 R, k, N, sum_g; 
    int64 g[1000], p[1000], n[1000], trav[1000], ride[1000];
    int64 i, x, profit, seats, nr;
    int64 start_of_cycle, initial_profit, cycle_profit;
    int64 rides_per_cycle, initial_rides;

    // Read input
    sum_g = 0;
    infile >> R >> k >> N;
    for(i=0; i<N; i++)  
    {
        infile >> g[i];
	sum_g += g[i];
    }

    if(sum_g < k)  return sum_g * R;

    // Profit and position Table
    for(i=0; i<N; i++)
    {
        x=i;
	profit = 0;
	seats = k;
	while(seats >= g[x])
	{
	    seats -= g[x];
	    profit += g[x];
	    x = (x + 1) % N;
	}
	p[i] = profit;
	n[i] = x;
	//cout << "n[" << i << "] = " << n[i] << endl;
	//cout << "p[" << i << "] = " << p[i] << endl;
    }

    // Cycle detection
    for(i=0; i<N; i++)  trav[i]=-1;
    x=0;
    profit = 0;
    nr = 0;
    while(trav[x]==-1)
    {
        trav[x]=profit;
	ride[x]=nr;
        profit += p[x];
        x = n[x];
	nr++;
    }
    start_of_cycle = x;
    initial_profit = trav[x];
    initial_rides = ride[x];
    cycle_profit = profit - initial_profit;
    rides_per_cycle = nr - initial_rides;
    //cout << "start_of_cycle=" << start_of_cycle << endl;
    //cout << "initial_profit=" << initial_profit << endl;
    //cout << "initial_rides=" << initial_rides << endl;
    //cout << "cycle_profit=" << cycle_profit << endl;
    //cout << "rides_per_cycle=" << rides_per_cycle << endl;

    //Calculate Profit
    if(R < initial_rides)
    {
        profit = 0;
        nr = R;
	x=0;
    }
    else
    {
        profit = initial_profit;
        nr = R - initial_rides;
	//cout << "earn inital profit: $" << initial_profit << " (" << initial_rides << " rides)" << endl;
	i = nr / rides_per_cycle;
	//cout << i << " cycles at $" << cycle_profit << " and " << rides_per_cycle << " rides per cycle." << endl;
	profit += cycle_profit * i;
	nr -= rides_per_cycle * i;
	x = start_of_cycle;
    }

    // full rides
    while(nr > 0)
    {
        profit += p[x];
        nr--;
	//cout << "ride with profit $" << p[x] << endl;
        x = n[x];
    }

    return profit;
}

int main(int argc, char* argv[])
{
    int Ncases;
    int64 result;
    if(argc < 2)
    {
        cout << "Usage: ./code <infile>" << endl;
        exit(1);
    }

    ifstream infile(argv[1]);
    if(infile.is_open())
    {
        infile >> Ncases;
	for(int i=0; i<Ncases; i++)
	{
            result = handle_case(infile);
	    cout << "Case #" << (i+1) << ": " << result << endl;
	}
    }
    else
    {
        cout << "error opening" << argv[1] << endl;
	return 1;
    }
    return 0;
}

