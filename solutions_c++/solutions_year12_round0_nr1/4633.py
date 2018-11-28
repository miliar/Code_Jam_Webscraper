#include <cstdio>
#include <cstring>

using namespace std;


const char * 
bef ="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
const char * 
aft ="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

char mapi[26];

void pre_work()
{
    int i;
    memset( mapi, 255, sizeof( mapi ));
    for ( i = 0; bef[i]; i++ ) 
    {
        //if ( mapi[ bef[i] - 'a']  != -1 
        //        && mapi[ bef[i] - 'a'] != aft[i] - 'a')
        //    printf( "suck!\n" );
        mapi[ bef[i] - 'a' ] = aft[ i ] - 'a';
    }
    mapi['z' - 'a'] = 'q' - 'a';
    mapi['q' - 'a'] = 'z' - 'a';
}
int main(  )
{
    pre_work();
    //for (int i = 0; i < 26; i++)
    //    printf("%c->%c\n", i+'a', mapi[i] + 'a');
    int cs;
    char line[2048];
    scanf( "%d" , &cs);
    gets(line);
    for (int cc = 1; cc <= cs; cc++)
    {
        printf( "Case #%d: ", cc );
        gets( line );
        for(int i=0; line[i] ; i++)
        {
            if (line[i] >= 'a' && line[i] <= 'z' )
            line[i] = mapi[ line[i] - 'a' ] + 'a';      
        }
        printf( "%s\n", line );
    }
    return 0;
}
