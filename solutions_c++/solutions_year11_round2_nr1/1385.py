#include <iostream>
#include <vector>

using namespace std;

double getWp(const string& s)
{
    double plays = 0;
    double wins = 0;
    for (int i = 0; i < s.length(); ++i)
    {
        if (s[i] == '1')
        {
            ++plays;
            ++wins;
        }
        else if (s[i] == '0')
            ++plays;
    }
    return wins / plays;
};

double getWp(const string& s, int i)
{
    string newS = s;
    newS.erase(i, 1);
    return getWp(newS);
};

double getOwp(const string& s, const vector<string>& table, int i)
{
    vector<double> wps;
    for (int j = 0; j < table.size(); ++j)
    {
        if (j != i && s[j] != '.')
            wps.push_back(getWp(table[j], i));
    }
    double owp = 0;
    for (int j = 0; j < wps.size(); ++j)
        owp += wps[j];
    return owp / wps.size();
};

double getOowp(const string& s, const vector<double>owps, int i)
{
    vector<double> oowps;
    for (int j = 0; j < owps.size(); ++j)
    {
        if (j != i && s[j] != '.')
            oowps.push_back(owps[j]);
    }
    double oowp = 0;
    for (int j = 0; j < oowps.size(); ++j)
        oowp += oowps[j];
    return oowp / oowps.size();
};

void doTestCase(int testCase)
{
    cout << "Case #" << testCase + 1 << ":" << endl;

    int n;
    cin >> n;
    
    vector<string> table;
    vector<double> wps;
    vector<double> owps;
    
    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        table.push_back(s);
    }
    
    for (int i = 0; i < n; ++i)
    {
        wps.clear();
        owps.clear();
        for (int j = 0; j < n; ++j)
        {
            wps.push_back(getWp(table[j]));
            owps.push_back(getOwp(table[j], table, j));
        }
        double rpi = (0.25 * wps[i]) + (0.5 * owps[i]) + (0.25 * getOowp(table[i], owps, i));
        cout << rpi << endl;
    }

    
    //cout << endl;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i)
        doTestCase(i);

    return EXIT_SUCCESS;
}
