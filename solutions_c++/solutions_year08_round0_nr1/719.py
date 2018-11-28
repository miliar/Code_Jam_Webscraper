#pragma warning (disable:4786)
#include <iostream>
#include <string>
#include <fstream> 
#include <vector>
#include <map>


using namespace std;
int g_querylist[1001];
int g_querylen;

int main(int argc, char *argv[])
{
    ifstream cin("A-large.in"); 
    ofstream cout("A-large.out");

    int N = 0;
    cin >> N;
    int casei = 1;

    while (N-- > 0)
    {
        // the map of search engine, key was the id
        map<string, int> semap;
        int switchs = 0;

        // the number of search engine
        int sercheng_num;
        cin >> sercheng_num;
        vector<bool> vbfalse(sercheng_num, false);
        string m_line;
        int i;
        // skip the line
        getline(cin, m_line);
        
        for (i = 0; i < sercheng_num; i++)
        {
            getline(cin, m_line);
            semap.insert(make_pair(m_line, i));
        }
         
        // 
        int querytime;
        cin >> querytime;
        i = querytime;
        // skip the line
        getline(cin, m_line);
        
        g_querylen = querytime;
        int startid = 0;
        for (i = 0; i < querytime; i++)
        {
            getline(cin, m_line);
            g_querylist[i] = semap[m_line]; // (*(semap.find(m_line))).second;
        }

        // deal the querylist
        vector<bool> vbl(sercheng_num, false);
        int count = sercheng_num;
        for (i = 0; i < querytime; i++)
        {
            int id = g_querylist[i];
            if (vbl[id])
                continue;
            else
                vbl[id] = true;

            count --;
            if (count == 0)
            {
                i--;
                vbl = vbfalse;
                count = sercheng_num;
                switchs++;
            }
        }


        cout << "Case #"<< casei++ << ": " << switchs << endl;
    }
    return 0;
}