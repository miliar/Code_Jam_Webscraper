#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int i;
	in >> i;
	for(int p = 1; p <= i; p++)
	{
            int x, y;
            in >> x >> y;
            if(y == 0) out << "Case #" << p << ": OFF" << "\n";
            else
            {
                int w = x;
                x = 1;
                for(int q = 0; q < w ; q++)
                {
                        x = x * 2;
                }
                y = y + 1;
                int t = y % x;
                if(t == 0) out << "Case #" << p << ": ON" << "\n";
                else out << "Case #" << p << ": OFF" << "\n";
            }
    }
	in.close();
	out.close();
	return 0;
}
