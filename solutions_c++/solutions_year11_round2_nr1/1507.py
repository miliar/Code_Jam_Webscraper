#include <iostream>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

//fstream omging("problem1.in");
//fstream omgouting("problem1.out");
//#define cin omging
//#define cout omgouting

#define MSET(x) memset( (x) , 0 , sizeof((x)) )



int main()
{
     freopen( "sample21.in" , "r" , stdin );
    freopen( "sample21.out" , "w" , stdout );
    int GCJ;
    cin>>GCJ;
    for(int GCJJ=0; GCJJ<GCJ; GCJJ++)
    {
    //goes here

    int n;
    cin>>n;

    char g[n][n];
    for(int i=0; i<n; i++)
    for(int i2=0; i2<n; i2++)
    {
        cin>>g[i][i2];
    }

    // calc WP
    double sumsup[n];

    double wp[n];
    int playedGamesOf[n];
    for(int i=0; i<n; i++)
    {
        sumsup[i] = 0;
        playedGamesOf[i] = 0;
        int wonGames = 0;
        for(int i2=0; i2<n; i2++)
        {
            if( g[i][i2]=='.' ) continue;
            playedGamesOf[i]++;
            if( g[i][i2]=='1' ) wonGames++;
        }
        if( playedGamesOf[i] )
        wp[i] = (double)wonGames / playedGamesOf[i];
        sumsup[i] += wp[i]*0.25;
    }

    double oWP[n];
    for(int i=0; i<n; i++) // this player
    {
        int oponents = 0;
        double wpsum = 0.0;

        for(int i2=0; i2<n; i2++)
        {

            if( g[i][i2]!='.' ) // played with player i2
            {
                /*
                oponents++; // opponents of i

                int playedGames = 0;
                int wonGames = 0;
                for(int j=0; j<n; j++) // calculate WP of i2
                {
                    if( g[i2][j]=='.' || j!=i ) continue; // where i2 didnt play against i
                    playedGames++;
                    if( g[i2][j]=='1' ) wonGames++;
                }*/
                int mod = 0;
                if( g[i2][i] == '1' ) mod--; //else mod--;

                wpsum += (wp[i2]*playedGamesOf[i2] + mod) / (playedGamesOf[i2]-1);
            }
        }

        //if( oponents )
        oWP[i] = wpsum / playedGamesOf[i];

        //cout<<"games played against "<<i<<" - "<<playedGamesOf[i]<<endl;
        //cout<<"owp of "<<i<<" is "<< oWP[i]<<endl;
        sumsup[i] += 0.5 * oWP[i];
    }


    for(int i=0; i<n; i++)
    {
        int oponents = 0;
        double owpsum = 0.0;

        for(int i2=0; i2<n; i2++)
        {
            if( g[i][i2] == '.' ) continue;
            oponents++;
            owpsum += oWP[i2];
        }
        if( oponents )
        sumsup[i] += (owpsum/oponents) * 0.25;
    }



    cout<<"Case #"<<GCJJ+1<<": "<<endl;
    for(int i=0; i<n; i++) cout<<sumsup[i]<<endl;

    }

    return 0;
}
