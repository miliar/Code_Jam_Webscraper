#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

void solve(int t)
{
int C,D,N,i,j, outpos;
cin >> N;
int Otime = 0, Opos = 1, Btime = 0, Bpos = 1;
char c;
int *mtime, *mpos, *wtime, *wpos;

for(i=0;i<N;i++)
{
cin>>c;
if(c=='O')
{mtime = &Otime;mpos = &Opos; wtime = &Btime, wpos = &Bpos;}
else
{mtime = &Btime;mpos = &Bpos; wtime = &Otime, wpos = &Opos;}
cin>>j;
*mtime += abs(j-*mpos)+1;
if(*mtime<=*wtime)*mtime=*wtime+1;
*mpos = j;
}

cout << "Case #" << t << ": " << *mtime <<endl;
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
