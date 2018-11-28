#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

#define FOR(i,n) for(i=0; i<(n); ++i)

char readChar(FILE *f)
{
	char ret = ' ';
	while (ret<'A' || ret > 'Z') fscanf(f, "%c", &ret);
	return ret;
}

char C[100][3];
char O[100][2];
int M[256];
int cn, on;
vector<char> R;

bool checkCom()
{
	if (R.size() < 2) return false;
	int i;
	FOR(i, cn)
	{
		if ((R[R.size() - 1] == C[i][0] && R[R.size() - 2] == C[i][1]) || (R[R.size() - 1] == C[i][1] && R[R.size() - 2] == C[i][0]))
		{
			--M[C[i][0]];
			--M[C[i][1]];
			++M[C[i][2]];
			R.pop_back();
			R.pop_back();
			R.push_back(C[i][2]);
			return true;
		}
	}
	return false;
}

void checkOp()
{
	if (R.size() < 2) return;
	int i;
	FOR(i, on)
	{
		if ((R[R.size() - 1] == O[i][0] && M[O[i][1]]) || (R[R.size() - 1] == O[i][1] && M[O[i][0]]))
		{
			R.clear();
			memset(M, 0, sizeof(M));
			return;
		}
	}
}

int main()
{
	FILE *fi = fopen("a.txt", "rt");
	FILE *fo = fopen("a.out", "wt");

	int t,tt;

	int i,j,k,n;

	fscanf(fi, "%d", &tt);
	FOR(t,tt)
	{
		memset(M, 0, sizeof(M));
		fscanf(fi, "%d", &cn);
		FOR(i,cn)
		{
			C[i][0] = readChar(fi);
			C[i][1] = readChar(fi);
			C[i][2] = readChar(fi);
		}
		fscanf(fi, "%d", &on);
		FOR(i,on)
		{
			O[i][0] = readChar(fi);
			O[i][1] = readChar(fi);
		}

		R.clear();
		fscanf(fi, "%d", &n);
		FOR(i,n)
		{
			char c = readChar(fi);
			R.push_back(c);
			++M[c];
			if (!checkCom())
			{
				checkOp();
			}
		}
		fprintf(fo, "Case #%d: [", t+1);
		FOR(i, R.size())
		{
			fprintf(fo, "%c", R[i]);
			if (i < R.size() -1) fprintf(fo, ", ");
		}
		fprintf(fo, "]\n");
	}

	fclose(fo);
	fclose(fi);
	return 0;
}