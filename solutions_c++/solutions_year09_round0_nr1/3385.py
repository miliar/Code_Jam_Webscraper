#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int L, D, N;
char cuv[5000][50];
char test[500][1000];
vector<int> contor;
vector<int> count;


void read()
{
	freopen("A-small.in", "r", stdin);
	cin >> L>>D>> N;
	for(int i = 0; i < D ; i++)
	{
		cin >> cuv[i];
	}
	for(int j = 0; j < N; j++)
	{
		cin >> test[j];
	}
}

void set0Contor()
{
	contor.erase(contor.begin(), contor.end());
	count.erase(count.begin(), count.end());
}

void cautaSolutii1(char l, int poz)
{
	for(int i = 0; i < D; i ++)
	{
		if(cuv[i][poz] == l)
		{
			contor.push_back(i);
			count.push_back(1);
		}
	}
}

void cautaSolutii(char l , int poz)
{
	for(int i = 0; i < contor.size(); i ++)
	{
		if(cuv[contor[i]][poz] == l)
		count[i] ++;
	}

}
 
int numaraSolutii()
{
	int nrSol = 0;
	for(int i = 0; i < contor.size(); i ++)
	{
		if(count[i] == L)
			nrSol++;
	}
	return nrSol;
}

void cautare(int poz)
{
	if(poz == 3)
	{
		poz ++;
		poz --;
	}

	string cuvant = test[poz];
	bool paranInchisa = false;
	int nrLitere = 0;
	int litereInceput = 0;

	do{
		
		if(test[poz][litereInceput] == '(')
		{
			paranInchisa = true;
		}
		else
		{
			if(test[poz][litereInceput] == ')')
			{
				paranInchisa = false;
			}
			else
			{
				cautaSolutii1(test[poz][litereInceput], 0);
			}
		}
		litereInceput++;
	}while(paranInchisa);

	for(int i = litereInceput; i < cuvant.length(); i++)
	{
		if(test[poz][i] == '(')
		{
			nrLitere++;
			paranInchisa = true;
		}
		else
		{
			if(test[poz][i] == ')')
			{
				paranInchisa = false;
			}
			else
			{
				if(!paranInchisa)
				{
					nrLitere ++;
				}
				cautaSolutii(test[poz][i], nrLitere);
				
			}
		}		

	}

}

void afisare()
{
	for(int i = 0; i < D ; i++)
	{
		cout << cuv[i]<< endl;
	}
	for(int j = 0; j < D ; j++)
	{
		cout << test[j]<< endl;
	}

}

int main(void)
{
	read();
	FILE *f = fopen("A-small.out", "w");
	for(int i = 0; i < N; i++)
	{
		cautare(i);
		fprintf(f, "%s%d%s %d\n", "Case #", i+1, ":", numaraSolutii() );
		set0Contor();
	}

	return 0;
}