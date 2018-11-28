#include <iostream>
#include <vector>

using namespace std;

double get_wp(int t, const vector<vector<bool> > & w, 
                     const vector<vector<bool> > & p)
{
    int n = w.size();
    double gg = 0;
    double ww = 0;

    for (int i = 0; i < n; i++)
    {
        if (p[t][i])
            gg++;
        if (w[t][i])
            ww++;
    }
    
    return ww/gg;
}

double get_owp(int t, const vector<vector<bool> > & w, 
                     const vector<vector<bool> > & p)
{
    int n = w.size();
    double oo = 0;
    double wp = 0;

    for (int i = 0; i < n; i++)
    {
        if (p[t][i])
        {
            oo++;
            double wwl = 0;
            double ggl = 0;
            for (int j = 0; j < n; j++)
            {
                if (j == t)
                    continue;
                if (p[i][j])
                    ggl++;
                if (w[i][j])
                    wwl++;
            }
            wp += wwl/ggl;
        }
    }
    
    return wp/oo;
}

double get_oowp(int t, const vector<vector<bool> > & w, 
                       const vector<vector<bool> > & p)
{
    int n = w.size();
    double oowp = 0;
    double oo = 0;

    for (int i = 0; i < n; i++)
        if (p[t][i])
        {
            oo++;
            oowp += get_owp(i, w, p);
        }
    
    return oowp/oo;
}

vector<double> get_rpis(const vector<vector<bool> > & w, 
                        const vector<vector<bool> > & p)
{
    vector<double> r;
    double wp, owp, oowp;
    int n = w.size();

    for (int i = 0; i < n; i++)
    {
        wp = get_wp(i, w, p);
        owp = get_owp(i, w, p);
        oowp = get_oowp(i, w, p);
        r.push_back(0.25*wp+0.5*owp+0.25*oowp);
    }

    return r;
}

int main()
{
    int t, n, l;
    string s;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        vector<vector<bool> > w(n, vector<bool>(n, false));
        vector<vector<bool> > p(n, vector<bool>(n, true));
        
        for (int j = 0; j < n; j++)
        {
            cin >> s;
            l = s.size();

            for (int k = 0; k < l; k++)
                if (s[k] == '1')
                    w[j][k] = true;
                else if (s[k] == '.')
                    p[j][k] = false;
        }

        vector<double> r = get_rpis(w, p);
        
        cout << "Case #" << i+1 << ":" << endl;
        for (int j = 0; j < n; j++)
            cout << r[j] << endl;
    }
    return 0;
}
