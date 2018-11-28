//Small data set

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int cases, wires, crosses;
    int* x;
    int* y;
	ifstream input;
	ofstream output;

	input.open("input.in");
	output.open("output.txt");

    input >> cases;
    //cout << cases;

    for(int i = 0; i < cases; i++)
    {
        crosses = 0;
        input >> wires;

        x = new int[wires];
        y = new int[wires];

        //cout << wires;
        input >> x[0];
        input >> y[0];
        if(wires == 1)
        {
            output << "Case #" << i+1 << ": 0" << endl;
        }
        else
        {
            for(int j = 1; j < wires; j++)
            {
                input >> x[j];
                input >> y[j];
                for(int k = 0; k < j; k++)
                {
                    if((x[k] > x[j] && y[k] < y[j]) || (x[k] < x[j] && y[k] > y[j]))
                    {
                        crosses++;
                    }
                }
            }
            output << "Case #" << i+1 << ": " << crosses << endl;
        }
    }

	input.close();
	output.close();
}
