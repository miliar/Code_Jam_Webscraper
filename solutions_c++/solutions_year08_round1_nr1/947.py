#include<iostream>
#include<fstream>
#include<list>
#include<algorithm>
using namespace std;

void main()
{
	int n;
	int l;
	int tmp;
	int sum;
	int caseno = 1;
	list<int> l1, l2;
	list<int>::iterator pos;
	list<int>::iterator pos2;

	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> n;
	
	while(n--)
	{
		sum = 0;
		in >> l;
		
		for(int i=0;i<l;i++)
		{
			in >> tmp;
			l1.push_back(tmp);			
		}
		l1.sort(greater<int>());
		for(int i=0;i<l;i++)
		{
			in >> tmp;
			l2.push_back(tmp);			
		}
		l2.sort(less<int>());

		//for(pos = l1.begin(); pos != l1.end(); ++pos)
		//	out << *pos << endl;
		//for(pos2 = l2.begin(); pos2 != l2.end(); ++pos2)
		//	out << *pos2 << endl;

		pos = l1.begin();
		pos2 = l2.begin();
		
		for(int i=0;i<l;i++, ++pos, ++pos2)
			sum += ((*pos) * (*pos2));


		out << "Case #" << caseno++ << ": " << sum << endl;
		l1.clear();
		l2.clear();
	}
}