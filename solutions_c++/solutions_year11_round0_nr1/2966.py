#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

int T;
int N;
int Tr,Tb;
int Lr,Lb;
int T0,L0,Color;


int main()
{
	FILE *in = fopen("f:/problem1b.in","r");
	FILE *out = fopen("f:/solution1b.out","w");
	fscanf(in,"%d",&T);
	for(int i = 0;i < T ; i++)
	{
		fscanf(in,"%d",&N);
		Tr = 0;
		Tb = 0;
		Lr = 1;
		Lb = 1;
		T0 = 0;
		L0 = 1;
		Color = -1;
		for(int j = 1; j<= N; j ++)
		{
			char tempColor;
			int tempC;
			fscanf(in," %c",&tempColor);
			if(tempColor == 'O')
			{
				tempC = 0;
			}
			else
			{
				tempC = 1;
			}
			fscanf(in," %d",&L0);
			if(tempC == 0)
			{
				if(abs(L0 - Lr) >= abs(Tr - T0))
				{
					T0 = abs(L0-Lr) + T0 + 1 - abs(Tr -T0);
					Tr = T0;
					Lr = L0;
				}
				else
				{
					T0 = T0 +1;
					Tr = T0;
					Lr = L0;
				}
			}
			else
			{
				if(abs(L0 - Lb) >= abs(Tb - T0))
				{
					T0 = abs(L0-Lb) + T0 + 1 - abs(Tb -T0);
					Tb = T0;
					Lb = L0;
				}
				else
				{
					T0 = T0 +1;
					Tb = T0;
					Lb = L0;
				}
			}
		}
		fprintf(out,"Case #%d: %d\n",i+1,T0);
	}

	
}