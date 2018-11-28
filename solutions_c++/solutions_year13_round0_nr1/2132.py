#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    char w;
    bool cz;
    int q;
    int e=1;
    for (q=1; q<=t; ++q)
    {
        vector <string> v(4);
        vector <string> co(4);
        for (int i=0; i<4; ++i)
        {
            cin >> co[i];
        }
        v=co;
        cz=0;
        int x[4]={0};
        int o[4]={0};
        x[0]=0, o[0]=0;
        x[1]=0, o[1]=0;
        x[2]=0, o[2]=0;
        x[3]=0, o[3]=0;
        int k=0;
        w=0;
        for (int i=0; i<4; ++i)
        {
            for (int j=0; j<4; ++j)
            {
                if (v[i][j]=='X')
                    ++x[i];
                
                if (v[i][j]=='O')
                    ++o[i];
                
                if (v[i][j]=='T')
                {
                    ++x[i];
                    ++o[i];
                }
                
                if (v[i][j]=='.')
                    ++k;
                
                
                if (x[i]==4) w='X';
                if (o[i]==4) w='O';
            }
        }
        
        x[0]=0, o[0]=0;
        x[1]=0, o[1]=0;
        x[2]=0, o[2]=0;
        x[3]=0, o[3]=0;

        
        for (int j=0; j<4; ++j)
        {
            for (int i=0; i<4; ++i)
            {
                if (v[i][j]=='X')
                    ++x[j];
                
                if (v[i][j]=='O')
                    ++o[j];
                
                if (v[i][j]=='T')
                {
                    ++x[j];
                    ++o[j];
                }
                
                if (v[i][j]=='.')
                    ++k;
                
                
                if (x[j]==4) w='X';
                if (o[j]==4) w='O';
            }
        }
        
        int ax=0, ao=0;
        
        for (int i=0; i<4; ++i)
        {
            if (v[i][i]=='X')
                ++ax;
            
            if (v[i][i]=='O')
                ++ao;
            
            if (v[i][i]=='T')
            {
                ++ax;
                ++ao;
            }
            
            if (v[i][i]=='.')
                ++k;
            
            
            if (ax==4) w='X';
            if (ao==4) w='O';
        }
        
        ax=0, ao=0;
        
        
        
        for (int i=0; i<4; ++i)
        {
            if (v[3-i][i]=='X')
                ++ax;
            
            if (v[3-i][i]=='O')
                ++ao;
            
            if (v[3-i][i]=='T')
            {
                ++ax;
                ++ao;
            }
            
            if (v[3-i][i]=='.')
                ++k;
            
            
            if (ax==4) w='X';
            if (ao==4) w='O';
        }
        
        if (w!=0) printf("Case #%d: %c won\n", q, w);
        else if (k>0) printf("Case #%d: Game has not completed\n", q);
        else printf("Case #%d: Draw\n", q);
        
        ++e;
    }


	return 0;
}