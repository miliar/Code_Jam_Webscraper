#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

void func(int casen);

int main()
{
	int cases;
	cin >> cases;

	for(int i=0;i<cases;i++)
	  func(i+1);	
}

void func(int casen)
{
	int n, i, rk;
	long long k, mm;

	cin >> n >> k;

	mm = 1;
	for(i=0;i<n;i++)
		mm *= 2;

	rk = k%mm;

	bool on=true;
	for(i=0, mm=1;i<n && on;i++, mm*=2, rk/=2)
		on = on && (rk%2>0);

	cout << "Case #" << casen << ": " << (on ? "ON" : "OFF") << endl;

}