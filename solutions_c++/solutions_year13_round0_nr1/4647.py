#include<cstdio>
#include<cstdlib>

using namespace std;

char mx[6][6];
int N;

void solve();
void reset();
void cnt(char c);
bool check();
void print();

int main()
{
int i, j;

gets(mx[0]);
N = atoi(mx[0]);
for(i = 0; i < N; i++)
	{
	for(j = 0; j < 5; j++)
		gets(mx[j]);
//	print();
	printf("Case #%d: ", i+1);
	solve();
	}
return 0;
}

void print()
{
int i, j;
for(i = 0; i < 4; i++)
	{
	for(j = 0; j < 4; j++)
		printf("%c",mx[i][j]);
	printf("\n");
	}
}




int xs, os, ts, dots;
bool dotsSeen;


void solve()
{
int i, j;
dotsSeen = false;

for(i = 0; i < 4; i++)
	{
	reset();
	for(j = 0; j < 4; j++)
		cnt(mx[i][j]);
	if(check()) return;
	}

for(j = 0; j < 4; j++)
	{
	reset();
	for(i = 0; i < 4; i++)
		cnt(mx[i][j]);
	if(check()) return;
	}

reset();
for(i = 0; i < 4; i++)
	cnt(mx[i][i]);
if(check()) return;

reset();
for(i = 0; i < 4; i++)
	cnt(mx[i][3-i]);
if(check()) return;

if(dotsSeen) printf("Game has not completed\n");
else printf("Draw\n");
}


void reset()
{
	xs = os = ts = dots = 0;
}


void cnt(char c)
{
if(c == '.') dots++;
else if(c == 'X') xs++;
else if(c == 'O') os++;
else ts++;
}



bool check()
{
if(xs == 4 || (xs == 3 && ts == 1)) { printf("X won\n"); return true; }
if(os == 4 || (os == 3 && ts == 1)) { printf("O won\n"); return true; }
if(dots) dotsSeen = true;
return false;
}

