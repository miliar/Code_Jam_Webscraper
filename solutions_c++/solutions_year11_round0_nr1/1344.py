#include <cstdlib>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

int main() 
{
	/*string fname = "A-small-attempt0";   // for small input file at first attempt*/
	string fname = "A-large";          // for large input file
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T,N,nxtbtn,prvbtn,Opos,Bpos;
    long prvtym, nxttym=0,Otym,Btym;
    char nxtbot,prvbot;
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) 
    {
		scanf("%d ",&N);
		nxttym=0;prvtym=-1; //RESET
		Opos=Bpos=1; Otym=Btym=0; //BOTS BACK
        for(int d = 1 ; d <= N ; d++){
                scanf("%c %d ", &nxtbot, &nxtbtn);
                if(nxtbot == 'O'){
                        Otym += abs(nxtbtn - Opos) + 1; 
                        //tym from previous same coloured bot
                        if(Otym <= prvtym) Otym += (prvtym - Otym) + 1; 
                        //delay due to prev bot of odr colour
                        nxttym = Otym;
                        Opos=nxtbtn; //new position of Orange
                        }
                else if(nxtbot == 'B'){                                  
                        Btym += abs(nxtbtn - Bpos) + 1;  
                        //tym from previous same coloured bot
                        if(Btym <= prvtym) Btym += (prvtym - Btym) + 1;  
                        //delay due to prev bot of odr colour
                        nxttym = Btym;
                        Bpos=nxtbtn;  //new position of Blue
                        }
                //printf("[%c]-->[%c] <%ld> \n[%d]-->[%d]\n", prvbot, nxtbot,nxttym, prvbtn,nxtbtn);                
				prvbtn=nxtbtn; prvbot=nxtbot; prvtym=nxttym;
        }

        printf("Case #%d: %ld\n", c, nxttym);
	}

	return 0;
}
