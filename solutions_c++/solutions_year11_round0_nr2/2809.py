#include <stdafx.h>
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

const long maxn=205;

char list[maxn];
long tests,n,d,sz,meta;
string temp;
long metamas[maxn][4];
long destr[maxn][3];
long q;
string str;

void add1(long number,long first,long second,long third)
{
	metamas[number][1]=first;
	metamas[number][2]=second;
	metamas[number][3]=third;
}

void add2(long number,long first,long second)
{
	destr[number][1]=first;
	destr[number][2]=second;
}

void solve()
{
	long choice;

	for (long i=0;i<=n-1;i++)
	{
		if (sz==0)
		{
			sz=1;
			list[1]=str[i];
		}
		else
		{
			bool found=false;
			for (choice=1;choice<=meta*2;choice++)
				if ((metamas[choice][1]==list[sz])&&(metamas[choice][2]==str[i]))
				{
					found=true;
					list[sz]=metamas[choice][3];
					break;
				}
			if (found==false)
			{
				for (long pred=sz;pred>=1;pred--)
				{
					for (choice=1;choice<=d*2;choice++)
						if ((destr[choice][1]==list[pred])&&(destr[choice][2]==str[i]))
						{
							sz=0;
							found=true;
							break;
						}
					if (found==true)
						break;
				}
				if (found==false)
				{
					sz++;
					list[sz]=str[i];
				}
			}
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%ld",&tests);
	for (long it=1;it<=tests;it++)
	{
		sz=0;
		scanf("%ld",&meta);
		for (q=1;q<=meta;q++)
		{
			cin >> temp;
			add1(q*2-1,temp[0],temp[1],temp[2]);
			add1(q*2,temp[1],temp[0],temp[2]);
		}
		scanf("%ld",&d);
		for (q=1;q<=d;q++)
		{
			cin >> temp;
			add2(q*2-1,temp[0],temp[1]);
			add2(q*2,temp[1],temp[0]);
		}
		scanf("%ld",&n);
		cin >> str;
		scanf("\n");

		solve();

		printf("Case #%ld: [",it);
		for (q=1;q<=sz;q++)
			if (q!=sz) printf("%c, ",list[q]);
			else printf("%c",list[q]);
		//printf("%c",list[sz]);
		printf("]\n");
	}
}