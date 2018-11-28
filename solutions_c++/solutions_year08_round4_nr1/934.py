#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

#include <cassert>

#include <math.h>

#define PI 2*acos(0.0)
typedef long long int int64;
typedef unsigned long long int uint64;

using namespace std;


int64 solve(unsigned int des, unsigned int *values, unsigned node, unsigned int *andor, unsigned int *ch, unsigned int M)
{
	int64 n1,n2,n3,n4,tot1,tot2;
	assert(node < M);
	if (des == values[node])
	{
		return 0ll;
	}
	else if (node >= (M-1)/2)
	{
		return -1ll; //impossible
	}
	else
	{	
		n1=solve(des,values,(node*2)+1, andor, ch, M);
		n2=solve(des,values,(node*2)+2, andor, ch, M);

		//n3=solve(0,values,(node*2)+1, andor, ch, M);
		//n4=solve(0,values,(node*2)+2, andor, ch, M);

		if ( (des == 1 && andor[node] == 0 ) || (des==0 && andor[node]==1))//or gate
		{
			if(n1==-1ll)
				tot1=n2;
			else if (n2==-1ll)
				tot1=n1;
			else
				tot1=(n1<n2)?n1:n2;

			if (ch[node] == 1)
			{
				if(n1==-1ll || n2 == -1ll)
					tot2=-1ll;
				else	
					tot2=n1+n2+1;


				if(tot1==-1ll)
					return tot2;
				else if(tot2==-1ll)
					return tot1;
				else
					return (tot1<tot2)?tot1:tot2;
			}
			else
			{
				return tot1;
			}

		}
		else if ( (des == 1 && andor[node] == 1 ) || (des == 0 && andor[node] == 0 ))  //and gate
		{
			if(n1==-1ll || n2 == -1ll)
				tot1=-1ll;
			else	
				tot1=n1+n2;

			if (ch[node] == 1)
			{
				if(n1==-1ll)
					tot2=n2;
				else if (n2==-1ll)
					tot2=n1;
				else
					tot2=(n1<n2)?n1:n2;
				if(tot2 != -1)
					tot2++;

				if(tot1==-1ll)
					return tot2;
				else if(tot2==-1ll)
					return tot1;
				else
					return (tot1<tot2)?tot1:tot2;
			}
			else
			{
				return tot1;
			}
		}

	}

}
int main()
{
	int64 i,j,k,l,m,n;
	int64 testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		cout << "Case #" << testId << ": ";
		//XXX  -- Read input --  XXX
		int64 M, no;
		unsigned int *values, *andor, *ch;
		unsigned int des;
		cin >> M;
		values = new unsigned int[M];
		andor = new unsigned int[M];
		ch = new unsigned int[M];

		cin >> des;
		for (i=0; i<(M-1)/2; i++)
		{
			cin >> andor[i];
			cin >> ch[i];
		}
		for (; i<M; i++)
		{
			cin >> values[i];
		}

		for(i=((M-1)/2)-1; i>=0; i--)
		{
			if(andor[i] == 1)
				values[i] = values[(i*2)+1] & values[(i*2)+2];
			else
				values[i] = values[(i*2)+1] | values[(i*2)+2];
		}
		//cout << "val[0] " << values[0] << endl;
		//cout << "des " << des << endl;

		no=solve(des, values, 0, andor, ch,M);

		//XXX  -- Print output --  XXX
		if(no == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << no << endl;

		/*
		//scanf("%s %s", p1, p2);
		char str[1024];

        gets(str);
        if (str[0]=='\0')
        	gets(str);
		*/


		//XXX  -- Process input --  XXX









		delete [] values;
		delete [] andor;
		delete [] ch;
	}

	return 0;
}
