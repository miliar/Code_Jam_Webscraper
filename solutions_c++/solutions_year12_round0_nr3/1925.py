#include <cstdlib>
#include <iostream>
#include <set>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	char aux[8];
	int casos, i, j, min, max, n, paresReciclados;
	set<int> apariciones;
	string num;
	
	cin >> casos;
	for (i = 0; i < casos; i++)
	{
		cin >> min >> max;
		paresReciclados = 0;
		while (min < max)
		{
			sprintf(aux,"%d",min);
			num = string(aux);
			for (j = 1; j < (int)num.length(); j++)
			{
				num = string(num.begin()+1,num.end()) + num[0];
				n = atoi(num.c_str());
				if ((n > min) && (n <= max) && (apariciones.find(n) == apariciones.end()))
				{
					//cout << min << " - " << n << endl;
					paresReciclados++;
					apariciones.insert(n);
				}
			}
			apariciones.clear();
			min++;
		}
		cout << "Case #" << i+1 << ": " << paresReciclados << endl;
	}
	
	return 0;
}

