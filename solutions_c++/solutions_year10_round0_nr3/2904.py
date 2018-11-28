#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void main()
{
	int t, r, k, n, z = 1;
	ifstream in;
	in.open("C-small-attempt1.in");
	ofstream out;
	out.open("output.txt");

	in >> t;

	while(t > 0)
	{
		in >> r >> k >> n;
		int left = k;
		int front = 0, back, earn = 0;
		vector<int> g(n);
		int size = g.size();
		for(int i = 0; i < size; i++)
			in >> g[i];
		while(r > 0)
		{
			left = k;
			back = front;
			while(left >= g[front])
			{
				left = left-g[front];
				earn = earn+g[front];
				front = (front+1)%size;
				if(front == back)
					break;
			}
			r--;
		}
		out << "Case #" << z << ": " << earn << endl;
		z++;
		t--;
	}
	in.close();
	out.close();
}