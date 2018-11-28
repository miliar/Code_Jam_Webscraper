#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    long long int cases, yes, no, tests, pow, count, num;
	ifstream input;
	ofstream output;

	input.open("input.in");
	output.open("output.txt");

	input >> cases;

	for(int i = 0; i < cases; i++)
	{
        input >> no;
        input >> yes;
        input >> pow;

        //cout << yes;
        //cout << no;
        //cout << pow;

        count = no;
        num = 0;
        tests = 0;

        output << "Case #" << i+1 << ": ";

        while(true)
        {
            count = count*pow;
            if(count >= yes)
            {
                break;
            }
            else
            {
                num++;
            }
        }

        while(true)
        {
            if(num == 0)
            {
                break;
            }

            if(num % 2 == 0)
            {
                num = num/2;
                tests++;
            }
            else if(num % 2 == 1)
            {
                num = (num-1)/2;
                tests++;
            }
        }

        output << tests << endl;

	}

	input.close();
	output.close();
}
