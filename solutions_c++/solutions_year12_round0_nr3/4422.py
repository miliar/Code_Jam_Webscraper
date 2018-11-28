#include <iostream>
#include <stdio.h>
#define cases 50
using namespace std;



int main()
{
	char cypher[] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o',
					 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g',
					 't', 'h', 'a', 'q'};
	FILE *fptr;
	fptr = fopen("input.in", "r");
	if (fptr == NULL)
		return -1;
	for (int i = 0; i < cases; i++)
	{
		char a[200];
		char b[200];
		char thestring[200];
		int a_length;
		int b_length;
		fgets (thestring, 101, fptr);
		char *strptr;
		strptr = thestring;
		
		while (*strptr != '\n')
		{
			int total_count = 0;
			int j = 0;
			while (*strptr != '\n' && *strptr != ' ')
			{
				a[j] = *strptr;
				j++;
				strptr++;
			}
			a[j] = '\0';
			a_length = j; //actual length
			strptr++;
			j = 0;
			while (*strptr != '\n' && *strptr != ' ')
			{
				b[j] = *strptr;
				j++;
				strptr++;
			}
			b[j] = '\0';
			b_length = j; //actual length
			string str_a = a;
			string str_b = b;
			int a_int = atoi(a);
			int b_int = atoi(b);
			while (a_int <= b_int)
			{
				int cur_length = 0;
				int temp = a_int;
				while ( temp > 0)
				{
					temp = temp/10;
					cur_length++;
				}
				int a_array[6];
				temp = a_int;
				//explode 
				for (int i = cur_length-1; i>=0; i--)
				{
					a_array[i] = temp % 10;
					temp /= 10;
				}
				//do the rotating here
				for (int j = 1; j < cur_length; j++)
				{
					int first = a_array[0];
					for (int k = 0; k < cur_length-1; k++)
					{
						a_array[k] = a_array[k+1];
					}
					a_array[cur_length-1] = first;
					
					//implode
					int recy = 0;
					for (int m = 0; m < cur_length; m++)
					{
						recy = recy + a_array[m];
						recy *= 10;
					}
					recy /= 10;
					if (recy <= b_int && recy > a_int && a_array[0] != 0 && recy != a_int)
					{
						total_count++;
					}
				}
				a_int++;
				
			}
					
			cout << "Case #" << i+1 << ": " << total_count << endl;
		}
		
	
	}

	system("Pause");
	return 0;
}