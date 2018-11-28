#include <iostream>
#include <cstdio>

using namespace std;

main()
    {int cases, dancers, surp, total[100], p, resp;
    int i, j;

    cin >> cases;

        for(i = 0; i<cases; i++)
            {cin >> dancers;
            cin >>surp;
            cin >> p;
            resp = 0;

            for(j=0; j<dancers; j++)
                cin>>total[j];

            for(j=0; j<dancers; j++)
                {if(total[j] >= 3*p-2)
                    resp++;
                else if (surp > 0 && total[j] >= 3*p-4 && total[j] >= 2 && total)
                    {resp++;
                    surp--;}}

            cout<< "Case #" << i+1 << ": " << resp << endl;}}




