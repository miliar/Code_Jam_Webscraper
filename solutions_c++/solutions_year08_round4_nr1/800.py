#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

char buff[32768];

#define IMPOSSIBLE -1

#define LEAF -1
#define AND 1
#define OR 0
#define OPPOSITE(gate) (1-(gate))

#define NO_VALUE -1


struct node 
{
	int gate;
	int changable;
	int value;
};

typedef vector<node> t_nodes;

void get_buff()
{
	buff[0]='\0';
	gets(buff);
	//printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
	return atoi(buff);
}

void get_2_nums(int* num1,int* num2)
{
	get_buff();
	sscanf(buff,"%d %d",num1,num2);
}

int handle_gate(int gate,int val1,int val2,int goal,bool changed)
{
	if (!goal)
		gate=OPPOSITE(gate);
	switch (gate)
	{
	case AND:
		{
			if (val1==IMPOSSIBLE || val2==IMPOSSIBLE)
				return IMPOSSIBLE;
			else
				return val1+val2 + (changed?1:0);
			break;
		}
	case OR:
		{
			if (val1==IMPOSSIBLE && val2==IMPOSSIBLE)
				return IMPOSSIBLE;
			else if (val1==IMPOSSIBLE)
				return val2 + (changed?1:0);
			else if (val2==IMPOSSIBLE)
				return val1 + (changed?1:0);
			else
				return min(val1,val2) + (changed?1:0);
			break;
		}
	default:
		return IMPOSSIBLE;
	}
}

int find_minimum(t_nodes& nodes,size_t pos,int goal)
{
	node& cur=nodes[pos-1];
	if (cur.gate==LEAF)
	{
		if (cur.value==goal)
			return 0;
		else
			return IMPOSSIBLE;
	}
	else
	{
		int val1=find_minimum(nodes,2*pos,goal);
		int val2=find_minimum(nodes,2*pos+1,goal);
		int res1=handle_gate(cur.gate,val1,val2,goal,false);
		int res2=IMPOSSIBLE;
		if (cur.changable)
			res2=handle_gate(OPPOSITE(cur.gate),val1,val2,goal,true);
		if (res1==IMPOSSIBLE)
			return res2;
		else if (res2==IMPOSSIBLE)
			return res1;
		else
			return min(res1,res2);
	}
}

int main(int argc, char* argv[])
{
	int N=get_num();

	for (int i=0 ; i<N ; ++i)
	{
		int M,V;
		get_2_nums(&M,&V);
		int interiors=(M-1)/2;
		int leafs=(M+1)/2;
		t_nodes nodesVec;
		for (int j=0 ; j<interiors ; ++j)
		{
			node i;
            get_2_nums(&i.gate,&i.changable);
			i.value=NO_VALUE;
			nodesVec.push_back(i);
		}
		for (int j=0 ; j<leafs ; ++j)
		{
			node i;
			i.value=get_num();
			i.changable=0;
			i.gate=LEAF;
			nodesVec.push_back(i);
		}
		int res=find_minimum(nodesVec,1,V);

		if (res==IMPOSSIBLE)
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}

