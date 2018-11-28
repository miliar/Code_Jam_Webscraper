#include <stdio.h>
#include <string>


unsigned char acmap[256][256];

std::string killmap[256];


int main(void)
{

    FILE *f;
	f=fopen("B-large.in","r");

	int time=0;
	int tc;
	fscanf(f,"%d\n",&tc);
	for(int t=0;t<tc;t++)
	{
		int ac;
		fscanf(f,"%d ",&ac);

		memset(acmap,0,sizeof(acmap));
		memset(killmap,0,sizeof(killmap));

        for(int i=0;i<ac;i++)
		{
			char buffer[1024];
			fscanf(f,"%s ",&buffer);
            if (buffer[3]) return 0;
			acmap[buffer[0]][buffer[1]]=buffer[2];
			acmap[buffer[1]][buffer[0]]=buffer[2];
		};

		int kc;
		fscanf(f,"%d ",&kc);

		for(int i=0;i<kc;i++)
		{
			char buffer[1024];
			fscanf(f,"%s ",&buffer);
			if (buffer[2]) 
				return 0;

			killmap[buffer[0]] += buffer[1];
			killmap[buffer[1]] += buffer[0];
		};

		int isin[256];
		memset(isin,0,sizeof(isin));
		std::string fin;
		fin="";
		int ic;
		fscanf(f,"%d ",&ic);
		for(int i=0;i<ic;i++)
		{
			int ch=0;
			fscanf(f,"%c",&ch);
			
			if (fin.length())
			{
				unsigned char lastch = fin[fin.length()-1];
				if (acmap[ch][lastch]) 
				{
					isin[fin[fin.length()-1]]--;
					fin[fin.length()-1] = acmap[ch][lastch];
					isin[acmap[ch][lastch]]++;
				}
				else
				{
					bool kill = false;
					for(int j=0;j<killmap[ch].length();j++)
					{
						if (isin[killmap[ch][j]])
						{
							kill = true;
						};
					};

                    if (kill)
					{
						memset(isin,0,sizeof(isin));
						fin = "";
					}
					else
					{
						fin += ch;
						isin[ch]++;
					}

				};
			}
			else
			{
				fin += ch;
				isin[ch]++;
			}

		};


		fscanf(f,"\n");
		printf("Case #%d: [",t+1);
		for(int i=0;i<fin.length();i++)
		{
			if (i!=0) printf(", ");
			printf("%c",fin[i]);
		};
		printf("]\n");

	};





	return 1;
};