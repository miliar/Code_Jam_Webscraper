#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>

using namespace std;

int main()
{
    int t, count;
    cin >> t;
    count=0;
    int n;    
    vector< vector<char> > table;
    vector<double> wp, owp, oowp;
    while (count<t)
    {
        count++;
        cout << "Case #" << count << ":" << endl;
        cin >> n;
        table.clear();
        wp.clear(); 
        owp.clear();
        oowp.clear();
        vector<char> temp;
        for (int i=0; i<n; i++)
        {
            temp.clear();
            for (int j=0; j<n; j++)
            {
                char ch;
                cin >> ch;
                temp.push_back(ch);
            }
            table.push_back(temp);
        }
        wp.assign(n,0);        
        owp.assign(n,0);
        oowp.assign(n,0);
        double win, lose;
        for (int i=0; i<n; i++)
        {
            win=0; lose=0;        
            for (int j=0; j<n; j++)
            {
                if (table[i][j]=='1') win++;
                if (table[i][j]=='0') lose++;
            }
            wp[i]=win/(win+lose);
        }
        double top, r;
        for (int i=0; i<n; i++)
        {
            top=0; r=0;        
            for (int j=0; j<n; j++)
            {
                if (table[i][j]=='1' || table[i][j]=='0') 
                {
                    win=0; lose=0;        
                    for (int k=0; k<n; k++)
                    {
                        if (k!=i)
                        {
                            if (table[j][k]=='1') win++;
                            if (table[j][k]=='0') lose++;
                        }
                    }
                    r+=win/(win+lose);                    
                    top++;
                }
            }
            owp[i]=r/top;
        }

        for (int i=0; i<n; i++)
        {
            top=0; r=0;        
            for (int j=0; j<n; j++)
            {
                if (table[i][j]=='1'||table[i][j]=='0') 
                {
                    top++;
                    r+=owp[j];
                }
            }
            oowp[i]=r/top;
        }

        cout.precision(12);
        for (int i=0; i<n; i++)
            cout << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << endl;

    }
    return 0;
    
}
