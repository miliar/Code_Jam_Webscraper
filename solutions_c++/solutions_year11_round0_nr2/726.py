#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);freopen("A-large.txt","w",stdout);
    freopen("B-large.in","r",stdin);freopen("B-large.txt","w",stdout);
    int testCaseCount = 0;
    scanf( "%d", &testCaseCount );
    for ( int caseId=1; caseId <= testCaseCount; caseId++)
    {
        char comb[50][3];
        char opp[50][2];

        int combCount;
        int oppCount;
        int invokeCount;
        vector<char> invoke;

        scanf( "%d", &combCount );
        for ( int i = 0; i < combCount; ++i )
        {
            //cout<<combCount<<endl;
            scanf(" %c%c%c", &comb[i][0], &comb[i][1], &comb[i][2] );
        }

        scanf( "%d", &oppCount );
        for ( int i = 0; i < oppCount; ++i )
        {
            //cout<<oppCount<<endl;
            scanf(" %c%c", &opp[i][0], &opp[i][1] );


        }

        scanf( "%d ", &invokeCount );
        for ( int i = 0; i < invokeCount; ++i )
        {
            char temp;
            scanf("%c", &temp );
            bool isCombined = false;
            for ( int j = 0; j < combCount; ++j )
            {
                if ( invoke.size() == 0 )
                {
                    invoke.push_back( temp );
                    goto END;
                }
                if (
                    ( temp == comb[j][0] && invoke[invoke.size()-1] == comb[j][1] )
                    || ( temp == comb[j][1] && invoke[invoke.size()-1] == comb[j][0] )
                   )
                {
                    invoke.pop_back();
                    invoke.push_back( comb[j][2] );
                    goto END;
                }
            }
            for ( int a = 0; a < oppCount; ++a )
            {
                for ( int b = 0; b < invoke.size(); ++b )
                {
                    if (
                        ( temp == opp[a][0] && invoke[b] == opp[a][1] )
                        || ( temp == opp[a][1] && invoke[b] == opp[a][0] )
                       )
                    {
                        invoke.clear();
                        goto END;
                    }
                }
            }
            invoke.push_back( temp );
            END:
            ;

        }


        cout<<"Case #"<<caseId<<": [";

        for ( int c = 0 ; c < invoke.size(); ++c )
        {
            if ( c == 0 )
            {
                cout<<invoke[c];
            }
            else
            {
                cout<<", "<<invoke[c];
            }
        }
        cout<<"]"<<endl;

        fflush(stdout);
    }
    return 0;

}
