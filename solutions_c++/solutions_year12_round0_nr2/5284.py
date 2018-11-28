
#include<stdio.h>
#include<iostream>
#include <limits.h>
#include <stdlib.h>
#include <vector>
using namespace std;

struct ast{
    int x;int y; char dir;
};
int xe,ye;
char de;
vector< ast > asters;

double colission(bool &found)
{
    double res = INT_MAX;
    double dist = INT_MAX;
    for(int i=0;i<asters.size(); ++i)
    {
        ast &a = asters[i];
        if( de == 'U' )
        {
            if( (a.dir == 'R' && xe > a.x) || 
                (a.dir == 'L' && xe < a.x) )
            {
                if( abs(xe - a.x) == abs(ye - a.y) )
                    res = abs(xe - a.x);
            }
            else if ( a.dir == 'D' && xe == a.x )
            {
                res = (double)abs(a.y - ye) / 2;
            }
        }
        else if( de == 'D' )
        {
            if( (a.dir == 'R' && xe > a.x) || 
                (a.dir == 'L' && xe < a.x) )
            {
                if( abs(xe - a.x) == abs(ye - a.y) )
                    res = abs(xe - a.x);
            }
            else if ( a.dir == 'U' && xe == a.x )
            {
                res = (double)abs(a.y - ye) / 2;
            }
        }
        else if( de == 'L' )
        {
            if( (a.dir == 'U' && ye > a.y) || 
                (a.dir == 'D' && ye < a.y) )
            {
                if( abs(xe - a.x) == abs(ye - a.y) )
                    res = abs(xe - a.x);
            }
            else if ( a.dir == 'R' && ye == a.y )
            {
                res = (double)abs(a.x - xe) / 2;
            }
        }
        else if( de == 'R' )
        {
            if( (a.dir == 'U' && ye > a.y) || 
                (a.dir == 'D' && ye < a.y))
            {
                if( abs(xe - a.x) == abs(ye - a.y) )
                    res = abs(xe - a.x);
            }
            else if ( a.dir == 'L' && ye == a.y )
            {
                res = (double)abs(a.x - xe) / 2;
            }
        }

        if( res < dist )
        {
            dist = res;
            found = true;
        }
    }

    return dist;
}

int main()
{
    int T;
    scanf("%d", &T);
    int iter=0;
    while(T--)
    {
        int N, S, p;
        scanf("%d %d %d", &N, &S,&p);
        vector<int> scores;
        for(int i=0;i<N;++i)
        {
            int sco;
            scanf("%d", &sco);
            scores.push_back(sco);
        }

//        printf("%d %d %d %d\n", N,S,p, scores.size());
        int res=0;
        int lowestSurprisingScore = 3*p - 4;
        int lowestAcceptableScore = 3*p - 2;
        for(int i=0;i<N;++i)
        {
            if( scores[i] >= lowestAcceptableScore )
            { ++res; }
            else if( S > 0 && (lowestSurprisingScore >= 0) && 
                     (scores[i] >= lowestSurprisingScore) ) 
            { ++res; --S; }
        }

        ++iter;
        printf("Case #%d: %d\n", iter, res);
    }
}
