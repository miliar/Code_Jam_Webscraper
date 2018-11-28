//      google jam 2.cpp
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
#include <math.h>

#define NMAX 101

int main()
{
	int T;
	scanf("%d", &T);

	FILE* out;
	out=fopen("2.out", "w");

	for(int i = 0; i<T; i++)
	{
		int N, S, P;
		int number = 0;
		int value[NMAX];

		scanf("%d %d %d", &N, &S, &P);


		for(int o = 0; o<N; o++)
			scanf("%d", &value[o]);

		for(int o = 0; o<N; o++)
		{
			if( (int)ceil(value[o]/3.0) >= P)
				number++;

			else if( value[o] % 3 == 0 && (int)ceil(value[o]/3.0) + 1 >= P && S>0 && value[o] != 0)
			{
				number++;
				S--;
			}

			else if( value[o] % 3 == 2 && (int)ceil(value[o]/3.0) + 1 >= P && S>0 && value[o] != 0)
			{
				number++;
				S--;
			}
		}

		fprintf(out, "Case #%d: %d\n", i+1, number);
	}


	return 0;
}

