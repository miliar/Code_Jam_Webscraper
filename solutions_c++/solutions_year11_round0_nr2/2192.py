#include<iostream>
#include<stdio.h>
using namespace std;

void solve(int t)
{
int C,D,N,i,j, outpos;
char str[110];
char out[110];

char nb['Z'+1]['Z'+1];
char opp['Z'+1]['Z'+1];
for(i='A';i<='Z';i++)
for(j='A';j<='Z';j++)
{nb[i][j]=0;opp[i][j]=0;}

cin >> C;
for(i=0;i<C;i++)
{
cin>>str;
nb[str[0]][str[1]] = str[2];
}

cin >> D;
for(i=0;i<D;i++)
{
cin>>str;
opp[str[0]][str[1]] = 1;
}

cin>>N;
cin>>str;

out[0] = str[0];
outpos = 0;
for(i=1;i<N;i++)
{
	char temp = nb[out[outpos]][str[i]];
	if(temp == 0) temp = nb[str[i]][out[outpos]];
	if (temp)
	{
		out[outpos] = temp;
		continue;
	}

	for(j=0;j<=outpos;j++)
	if(opp[out[j]][str[i]] || opp[str[i]][out[j]])
	{
		out[0] = str[++i];
		outpos = 0;
		goto NEXT_OUTER;
	}

	out[++outpos] = str[i];
NEXT_OUTER:;
}

cout << "Case #" << t << ": [";
for(i=0;i<=outpos;i++)
{
	if(out[0])
		cout << out[i];
	if(i==outpos)
		cout << "]" << endl;
	else
		cout << ", ";
}
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
