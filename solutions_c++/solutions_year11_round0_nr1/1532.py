#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
using namespace std;
struct Node
{
	char c;
	int dest;
} nodes[100];
int n;
int destO, destB;
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> nodes[i].c >> nodes[i].dest;
			//gets(str);
			//sscanf(str, "%s %d", &nodes[i].c, &nodes[i].dest);
		}
		destO = destB = 1;
		int timeO = 0, timeB = 0;
		if (nodes[0].c == 'O') {
			timeO += abs(destO - nodes[0].dest) + 1;
			destO = nodes[0].dest;
		} else {
			timeB += abs(destB - nodes[0].dest) + 1;
			destB = nodes[0].dest;
		}
		for (int i = 1; i < n; i++)
		{
			if (nodes[i].c == nodes[i - 1].c) 
			{
				if (nodes[i].c == 'O') {
					timeO += abs(destO - nodes[i].dest) + 1;
					destO = nodes[i].dest;
				} else {
					timeB += abs(destB - nodes[i].dest) + 1;
					destB = nodes[i].dest;
				}
			} else
			{
				if (nodes[i].c == 'O') {
					timeO += abs(destO - nodes[i].dest) + 1;
					destO = nodes[i].dest;
					if (timeO <= timeB) timeO = timeB + 1;
				} else {
					timeB += abs(destB - nodes[i].dest) + 1;
					destB = nodes[i].dest;
					if (timeB <= timeO) timeB = timeO + 1;		
				}
			}
		}
		printf("Case #%d: %d\n", cases, max(timeB, timeO));
	}
}