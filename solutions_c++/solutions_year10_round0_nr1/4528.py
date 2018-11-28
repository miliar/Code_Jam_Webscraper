#include<stdio.h>


struct Z
{
    int energ;
    int lig;
} v[32];


int main ()
{
    int x;
    scanf ("%d", &x);
    int count = 1;
 
    while (x)
    {
        int n;
        int k;
        scanf ("%d %d", &n, &k);
 
		for (int i=0; i<n; i++) 
		{
			v[i].energ = 0;
			v[i].lig = 0;
		}
		v[0].energ = 1;
 
        for(int i=0; i<k; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (v[j].energ)
                    v[j].lig = v[j].lig ? 0:1;
                else break;
            }
            for(int j=0; j<n; j++)
				v[j+1].energ = (v[j].energ && v[j].lig) ? 1:0;
        }
 
        printf("Case #%d: %s\n", count++, v[n-1].energ && v[n-1].lig ? "ON":"OFF");
        x--;
    }
 
    return 0;
}
