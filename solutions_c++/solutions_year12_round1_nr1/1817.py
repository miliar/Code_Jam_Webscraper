#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>
#include <math.h>

using namespace std;



int main(void)
{
	unsigned long N;


	freopen("A-small-attempt1.in", "rt", stdin);
	//freopen("A-large.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;

	unsigned long n;
	for (n=1;n<=N;n++)
	{

        vector<float> vP, vPm;
        float R, res, pt;
        int ct, ce;


        cin >> ce >> ct;

        for (int cpt=0; cpt<ce; cpt++)
        {
            cin >> pt;
            vP.push_back(pt);
            //vPi.push_back(1-pt);
            //cout << pt << " " << vP[cpt] << " " << vPi[cpt] << " "  << endl;
        }

        vPm.push_back(vP[0]);
        for (int cpt=1; cpt<ce; cpt++) vPm.push_back(vPm[cpt-1]*vP[cpt]);


        R = 2 + ct;

        res = (vPm[ce-1]*(ct-ce+1) + (1-vPm[ce-1])*(2*ct+2-ce));
        if (res<R) R=res;

        //cout << vPm[ce-1]*(ct-ce+1) << " + " << (1-vPm[ce-1])*(2*ct+2-ce) << endl;

        //printf("%4.10f\n", res);



        res = ce+ct+1; if (res<R) R=res;  // pos0 (tots els backspaces)
       // std::cout <<  res << endl;




        for (int pos=1; pos<=ce-1; pos++)
        {
            res = vPm[pos-1]*(ce-2*pos+ct+1) + (1-vPm[pos-1])*(ce-2*pos+2*ct+2);
            if (res<R) R=res;
            //cout << "pos " << pos << ": " << res << endl;
        }


		//cout << "Case #" << n << ": " << (float)R << endl;
		cout << "Case #" << n << ": ";
		printf("%4.10f\n", R);


   	}
}
