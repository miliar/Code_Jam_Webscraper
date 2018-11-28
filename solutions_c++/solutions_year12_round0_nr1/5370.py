#include<fstream.h>
#include<conio.h>
#include<stdio.h>

void main()
{
	int T, i, j;
	char G[30][101], S[30][101];
	fstream fi,fo;
	fi.open("input.txt",ios::in);
	fo.open("output.txt",ios::out);

	fi>>T;
	fi.getline(G[0],100,'\n');
	i=0;
	while(fi && i<T)
	{
		fi.getline(G[i],102,'\n');
		if(fi.eof())
			break;
		j=0;
		while(G[i][j]!='\0')
		{
			switch(G[i][j])
			{
			 case 'a': S[i][j] = 'y'; break;
			 case 'b': S[i][j] = 'h'; break;
			 case 'c': S[i][j] = 'e'; break;
			 case 'd': S[i][j] = 's'; break;
			 case 'e': S[i][j] = 'o'; break;
			 case 'f': S[i][j] = 'c'; break;
			 case 'g': S[i][j] = 'v'; break;
			 case 'h': S[i][j] = 'x'; break;
			 case 'i': S[i][j] = 'd'; break;
			 case 'j': S[i][j] = 'u'; break;
			 case 'k': S[i][j] = 'i'; break;
			 case 'l': S[i][j] = 'g'; break;
			 case 'm': S[i][j] = 'l'; break;
			 case 'n': S[i][j] = 'b'; break;
			 case 'o': S[i][j] = 'k'; break;
			 case 'p': S[i][j] = 'r'; break;
			 case 'q': S[i][j] = 'z'; break;
			 case 'r': S[i][j] = 't'; break;
			 case 's': S[i][j] = 'n'; break;
			 case 't': S[i][j] = 'w'; break;
			 case 'u': S[i][j] = 'j'; break;
			 case 'v': S[i][j] = 'p'; break;
			 case 'w': S[i][j] = 'f'; break;
			 case 'x': S[i][j] = 'm'; break;
			 case 'y': S[i][j] = 'a'; break;
			 case 'z': S[i][j] = 'q'; break;
			 case ' ': S[i][j] = ' '; break;

			}
			j++;

		}
		S[i][j] = '\0';
		i++;

	}

	for(i=0 ; i<T ; i++)
		fo<<"\nCase #"<<(i+1)<<": "<<S[i];

	fo.close();
	fi.close();

}
