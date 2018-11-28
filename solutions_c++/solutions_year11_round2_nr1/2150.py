#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) 
{
	freopen("input21.txt", "rt", stdin);
	freopen("output21.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		int N;
		cin >> N;
        
        vector <string> s;
        s.clear();
        for (int j = 0; j < N; j++)
        {
            string ss;
            cin >> ss;
            s.push_back(ss);
        }
        
        vector <double> wp;
        wp.clear();
        for (int j = 0; j < N; j++)
        {
            int c = 0, w = 0;
            for (int k = 0; k < N; k++) 
            {
                if (s[j][k] == '1')
                {
                    w++;
                    c++;
                }
                else if (s[j][k] == '0')
                    c++;
            }
            wp.push_back((double)w / (double)c);
        }
		
        vector <double> owp;
        owp.clear();
        for (int j = 0; j < N; j++)
        {
            vector<string> minis;
            minis.clear();
            for (int k = 0; k < N; k++)
            {
                string ws;
                for (int l = 0; l < N; l++)
                {
                    if (k == j)
                        ws += '.';
                    else
                    {
                        if (l != j)
                            ws += s[k][l];
                        else
                            ws += '.';
                    }
                }
                minis.push_back(ws);
            }
            vector<double> twp;
            twp.clear();
            for (int f = 0; f < N; f++)
            {
                int c = 0, w = 0;
                for (int k = 0; k < N; k++) 
                {
                    if (minis[f][k] == '1')
                    {
                        w++;
                        c++;
                    }
                    else if (minis[f][k] == '0')
                        c++;
                }
                if (c == 0)
                    c = 1;
                twp.push_back((double)w / (double)c);
            }
            
            int c = 0;
            double wpp = 0.0;
            for (int k = 0; k < N; k++) 
            {
                if (k != j)
                {
                    if (s[k][j] != '.')
                    {
                        wpp += twp[k];
                        c++;
                    }
                }
            }
            owp.push_back(wpp / (double)c);
        }
        
        vector <double> oowp;
        oowp.clear();
        for (int j = 0; j < N; j++)
        {
            int c = 0;
            double owpp = 0.0;
            for (int k = 0; k < N; k++) 
            {
                if (s[j][k] != '.')
                {
                    owpp += owp[k];
                    c++;
                }
            }
            oowp.push_back(owpp / (double)c);
        }
        cout << "Case #" << i+1 << ":" << endl;
        for (int j = 0; j < N; j++)
        {
            cout << 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
        }
	}
	
	return 0;
}

