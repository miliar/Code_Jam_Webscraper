#include <fstream>
#include <iostream>
#include <conio.h>

using namespace std;

int main ()	{
	ifstream in ("c:\\codejam\\2\\input.txt", ios :: in);
	if (!in)
		cout << "Input Fail\n";
	ofstream out ("c:\\codejam\\2\\output.txt");
	if (!in)
		cout << "Output Fail\n";
	int t;
	char c[36][3] = {0,0,0}, d[28][2] = {0,0}, input[100], output[100], ch, temp;
	int no_c, no_d, no_i, i, j, i1, output_i, rf, cf, tf, tt;
	int f_c[2] = {0,0}, f_d[2] = {0,0};


	in >> t;
	tt = t;

	do {
		output_i = 0;
		in >> no_c;
		for (i = 0; i < no_c; i++)	
			in >> c [i];
		//cout << c[0];

		in >> no_d;
		for (i = 0; i < no_d; i++)	
			in >> d [i];
		//cout << d[0];

		in >> no_i;
		in >> input;

		//cout << input;
		
		for (i1 = 0; i1 < no_i; i1++)	{
			ch = input[i1];
			f_c[0] = f_c[1] = f_d[0] = f_d[1] = 0;
			rf = cf = tf = 0;
			if (output_i == 0)	{
				output[output_i++] = input [i1];
				continue;
			}
			// Replacement
			for (i = 0; i < no_c; i++)	{
				for (j = 0; j < 2; j++)	{
					if (ch == c[i][j])	{
						f_c[0] = i;
						f_c[1] = j;
						rf = 1;
					}
				}
			}
			if (rf == 1)	{
			if (f_c[1] == 1)
				f_c[1] = 0;
			else if (f_c[1] == 0)
				f_c[1] = 1;

			if (output[output_i - 1] == c[f_c[0]][f_c[1]])	{
				output_i --;
				output[output_i++] = c[f_c[0]][2];
				continue;
			}
			}
			// Clearing
			for (i = 0; i < no_d; i++)	{
				for (j = 0; j < 2; j++)	{
					if (ch == d[i][j])	{
						f_d[0] = i;
						f_d[1] = j;
						cf = 1;
					}
				}
			}
			if (cf == 1)	{
			if (f_d[1] == 1)
				f_d[1] = 0;
			else if (f_d[1] == 0)
				f_d[1] = 1;
			temp = d[f_d[0]][f_d[1]];
			for (i = 0; i < output_i; i++)	{
				if (output[i] == temp)	{
					output_i = 0;
					output[0] = '\0';
					tf = 1;
					break;
				}
			}
			}
			if (tf == 1)
				continue;

			output[output_i++] = ch;
		}
		//getch();
		t--;
		output[output_i++] = '\0';
		cout << output << '\n';
		i = strlen(output);
		out << "Case #" << tt - t << ": [";
		for (i1 = 0; i1 < i; i1++)	{
			if (i1 == 0)	out << output[i1];
			else out << ", " << output[i1];
		}
		out <<"]\0"; 
		//out << output;
		out << '\n';
	}while (t);
	

	
	out.close();
	in.close();
	getch();
	return 0;
}