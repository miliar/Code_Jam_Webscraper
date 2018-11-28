//
//  main.cpp
//  RPI


#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <iomanip.h>

using namespace std;

int main (int argc, const char * argv[])
{
    FILE *in = fopen( "A-large.in", "rt" );
    int T;
    int N;
    char line[1024];
    
    fgets(line, sizeof(line), in);
    sscanf(line, "%d", &T);
    
    cerr << T << endl;
    
    int p = 0;

    while( !feof(in) )
    {
        p++;
        vector<string> v;
        
        fgets(line, sizeof(line), in);
        sscanf(line, "%d", &N);
        
        cerr << N << endl;

        for( int i = 0; i < N; i++ )
        {
            string s;
            fgets(line, sizeof(line), in);
            s = line;
            v.push_back(s);
        }
        
        vector<long double> WP(N);
        vector<long double> OWP(N);
        vector<long double> OOWP(N);
        vector<long double> RPI(N);
        
        // WP
        for( int i = 0; i < N; i++ )
        {
            string s = v[i];
            long double wp = 0;
            int c = 0;
            
            for( int j = 0; j < s.length() - 1; j++ )
            {
                if( s[j] != '.' )
                {
                    c++;
                    wp += s[j] - '0';
                }
            }
            
            wp /= c;
            
//            cout << i << " team's WP is " << wp << endl;
            WP[i] = wp;
        }
        
        // OWP
        for( int i = 0; i < N; i++ )
        {
            string s = v[i];
            long double owp = 0;
            int c = 0;

            // チーム iのOWPを求める
            // チーム iを除外した場合の特別なWPを求める
            vector<long double> wp(N);

            for( int ii = 0; ii < N; ii++ )
            {
                string ss = v[ii];
                long double wwp = 0;
                int cc = 0;
                
                ss[i] = '.';
                for( int j = 0; j < s.length() - 1; j++ )
                {
                    if( ss[j] != '.' )
                    {
                        cc++;
                        wwp += ss[j] - '0';                            
                    }
                }
                
                wwp /= cc;
                wp[ii] = wwp;
            }
            
            
            for( int j = 0; j < s.length() - 1; j++ )
            {
                if( s[j] != '.' )
                {
                    c++;
                    owp += wp[j];
                }
            }            
            owp /= c;
            
//            cout << i << " team's OWP is " << owp << endl;
            OWP[i] = owp;
        }

        // OOWP
        for( int i = 0; i < N; i++ )
        {
            string s = v[i];
            long double oowp = 0;
            int c = 0;
            
            for( int j = 0; j < s.length() - 1; j++ )
            {
                if( s[j] != '.' )
                {
                    c++;
                    oowp += OWP[j];
                }
            }
            
            oowp /= c;
            
//            cout << i << " team's OOWP is " << oowp << endl;
            OOWP[i] = oowp;
        }
        
        cout << setprecision(12);
        printf("Case #%d:\n", p);
        for( int i = 0; i < N; i++ )
        {
            RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            cout << RPI[i] << endl;
        }
        
    }
    
    return 0;
}

