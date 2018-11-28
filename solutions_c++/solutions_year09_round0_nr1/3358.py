/*
	Alien Language
*/

#include<iostream.h>
#include<stdio.h>
#include<malloc.h>
#include<string.h>


void main(int argc,char *argv[])
{
	long L, D, N;
	//cin>>L>>D>>N;

	FILE *fin , *fout;

	fin = fopen(argv[1],"r");
	fout = fopen(argv[2], "w");

	fscanf(fin,"%ld %ld %ld", &L,&D,&N);

	char **ptr;
	ptr = new char*[D];

	ptr[0] = new char[L*D];

	for(long i=0; i<D; i++)
	{
		ptr[i] = ptr[0] + i*L;
	}

	for(i = 0; i<D;i++)
	{
		//gets(ptr[i]);
		fscanf(fin,"%s",ptr[i]);
	}

	char str[1000];
		
	for(int input = 0;input<N;input++)
	{
		//gets(str);
		fscanf(fin,"%s",str);

		long count = 0;

		for(i=0;i<D;i++)
		{
			long len = strlen(str);

			long index=0;
			int temp = 1;

			for( long j=0; j < len ;)
			{
				int temp2 = 0;

				if(str[j] != '(')
				{
					if(str[j] == ptr[i][index])
					{
						j++;
						index++;
					}
					else
					{
						temp=0;
						break;
					}
				}
				else
				{
					j++;
					while(str[j]!=')')
					{
						if(str[j]==ptr[i][index])
						{
							index++;
							temp2 = 1;
							while(str[j]!=')')
							{
								j++;
							}
						}
						j++;
					}
					if(temp2==0)
					{
						temp=0;
						break;
					}
				}
			}

			if(temp==1)
			{
				count++;
			}
		}

		//cout<<"Case #"<<input<<": "<<count<<endl;
		fprintf(fout,"Case #%ld: %ld\n",input+1,count);
	}
	fclose(fin);
	fclose(fout);
}





