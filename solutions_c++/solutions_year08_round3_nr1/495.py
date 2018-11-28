#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

const float PI = 3.1415926535897932384626433832795;

char *fgetline(char *buf, int size, FILE *stream)
{
	static char eolbuf[100];
	char *cp;
	int l;
	
	cp = fgets(buf,size,stream);
	l = strlen(buf);
	if (l > 0 && buf[l - 1] != '\n') {
		do {
		fgets(eolbuf,99,stream);
		l = strlen(eolbuf);
		} while (l > 0 && eolbuf[l - 1] != '\n');
	}
	return cp;
}

void splitString(string& sstring, string& separators, string& dstringBefore, string& dstringAfter)
{
	int n = sstring.length();
	int start, stop;

	start = sstring.find_first_not_of(separators);
	while ((start >= 0) && (start < n)) 
	{
		stop = sstring.find_first_of(separators, start);
		if ((stop < 0) || (stop > n)) stop = n;
		dstringBefore	= sstring.substr(0, start - 1);
		dstringAfter	= sstring.substr(start, stop - start);
		start = sstring.find_first_not_of(separators, stop+1);
	}
}

int searchString(vector<string> strVec, string str)
{
	int index = -1, i;
	for (i = 0; (i < (int) strVec.size() && index < 0); i++)
	{
		if (strVec[i] == str)
		{
			index = i;
		}
	}
	
	return index;
}

float sqr(float x)
{
	return x*x;
}

bool isPrimzahl(int x)
{
      int faktor = 2;
      while (faktor <= (x/2))
      {
            if ((x % faktor) == 0) return false;
            faktor++;
      }
      return true;
}

int main()
{
	FILE					*pOut, *pIn;
	long long				i, j, k, l, N, Y, P, K, L, /*frequency[1001]*/;
	string					str, strOut;
	vector<long long>		frequency;
	vector< vector<bool> >	keyAvailable;
	
	pIn				= fopen ("A-large.in","r");
	pOut			= fopen ("OUT.txt","w");
	
	fscanf(pIn, "%I64d",&N);
	for (i = 1; i <= N; i++)
	{
		fscanf(pIn, "%I64d %I64d %I64d\r\n", &P, &K, &L);

		frequency.clear();
		for (j = 0; j < L ; j++)
		{
			long long tmp;
			fscanf(pIn, "%I64d", &tmp);
			frequency.push_back(tmp);
		}
		std::sort(frequency.begin(), frequency.end());
		
		keyAvailable.clear();
		keyAvailable.resize(K);
		for (j = 0; j < K; j++)
		{
			keyAvailable[j].resize(P);
			
			for (k = 0; k < P; k++)
				keyAvailable[j][k] = true;
		}

		Y = 0;
		for (j = frequency.size()-1; j >= 0; j--)
		{
			long long keynumber = 0;
			for (l = 0; (l < P) && !keynumber; l++)
			{
				for (k = 0; (k < K) && !keynumber; k++)
				{
					if (keyAvailable[k][l])
					{
						keyAvailable[k][l]	= false;
						keynumber			= l+1;
					}
				}
			}
			Y += frequency[j]*keynumber;
		}
		
		fprintf(pOut, "Case #%I64d: %I64d\n", i, Y);
	}
		
	return 0;
}
