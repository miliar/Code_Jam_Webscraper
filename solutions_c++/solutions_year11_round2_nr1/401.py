#include <algorithm>
#include <iostream>
#include <string.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);


    int T;
    cin >> T;
    char games[128][128];
    int won[128];
    int lost[128];
    double wp[128];
    double owp[128];

    for (int t = 0; t < T; ++t)
    {
    	int n;
        cin >> n;

        int gres[128][128];
        double wp[128];

        for (int i=0;i<n;i++)
        {
            cin >> games[i];
            won[i] = 0;
            lost[i] = 0;
            for (int j=0;j<n;j++)
            {
            	if ('1'==games[i][j]) ++won[i];
            	if ('0'==games[i][j]) ++lost[i];
            }
        }

//       for (int i=0;i<n;i++)
//   	   cout << endl << " won[i]: " << won[i] << " lost[i]: " << lost[i] << " games: " << games[i] << endl;

        cout << "Case #" << t+1 << ": " << endl;

        for (int i=0;i<n;i++)
        {
        	double WP = (double)(won[i]) / (double)(won[i]+lost[i]);

        	double OWP = 0.0;

        	for (int j=0;j<n;j++)
        	{
        		double cowp = 0.0;
       			if (games[i][j]=='1')
       				cowp = 	(double)(won[j]) / (double)(won[j]+lost[j]-1);
       			if (games[i][j]=='0')
       				cowp = 	(double)(won[j]-1) / (double)(won[j]+lost[j]-1);
       			if (games[i][j]!='.')
       				OWP += cowp;

//       			printf("i:%d   j:%d   cowp:%f   games[i][j]:%c   won[j]:%d  lost[j]:%d\n",i,j,cowp,games[i][j],won[j],lost[j]);

       	}
        	OWP = OWP / (double)(won[i]+lost[i]);

        	wp[i] = WP;
        	owp[i] = OWP;
        }
        for (int i=0;i<n;i++)
        {
        	double oowp = 0.0;
        	for (int j=0;j<n;j++)
        		if (games[i][j]!='.')
        			oowp += owp[j];
        	oowp = oowp / (double)(lost[i]+won[i]);

        	double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp;
        	cout << setprecision(12) <<  rpi << endl;
        }
    }

    return 0;
}
