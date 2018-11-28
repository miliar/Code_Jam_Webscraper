#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

void combi2(int *P, int posOfP, int startPos, int nCandy, int nDivided, unsigned long long* Candys, unsigned long long &maxVal, bool &possible)
{
	int i,j;

    if(posOfP == 0)
	{
        unsigned long long value=0;
        unsigned long long value2=0;
        unsigned long long realValue2=0;
        for(i = 0; i < nCandy; i++)
		{
            bool same=false;
            for(j = nDivided; j > 0; j--)
			{
                if(i == P[j])
				{
                    value ^= Candys[P[j]];
                    same = true;
                }
            }
            if(!same)
			{
                value2 ^= Candys[i];
                realValue2 += Candys[i];
            }
        }
        if(value == value2)
		{
            possible = true;
            if(realValue2 > maxVal) maxVal = realValue2;
        }
    }
	else
	{
        for(i = startPos; i < nCandy; i++)
		{
            P[posOfP] = i;
            combi2(P, posOfP-1, i+1, nCandy, nDivided, Candys, maxVal, possible);
        }
    }
}

int main()
{

// Read from file
#if 1
	ifstream readStream;
	ofstream writeStream;

	readStream.open("C-small-attempt0.in", ios::in);
	writeStream.open("C-small-attempt0.out", ios::out);
#endif

	char temp[10000];
	readStream.getline(temp, 10000, '\n');
	int nCase = atoi(temp);

	char *splitted;
	int i, c;
	unsigned long long* candies;
	unsigned long long maxVal = 0;
	int nDivided = 0;
	
    for(i=0; i<nCase; i++)
	{
		readStream.getline(temp, 10000, '\n');
		int nCandy = atoi(temp);
		candies = new unsigned long long[nCandy];

		readStream.getline(temp, 10000, '\n');
		splitted = strtok(temp," ");
		candies[0] = atol(splitted);
		
		unsigned long long realMax = 0;
		for(c=1; c<nCandy; c++)
		{
			splitted = strtok(NULL," ");
			candies[c] = atol(splitted);
		}

		for(c=1; c<nCandy; c++)
		{
			bool possible = false;
			nDivided = c;
			maxVal = 0;
			int *dividedCandys = new int[nCandy];
			combi2(dividedCandys, nDivided, 0, nCandy, nDivided, candies, maxVal, possible);
			if(possible)
			{
				if(maxVal > realMax) realMax = maxVal;
			}
		}

		if(realMax == 0)writeStream<<"Case #"<<i+1<<": "<<"NO"<<endl;
		else writeStream<<"Case #"<<i+1<<": "<<realMax<<endl;
	}

	readStream.clear();
	readStream.close();

	writeStream.clear();
	writeStream.close();

    return 0;
}

