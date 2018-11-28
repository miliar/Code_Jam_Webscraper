// B1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


using namespace std;
#define M 20000 //Max
class one
{
public:
	int L;
	int O;
};
class lakes
{
public:
	one bottom;
	int howmanynum;
	int numlist[1000];
};
lakes Lks[26];

one lastone,thisone,tmp;
int lines,columns;
int alti[100][100];
int altiflag[100][100];
int lakes[27],smallest;
int Oi,Li,Oit,Lit;
int maxi,num,lsofar;
int ans,i,j,k,s;
char answer[100][100];
char tmpc;
int main(int argc, char* argv[])
{
	fstream fin ("B.in");
	fstream fout("B.txt");
	int Cases;
	fin>> Cases;
	for (int Ci=1;Ci<= Cases;Ci++)
	{
		lsofar = 0;
		memset(Lks,0,sizeof(Lks));
		fin>>lines>>columns;
		for(Li=1;Li<=lines;Li++)
		{
			for (Oi=1;Oi<=columns;Oi++)
			{
				fin >> alti[Li-1][Oi-1];
				altiflag[Li-1][Oi-1]=0;
				answer[Li-1][Oi-1] = 'A';
			}
		}

		num=1;

while(1)
		{	
DO:
			maxi=0;
			for(Li=0;Li<lines;Li++)
			{
				for (Oi=0;Oi<columns;Oi++)
				{
					if(alti[Li][Oi] >= maxi && altiflag[Li][Oi] == 0)
					{
						maxi = alti[Li][Oi];
						lastone.L = Li;
						lastone.O=Oi;
					}
				}
			}
			tmp.L = lastone.L;
			tmp.O = lastone.O;
			altiflag[lastone.L][lastone.O]=num; 
			smallest = alti[lastone.L][lastone.O];
			while(1)
			{		
				if(lastone.L>=1&&alti[lastone.L-1][lastone.O]<smallest)
				{
					smallest = alti[lastone.L-1][lastone.O];
					tmp.L = lastone.L-1;
					tmp.O  = lastone.O ;
				}
				if(lastone.O>=1&&alti[lastone.L][lastone.O-1]<smallest)
				{
					smallest = alti[lastone.L][lastone.O-1];
					tmp.L = lastone.L;
					tmp.O  = lastone.O-1 ;
				}
				if(lastone.O<=columns-2&&alti[lastone.L][lastone.O+1]<smallest)
				{
					smallest = alti[lastone.L][lastone.O+1];
					tmp.L = lastone.L;
					tmp.O  = lastone.O+1 ;
				}
				if(lastone.L<=lines-2&&alti[lastone.L+1][lastone.O]<smallest)
				{
					smallest = alti[lastone.L+1][lastone.O];
					tmp.L = lastone.L + 1;
					tmp.O  = lastone.O;
				}
				if(altiflag[tmp.L][tmp.O] == 0)
				{
					altiflag[tmp.L][tmp.O] = num;
					lastone.L = tmp.L;
					lastone.O =tmp.O;
					continue;
				}
				else
				{
					if(tmp.L ==lastone.L&&tmp.O ==lastone.O)
					{//the smallest in the lake
						Lks[lsofar].bottom.L= tmp.L;
						Lks[lsofar].bottom.O= tmp.O;
						Lks[lsofar].howmanynum = 1;
						Lks[lsofar].numlist[Lks[lsofar].howmanynum-1] = num;
						lsofar ++;
						altiflag[tmp.L][tmp.O] = num;
						num += 1;
						break;
					}
					else
					{
						for(i =0; i<lsofar;i++)
						{
							for(j=0;j<Lks[i].howmanynum;j++)
							{
								if(Lks[i].numlist[j] == altiflag[tmp.L][tmp.O])
								{
									Lks[i].numlist[Lks[i].howmanynum] = num;
									Lks[i].howmanynum ++;
									num++;
									goto outloop;
								}
							}
						}
					}
				}
			}
outloop:
			for(Li=0;Li<lines;Li++)
			{
				for (Oi=0;Oi<columns;Oi++)
				{
					if(altiflag[Li][Oi] != 0)
						continue;
					else
						goto DO;
				}
			}
			break;
		}
		tmpc = 'a';
		fout << "Case #"<<Ci<<":\n";
		for(Li=0;Li<lines;Li++)
		{
			for (Oi=0;Oi<columns;Oi++)
			{
				if(answer[Li][Oi]>='a'&&answer[Li][Oi]<='z')
				{
					fout<<answer[Li][Oi]<<" ";
				}
				else
				{
					for(i =0; i<lsofar;i++)
					{
						for(j=0;j<Lks[i].howmanynum;j++)
						{
							if(Lks[i].numlist[j] == altiflag[Li][Oi])
							{
								for(k=0;k<Lks[i].howmanynum;k++)
								{
									for(Lit=0;Lit<lines;Lit++)
									{
										for (Oit=0;Oit<columns;Oit++)
										{
											if(altiflag[Lit][Oit] == Lks[i].numlist[k])
											{
												answer[Lit][Oit] = tmpc;
											}
										}
									}
								}
							}
						}
					}
					tmpc += 1;
					fout<<answer[Li][Oi]<<" ";
				}
				

			}
			fout<<"\n";
		}


	}
	return 0;
}

