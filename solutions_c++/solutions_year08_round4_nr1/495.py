#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const int SIZE = 20005;
int value[SIZE];
struct Mymynode
{
	bool and , canchange;
};

Mymynode mynode[SIZE];
int m , v; 

int op[2][SIZE];

void DFS(int current)
{
	if(current * 2 > m)
	{
		op[value[current]][current] = 0 ;
		op[1-value[current]][current] = -1;
		return ;
	}
	DFS(2*current);
	DFS(2*current+1);
	op[0][current] = op[1][current] = INT_MAX;
	int leftzero , leftone , rightzero , rightone;
	leftzero = op[0][2*current];
	leftone = op[1][2*current];
	rightzero = op[0][2*current+1];
	rightone = op[1][2*current+1] ;
	if(mynode[current].and == true)
	{
		if(leftzero != -1 && rightzero != -1)
			if(op[0][current] > leftzero + rightzero)
				op[0][current] = leftzero + rightzero ;
		if(leftzero != -1 && rightone != -1)
			if(op[0][current] > leftzero + rightone)
				op[0][current] = leftzero + rightone ;
		if(leftone != -1 && rightzero != -1)
			if(op[0][current] > leftone + rightzero)
				op[0][current] = leftone + rightzero ;
		if( leftone != -1 && rightone != -1)
			if(op[1][current] > leftone + rightone)
				op[1][current] = leftone + rightone ;
	}
	else
	{
		if(leftzero != -1 && rightzero != -1)
			if(op[0][current] > leftzero + rightzero)
				op[0][current] = leftzero + rightzero ;
		if(leftzero != -1 && rightone != -1)
			if(op[1][current] > leftzero + rightone)
				op[1][current] = leftzero + rightone ;
		if(leftone != -1 && rightzero != -1)
			if(op[1][current] > leftone + rightzero)
				op[1][current] = leftone + rightzero ;
		if( leftone != -1 && rightone != -1)
			if(op[1][current] > leftone + rightone)
				op[1][current] = leftone + rightone ;
	}
	if(mynode[current].canchange == true)
	{
		if(mynode[current].and == true)
		{
			if(leftzero != -1 && rightzero != -1)
				if(op[0][current] > leftzero + rightzero + 1)
					op[0][current] = leftzero + rightzero + 1;
			if(leftzero != -1 && rightone != -1)
				if(op[1][current] > leftzero + rightone + 1)
					op[1][current] = leftzero + rightone + 1;
			if(leftone != -1 && rightzero != -1)
				if(op[1][current] > leftone + rightzero + 1)
					op[1][current] = leftone + rightzero + 1;
			if( leftone != -1 && rightone != -1)
				if(op[1][current] > leftone + rightone + 1)
					op[1][current] = leftone + rightone + 1;
		}
		else
		{
			if(leftzero != -1 && rightzero != -1)
				if(op[0][current] > leftzero + rightzero + 1)
					op[0][current] = leftzero + rightzero +1;
			if(leftzero != -1 && rightone != -1)
				if(op[0][current] > leftzero + rightone + 1)
					op[0][current] = leftzero + rightone + 1;
			if(leftone != -1 && rightzero != -1)
				if(op[0][current] > leftone + rightzero + 1)
					op[0][current] = leftone + rightzero+ 1 ;
			if( leftone != -1 && rightone != -1)
				if(op[1][current] > leftone + rightone + 1)
					op[1][current] = leftone + rightone + 1;
		}
	}
	if(op[0][current] == INT_MAX) op[0][current] = -1;
	if(op[1][current] == INT_MAX) op[1][current] = -1;
}
int main(void)
{
	int cases ;
	freopen("A-large.in","r",stdin);
	freopen("Aout.txt","w",stdout);
	scanf("%d",&cases);
	int i ,j,f ;
	for(f = 1 ; f <= cases ; f ++)
	{
		memset(value,-1,sizeof(value));
		int a , b;
		scanf("%d %d",&m,&v);
		for(i = 1; i <= (m - 1)/2 ; i ++)
		{
			scanf("%d %d",&a,&b);
			if(a == 1)
				mynode[i].and = 1;
			else
				mynode[i].and = 0;
			if(b == 1)
				mynode[i].canchange = 1;
			else
				mynode[i].canchange = 0;
		}
		for(i = (m - 1) /2 + 1 ; i <= m ; i ++)
			scanf("%d",&value[i]);
		DFS(1);
		printf("Case #%d:",f);
		if(op[v][1] == -1)
			printf(" IMPOSSIBLE\n");
		else
			printf(" %d\n",op[v][1]);
	}
	return 0;
}