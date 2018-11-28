//      google jam 3.cpp
//
//      Copyright 2012 Francisco Machado <lactor@LactorBook>
//
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.
//
//


#include <iostream>
#include <stdio.h>

int p(int a, int b)
{
	int k=1;
	for(int i=0; i<b; i++)
		k*=a;
	return k;
}

int main()
{
	int T;
	scanf("%d", &T);

	FILE* out;
	out = fopen("3.out", "w");

	for(int q = 0;q<T; q++)
	{
		int upper, lower;

		scanf("%d %d", &lower, &upper);

		int max=0;
		while(p(10,max) < upper)
		{
			max++;
		}
		max--;

		int number  = 0;

		for( int k = lower; k<= upper; k++)
		{
			int value = k;

			for(int z = 0; z<max; z++)
			{
				int temp = value % 10;

				value -= temp;

				value/=10;

				value += temp * p(10, max);


				if( value > k && value <= upper)
				{
					number++;
				}
			}
		}

		fprintf(out, "Case #%d: %d\n", q+1, number);
	}


	return 0;
}

