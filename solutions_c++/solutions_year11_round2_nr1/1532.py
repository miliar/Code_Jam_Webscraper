
#include <iostream>
#include <vector>
#include <list>
#include <map>


using namespace std;
//~ for(int i = 0; i < n; ++i)
int main()
{
    int t;
    cin >> t;
    for(int i =0 ; i < t; ++i)
    {
        vector< vector<char> >  mat;
        vector<char> temp;
        int n;
        cin  >> n;
        for(int j=0; j < n; ++j)
        {
            mat.push_back(temp);
            for(int k=0; k < n; ++k)
            {
                char temp_char;
                cin >> temp_char;
                mat[j].push_back(temp_char);
            }
            
            
        }
        
        vector<double> wp;
        double temp_double;
        int won = 0;
        int played = 0;
        for(int j = 0; j < n; ++j)
        {
            played = 0;
            won = 0;
            for(int k=0; k < n; ++k)
            {
                if(mat[j][k]!='.')
                {
                    ++played;
                }
                if(mat[j][k]=='1')
                {
                    ++won;
                }
            }
            //~ cout << "played: " << played << endl;
            //~ cout << "played: " << won << endl;
            temp_double = double(won)/double(played);
            wp.push_back(temp_double);
            
        }
        vector<double> owp;
        vector<double> oowp;
        vector< vector<bool> > has_played_v;
        for(int j = 0; j < n; ++j)
        {
            vector<bool> discard;
            has_played_v.push_back(discard);
            vector<double> otherswp;
            for(int l = 0; l < n; ++l)
            {
                bool has_played = false;
                if(l!=j)
                {
                    played = 0;
                    won = 0;
                    for(int k=0; k < n; ++k)
                    {
                        if(k!=j)
                        {
                            if(mat[l][k]!='.')
                            {
                                ++played;
                            }
                            if(mat[l][k]=='1')
                            {
                                ++won;
                            }
                        }
                        else
                        {
                            has_played = has_played || (mat[l][k]!='.');
                        }
                    }
                    temp_double = double(won)/double(played);
                    if(has_played)
                    {
                        otherswp.push_back(temp_double);
                    }
                    has_played_v[j].push_back(has_played);
                }
                else
                {
                    has_played_v[j].push_back(false);
                }
                
            }
            temp_double = 0.0;
            for(int l=0; l < otherswp.size(); ++l)
            {
                temp_double += otherswp[l];
            }
            temp_double = temp_double / double(otherswp.size());
            owp.push_back(temp_double);
            
        }
        for(int j = 0; j < n; ++j)
        {
            int number = 0;
            temp_double = 0.0;
            for(int l=0; l < n; ++l)
            {
                if(l!=j && has_played_v[j][l])
                {
                    ++number;
                    temp_double += owp[l];
                }
            }
            temp_double = temp_double / double(number);
            oowp.push_back(temp_double);
        }
        cout << "Case #" << i+1 << ":" << endl;
        for(int j = 0; j < n; ++j)
        {
            //~ cout << owp[j]  << endl;
            cout << 0.25 * wp[j] + 0.5 * owp[j] + 0.25*oowp[j] << endl;
        }
    }
    
    
    return 0;
}
