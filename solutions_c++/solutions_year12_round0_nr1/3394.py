//      google jam.cpp
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

int main()

{
	char decod[27] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q', 'Z'};

	int n;
	scanf("%d", &n);

	FILE* out;
	out = fopen("teste.out", "w");

	for(int i = 0; i<n; i++)
	{
		char line[101];

		scanf(" %[^\n]", line);

		fprintf(out, "Case #%d: ", i+1);

		int o=0;
		while(line[o]!='\0')
		{
			if(line[o] != ' ')
			{
				char temp = decod[ line[o] - 'a' ];
				fprintf(out,"%c", temp);
			}
			else
				fprintf(out, " ");
			o++;
		}
		fprintf(out, "\n");
	}

	return 0;
}

