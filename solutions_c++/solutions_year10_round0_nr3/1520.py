#include <iostream>
#include <fstream>
using namespace std;

struct combi
{
	int next;
	long long value;
};

combi table[1000];
long long queue[1000];
long long *p;
long long *end;
long long *begin = queue;

void advance()
{
	p++;
	if(p == end)
		p = begin;	
}

int main()
{
	long long times, rooms, groups,income,currentRooms,currentGroups;
	int cases,index;
	combi tempCombi;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> cases;
	for(int i=0; i< cases; i++)
	{
		p = queue;
		income = 0;
		in >> times >> rooms >> groups;
		for(int j = 0; j<groups; j++)
			in >> queue[j];
		end = queue+groups;
		for(int j=0; j<groups;j++)
		{
			income = 0;
			p = queue+j;
			currentRooms = rooms;
			currentGroups =0;
			while(currentRooms >= *p)
			{
				currentGroups++;
				if(currentGroups > groups)
					break;
				currentRooms -= *p;
				income += *p;
				advance();
			}
			tempCombi.next = p - begin;
			tempCombi.value = income;
			table[j] = tempCombi;
		}
		income =0;
		index =0;
		for(int j =0; j<times; j++)
		{
			income += table[index].value;
			index = table[index].next;
		}

		out << "Case #" << i+1 << ": " << income << endl;		
	}
}
