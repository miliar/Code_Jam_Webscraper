#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back

char a[10000];


int main()
    {

    int TC;
    gets(a);
    sscanf(a,"%d",&TC);

    FOR(tc, 0, TC)
        {
        gets(a);
        string b;
        FOR(i,0,strlen(a))
            b+=a[i];
        stringstream SS(b);

        string s;
        int A[30][30];
        int B[30][30];

        FOR(i,0,30)
            FOR(j,0,30)
                A[i][j] = B[i][j] = -1;

        int C,D,N;
        SS >> C;
        FOR(i,0,C)
            {
            SS >> s;
            A[s[0]-'A'][s[1]-'A'] =  A[s[1]-'A'][s[0]-'A'] = s[2] - 'A';
            //cout << s[0]-'A' << " " <<s[1]-'A' << endl;
            
            // 1 QFT 1 RF 3 RFE
            
            }

        SS >> D;
        FOR(i,0,D)
            {
            SS >> s;
            B[s[0]-'A'][s[1]-'A'] =  B[s[1]-'A'][s[0]-'A'] = 1;
            }

        string sol;
        
        SS >> N;
        string niz;
        SS >> niz;

        int ima[30];
        memset(ima,0,sizeof(ima));
        
        FOR(i,0,N)
            {
            sol += niz[i];
            ima[niz[i] - 'A']++;
            //cout << i << endl;
           // cout << sol << endl;
            
            while( sol.size() > 1 && A[sol[(int)(sol.size()) - 1]-'A'][sol[(int)(sol.size()) - 2]-'A'] != -1 )
                {
                char c = A[sol[(int)(sol.size()) - 1]-'A'][sol[(int)(sol.size()) - 2]-'A'] + 'A';
                ima[ sol[(int)(sol.size()) - 1]-'A' ] --;
                ima[ sol[(int)(sol.size()) - 2]-'A' ] --;
                ima[ c - 'A' ] ++;
                sol = sol.substr(0,(int)(sol.size()) - 2);
                sol += c;
                }

            int last = sol[(int)(sol.size()) - 1]-'A';
            FOR(i,0,30)            
                if ( B[last][i] == 1 && ima[i] > 0 )
                    { sol = ""; memset(ima,0,sizeof(ima));}
            //cout << sol << endl;
            }

        printf("Case #%d: [",tc+1);
        FOR( i, 0,(int)(sol.size()) - 1 )
            printf("%c, ",sol[i]);
        if ( sol.size() > 0 )
            printf("%c", sol[(int)(sol.size()) - 1] );
        printf("]\n");
        }
    //system("pause");
    return 0;
    }
