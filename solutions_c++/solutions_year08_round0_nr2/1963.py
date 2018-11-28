#include <stdio.h>
#include <stdlib.h>

int N,NA,NB,turn;
char strab1[100][7];
char strab2[100][7];
char strba1[100][7];
char strba2[100][7];

int ab[100][2];
int ba[100][2];

int anka[1440],ankb[1440];
int la[1440],lb[1440];

void convert_to_min();
void write_array();

int main(int argc,char* argv[])
{
	int index=1; 
	
	FILE *in=fopen("trainfile.txt","r");
	fscanf(in,"%d",&N);
	for(int i=0;i<N;i++)
	{
		fscanf(in,"%d",&turn);
		fscanf(in,"%d",&NA);
		fscanf(in,"%d",&NB);
		if(NA==0||NB==0)
		{
			if(NA==0)
			{
				printf("Case #%d: %d %d\n",index++,NA,NB);
			}
			if(NB==0)
			{
				printf("Case #%d: %d %d\n",index++,NA,NB);
			}
		}
		else
		{
			int cura=0,curb=0,maxa=0,maxb=0;
			for(int n=0;n<1440;n++)
			{
				anka[n]=0;
				ankb[n]=0;
				la[n]=0;
				lb[n]=0;
			}
			for(int a=0;a<NA;a++)
			{
				fscanf(in,"%s",strab1[a]);
				fscanf(in,"%s",strab2[a]);
			}
			for(int a=0;a<NB;a++)
			{
				fscanf(in,"%s",strba1[a]);
				fscanf(in,"%s",strba2[a]);
			}
			convert_to_min();
			write_array();
			
			/*
			for(int ct=0;ct<1440;ct++)
			{
				if(la[ct]>0)
					printf("la[%d]: %d\n",ct,la[ct]);
				if(lb[ct]>0)
					printf("lb[%d]: %d\n",ct,lb[ct]);
				if(anka[ct]>0)
					printf("anka[%d]: %d\n",ct,anka[ct]);
				if(ankb[ct]>0)
					printf("ankb[%d]: %d\n",ct,ankb[ct]);
			}*/
			
			for(int ct=0;ct<1440;ct++)
			{
				cura+=anka[ct];
				curb+=ankb[ct];
				
				//Banhof A
				if(la[ct]) //zug startet
				{
					if(la[ct]>cura)
					{
						maxa+=la[ct]-cura;
						cura=0;
					}
					else
					{
						cura-=la[ct];
					}
				}
				
				if(lb[ct]) //zug startet
				{
					if(lb[ct]>curb)
					{
						maxb+=lb[ct]-curb;
						curb=0;
					}
					else
					{
						curb-=lb[ct];
					}
				}
			}
			printf("Case #%d: %d %d\n",index++,maxa,maxb);
			/*
			printf("Durchlauf %d\n",i);
			for(int a=0;a<NA;a++)
			{
				printf("%s",strab1[a]);
				printf(" %s\n",strab2[a]);
			}
			for(int a=0;a<NB;a++)
			{
				printf("%s",strba1[a]);
				printf(" %s\n",strba2[a]);
			}
			//printf("else\n");
			 */
		}
	}
	return 0;
}

void write_array()
{
	for(int a=0;a<NA;a++)
	{
		la[ab[a][0]]++;
		ankb[ab[a][1]]++;
	}
	for(int a=0;a<NB;a++)
	{
		lb[ba[a][0]]++;
		anka[ba[a][1]]++;
	}
}

void convert_to_min()
{
	char one[3],two[3];
	one[2]=0;
	two[2]=0;
	for(int a=0;a<NA;a++)
	{
		one[0]=strab1[a][0];
		one[1]=strab1[a][1];
		two[0]=strab1[a][3];
		two[1]=strab1[a][4];
		ab[a][0]=atoi(one)*60+atoi(two);
		//printf("ab[%d][0]: %d  ",a,ab[a][0]);
		one[0]=strab2[a][0];
		one[1]=strab2[a][1];
		two[0]=strab2[a][3];
		two[1]=strab2[a][4];
		ab[a][1]=atoi(one)*60+atoi(two)+turn;
		//printf("ab[%d][1]: %d\n",a,ab[a][1]);
	}
	
	for(int a=0;a<NB;a++)
	{
		one[0]=strba1[a][0];
		one[1]=strba1[a][1];
		two[0]=strba1[a][3];
		two[1]=strba1[a][4];
		ba[a][0]=atoi(one)*60+atoi(two);
		//printf("ba[%d][0]: %d  ",a,ba[a][0]);
		
		one[0]=strba2[a][0];
		one[1]=strba2[a][1];
		two[0]=strba2[a][3];
		two[1]=strba2[a][4];
		ba[a][1]=atoi(one)*60+atoi(two)+turn;
		//printf("ba[%d][1]: %d\n",a,ba[a][1]);
	}
}








