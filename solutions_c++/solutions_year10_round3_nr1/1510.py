#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in("A-small-attempt4.in");
	ofstream out("A-small-attempt4.out");
	int input;
	in >> input;
	for(int q = 0; q < input; q++)
	{
            int total = 0;
            int lines;
            in >> lines;
            int x[lines];
            int y[lines];
            for(int a = 0; a < lines; a++)
            {
                    in >> x[a] >> y[a];
                    
            }
            int height[lines];
            for(int a = 0; a < lines-1; a++)
            {
                    for(int b = a+1; b < lines; b++)
                    {
                            if(y[a] > y[b] && x[a] < x[b]) total++;
                            else if(y[a] < y[b] && x[a] > x[b]) total++;         
                    }
            }
            
            out << "Case #" << (q+1) << ": " << total << "\n";
            
    }
	in.close();
	out.close();
	return 0;
}
