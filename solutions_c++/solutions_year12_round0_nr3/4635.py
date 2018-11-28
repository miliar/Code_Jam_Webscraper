#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

static set<int> all_num;

int getMultiplier(int v)
{
   int i = 1;
   int tv = v / 10;
   while (tv > 0) {
	   i = i * 10;
	   tv =  tv /10;
   }
   return i;
}

int countAll(int v, int lo, int hi)
{
  set<int> curs;
  int tv = v;
  int mul = getMultiplier(v);
  curs.insert(tv);
  all_num.insert(tv);
  int count = 1;
  while (1)
  {
	  int firstDigit = tv % 10;
	  tv = (tv/10) + (firstDigit * mul);
	  set<int>::iterator it;
	  it = curs.find(tv);
	  if (it != curs.end())
		  break;
	  curs.insert(tv);
	  all_num.insert(tv);
	  if (tv >= lo && tv <=hi)
		  count ++;
  }
  int total = 0;
  if (count > 1)
	  total = (count) * (count-1) / 2;
  return total;
}

int main()
{
    ifstream infile("C-small-attempt1.in");
	ofstream outfile("result.txt");
	string str;
	getline(infile, str);
    istringstream buffer(str);
    int testCase = 0;
    buffer >> testCase;

    for (int k=0; k < testCase; k++)
	{
		getline(infile, str);
		istringstream buffer1(str);
		int lo = 0;
		int hi = 0;
		buffer1 >> lo >> hi;
		int total = 0;
		for (int i=lo; i <= hi; i++)
		{
			set<int>::iterator it;
			it = all_num.find(i);
			if (it == all_num.end())
            total += countAll(i, lo, hi);
		}
		all_num.clear();
		outfile << "Case #" <<  k+1  << ": " << total << endl;
	}
	return 0;
}