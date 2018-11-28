#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool ordena ( int a, int b )
{
    return a < b;
}

int main (void)
{
    int n;
    int i;

    char linha[200];

    int saidasA[110], chegadasA[110], saidasB[110], chegadasB[110];

    vector<int> saidaA, chegadaA, saidaB, chegadaB;

    int trensA, trensB;

    fgets(linha, sizeof(linha), stdin);
    sscanf(linha,"%d",&n);

    for ( i = 0 ; i < n ; i++ )
    {
	int TTime, NA, NB, j, tempMin2, tempHour2, tempMin, tempHour;
	saidaA.clear();
	chegadaA.clear();
	saidaB.clear();
	chegadaB.clear();

	trensA = trensB = 0;

	fgets(linha, sizeof(linha), stdin);
	sscanf(linha, "%d", &TTime);

	fgets(linha, sizeof(linha), stdin);
	sscanf(linha, "%d %d", &NA, &NB);

	for ( j = 0 ; j < NA ; j++ )
	{
	    fgets(linha, sizeof(linha), stdin);
	    sscanf(linha, "%d:%d %d:%d", &tempHour, &tempMin, &tempHour2, &tempMin2);

	    saidasA[j] = tempHour * 60 + tempMin;
	    chegadasA[j] = tempHour2 * 60 + tempMin2;
	}

	saidaA.insert(saidaA.begin(), saidasA, saidasA+NA);
	chegadaA.insert(chegadaA.begin(), chegadasA, chegadasA+NA);

	sort(saidaA.begin(), saidaA.end(), ordena);
	sort(chegadaA.begin(), chegadaA.end(), ordena);

	for ( j = 0 ; j < NB ; j++ )
	{
	    fgets(linha, sizeof(linha), stdin);
	    sscanf(linha, "%d:%d %d:%d",&tempHour, &tempMin, &tempHour2, &tempMin2);

	    saidasB[j] = tempHour*60 + tempMin;
	    chegadasB[j] = tempHour2 * 60 + tempMin2;
	}
	saidaB.insert(saidaB.begin(), saidasB, saidasB+NB);
	chegadaB.insert(chegadaB.begin(), chegadasB, chegadasB+NB);

	sort(saidaB.begin(), saidaB.end(), ordena);
	sort(chegadaB.begin(), chegadaB.end(), ordena);

	vector<int>::iterator it;

	for ( it = saidaA.begin() ; it != saidaA.end() ; saidaA.erase(saidaA.begin()), it = saidaA.begin() )
	{
	    if ( chegadaB.size() > 0 && (*it) >= (*chegadaB.begin())+TTime )
		chegadaB.erase(chegadaB.begin());
	    else
		trensA++;
	}

	for ( it = saidaB.begin() ; it != saidaB.end() ; saidaB.erase(saidaB.begin()), it = saidaB.begin() )
	{
	    if ( chegadaA.size() > 0 && (*it) >= (*chegadaA.begin())+TTime )
		chegadaA.erase(chegadaA.begin());
	    else
		trensB++;
	}

	printf("Case #%d: %d %d\n", i+1, trensA, trensB);
    }

    return 0;
}

