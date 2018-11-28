#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

int tc, ntc;

int na, nb;
char A[26][26];
bool B[26][26];
char buf[50];
char s[1000];

int len;

int main()
{
	FILE* fi = fopen("B-large.in", "r");
	FILE* fo = fopen("B-large.out", "w");
	
	fscanf(fi, "%d", &ntc);
	for (tc = 1; tc <= ntc; tc++)
	{
		memset(A, -1, sizeof(A));
		memset(B, 0, sizeof(B));
	
		fscanf(fi, "%d", &na);
		while (na--)
		{
			fscanf(fi, "%s", buf);
			int a = buf[0] - 'A';
			int b = buf[1] - 'A'; 
			int c = buf[2] - 'A';
			A[a][b] = A[b][a] = c;
		}

		fscanf(fi, "%d", &nb);
		while (nb--)
		{
			fscanf(fi, "%s", buf);
			int a = buf[0] - 'A';
			int b = buf[1] - 'A';
			B[a][b] = B[b][a] = true;
		}
		
		fscanf(fi, "%d", &len);
		fscanf(fi, "%s", s);
		int i;
		for (i=0; i<len; i++) s[i] -= 'A';
		
		vector <int> v;
		for (i=0; i<len; i++)
		{
			v.push_back( s[i] );
			
			while (v.size() >= 2)
			{
				int a = v[v.size()-1];
				int b = v[v.size()-2];
				if (A[a][b] == -1) break;
				v.pop_back(); v.pop_back();
				v.push_back(A[a][b]);
			}
			
			if (v.size() >= 2)
			{
				int j;
				for (j=0; j<v.size()-1; j++) if (B[v[j]][v.back()]) break;
				if (j < v.size()-1)
					v.clear();
			}
		}
		
		printf("Case #%d: ", tc);
		printf("[");
		for (i=0; i<v.size(); i++)
		{
			if (i) printf(", ");
			printf("%c", v[i]+'A');
		}
		printf("]\n");
		
		fprintf(fo, "Case #%d: ", tc);
		fprintf(fo, "[");
		for (i=0; i<v.size(); i++)
		{
			if (i) fprintf(fo, ", ");
			fprintf(fo, "%c", v[i]+'A');
		}
		fprintf(fo, "]\n");
	}
	
	
	
	fclose(fi); fclose(fo);
}