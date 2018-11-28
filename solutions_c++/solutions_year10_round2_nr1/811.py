#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
using namespace std;

class Dir
{
public:
    const string name;
    vector<Dir*> child;

    Dir(const string & nme) : name(nme) {}

    ~Dir()
    {
        for(vector<Dir*>::const_iterator iter = child.begin(); iter != child.end(); iter++)
            delete * iter;
    }

    bool mkdir(deque<string> & qdir)
    {
        if(qdir.empty())
            return false;
        else
        {
            const string s = qdir.front();
            qdir.pop_front();
            for(vector<Dir*>::const_iterator iter = child.begin(); iter != child.end(); iter++)
            {
                if( (*iter)->name == s )
                    return (*iter)->mkdir(qdir);
            }
            Dir * ds = new Dir(s);
            child.push_back(ds);
            ds->mkdir(qdir);
            return true;
        }
    }

};

deque<string> splitStr(char * sin)
{
    deque<string> q;
    const char * sout = strtok(sin, "/");
    while(sout)
    {
        q.push_back(sout);
        sout = strtok(NULL, "/");
    }
    return q;
}

int main()
{
    char buffer[120];
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        Dir d("");
        int N, M;
        cin >> N >> M;
        for(int n = 0; n < N; n++)
        {
            cin >> buffer;
            deque<string> q = splitStr(buffer);
            d.mkdir(q);
        }
        int counter = 0;
        for(int m = 0; m < M; m++)
        {
            cin >> buffer;
            deque<string> q = splitStr(buffer);
            deque<string> qq;
            for(deque<string>::const_iterator iter = q.begin(); iter != q.end(); iter++)
            {
                qq.push_back(*iter);
                deque<string> qqq = qq;
                counter += d.mkdir(qqq);
            }
        }

        cout << "Case #" << t << ": " << counter << endl;
    }



    
    return 0;
}

