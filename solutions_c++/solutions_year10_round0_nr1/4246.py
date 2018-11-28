#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int case_num=1;
	int cnt;
	int N,K;
	long power,state;
	long temp;
	int j=0;
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	in >> cnt;//////////////
	while(cnt > 0)
	{
		cnt--;
		in >> N >> K;//////////////
		power=0x00000001;
		state=0x00000000;
		while(K>0)
		{
			K--;
			j=0;
			state=state^power;
			power=1;
			while((state & (1 << j++))!=0)
			{
				power=(power << 1)+1;
			}
		}
		out << "Case #" << case_num++ << ": ";/////////
		if(((power >> N) & (0x1))==1)
			out << "ON" << endl;////////
		else
			out << "OFF" << endl;//////////
	}
	return 0;
}