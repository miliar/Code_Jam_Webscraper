#include <fstream>
#include <algorithm>
#include <iterator>
using namespace std;

int gcd2(unsigned x, unsigned y)
{
	while (x!=y) {
		if (x>y) {
			x-=y;
		}
		else {
			y-=x;
		}
	}
	return x;
}

int gcd(unsigned a[],unsigned n)
{
	int b[1000] = {0};
	if (n==1) 
	{
		return a[0];
	}
	if (n >= 2) 
	{
		b[0] = gcd2(a[0],a[1]);
		for (int i = 1; i < n - 1; i++) 
		{
			b[i] = gcd2(b[i-1],a[i]);
		}
		return b[n-2];
	}
	return 0;
}

int main()
{
	unsigned iLine = 0;
	unsigned iGreatEvent = 0;
	unsigned iEventTime[3];
	unsigned iEventTimeUnique[3];
	unsigned T,y;
	ifstream filein("B.in");
	ofstream fileout("B.out");
	if (filein) 
	{
		filein >> iLine;
		for (int i = 0; i < iLine; i++) 
		{
			filein >> iGreatEvent;
			for (int j = 0; j < iGreatEvent; j++) 
			{
				filein >> iEventTime[j];
			}
			sort(iEventTime,iEventTime + iGreatEvent);
			iGreatEvent = unique_copy(iEventTime,iEventTime + iGreatEvent,iEventTimeUnique) - iEventTimeUnique;
			for (int j = 0; j < iGreatEvent-1; j++) 
			{
				iEventTimeUnique[j] = iEventTimeUnique[j+1]-iEventTimeUnique[j];
			}
			T = gcd(iEventTimeUnique,iGreatEvent-1);
			y = (T - iEventTime[0]%T)%T;
			fileout << "Case #" << (i+1) << ": " << y << endl;
		}
	}
	return 0;
}
