#include <cstdio>

int main()
{
    int nbTests = 0;
    scanf("%d", &nbTests);
    for (int test = 0; test < nbTests; test++)
    {
	int bitLumiere = 0, etat = 0, etatVoulu= 0;
	scanf("%d%d", &bitLumiere, &etat);
	for (int i = 0; i < bitLumiere; i++)
	{
	    etatVoulu <<= 1;
	    etatVoulu |= 1;
	}
	//printf("etat %d etatVoulu %d\t", etat, etatVoulu);
	bool ON = (etat & etatVoulu) >= etatVoulu;
	printf("Case #%d: %s\n", test+1, (ON) ? "ON" : "OFF");
    }
    return 0;
}
