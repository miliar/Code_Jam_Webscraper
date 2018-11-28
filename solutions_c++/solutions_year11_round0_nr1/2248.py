#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const int oo = 1 << 30;

int n;

typedef struct {
    int pos;
    bool blue;
} but;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        cin >> n;
        vector<but> b(n);
        for (int i = 0; i < n; i++)
        {
            char side;
            int pos;
            cin >> side >> b[i].pos;
            b[i].blue = side == 'B' ? true : false;
        }
        
        int pO = 1, pB = 1;
        int res = 0;
        for (int i = 0; i < n; i++)
        {
        	int need, dist;
        	int nextO = oo, nextB = oo;
        	//nextO
        	for (int j = i; j < n; j++)
        		if (b[j].blue)
        		{
        			nextB = b[j].pos;
        			break;
        		}
        	
        	for (int j = i; j < n; j++)
        		if (!b[j].blue)
        		{
        			nextO = b[j].pos;
        			break;
        		}
        	
	       	if (b[i].blue)
        	{
        		need = abs(nextB - pB) + 1;
        		dist = abs(nextO - pO);
        		
        		pB = nextB;
        		if (dist <= need)
        			pO = nextO;
        		else if (nextO < pO)
        			pO -= need;
        		else if (nextO > pO)
        			pO += need;
        	}
        	else
        	{
        		need = abs(nextO - pO) + 1;
        		dist = abs(nextB - pB);
        		
        		pO = nextO;
        		if (dist <= need)
        			pB = nextB;
        		else if (nextB < pB)
        			pB -= need;
        		else if (nextB > pB)
        			pB += need;
        	}
        	
        	res += need;
        }
        
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
