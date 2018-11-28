#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    bool isdir[200];
    int caseNo=1,t,n,m;
    int i,j;
    int ans,temp;
    string line;
    cin >> t;
    //cout << t << endl;
    while(t--)
    {
        int id=1;

        cin >> n >> m;
        //cout << n << m << endl;
        map<string, int > dir2num;
        for(i=0; i<n; ++i)
        {
            cin >> line;
            //cout << line << endl;
            for(j=0; j<line.length(); ++j)
            {
                if(line[j] =='/') isdir[j] = true;
                else isdir[j] = false;
            }
            for(j=1; j<line.length(); ++j)
            {
                if(isdir[j])
                {
                    string tmpstr = line.substr(0, j);
                    //cout << tmpstr << endl;
                    if(dir2num.find(tmpstr)==dir2num.end())
                    {
                        dir2num[tmpstr] = id++;
                    }
                }
            }
            if(dir2num.find(line)==dir2num.end())
            {
                dir2num[line] = id++;
            }
        }
        temp = id;
        for(i=0; i<m; ++i)
        {
            cin >> line;
            //cout << line << endl;
            for(j=0; j<line.length(); ++j)
            {
                if(line[j] =='/') isdir[j] = true;
                else isdir[j] = false;
            }
            for(j=1; j<line.length(); ++j)
            {
                if(isdir[j])
                {
                    string tmpstr = line.substr(0, j);
                    //cout << tmpstr << endl;
                    if(dir2num.find(tmpstr)==dir2num.end())
                    {
                        dir2num[tmpstr] = id++;
                    }
                }
            }
            if(dir2num.find(line)==dir2num.end())
            {
                dir2num[line] = id++;
            }
        }
        ans = id - temp;
        cout << "Case #" << caseNo++ << ": " << ans << endl;
    }
}

