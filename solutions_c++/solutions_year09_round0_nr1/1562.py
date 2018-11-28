#include<iostream>
#include<cmath>
#include<cstdlib>
#include<vector>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;


void g(ifstream& myfile)
{
    vector<string> x;
    ofstream m;
    m.open ("A-large.out");

    if (myfile.is_open())
    {
        int j[3];
        for(int i=0;i<=2;++i)
            myfile>>j[i];
        while(x.size()<j[1])
        {
            string s;
            getline(myfile, s);
            if(s.size()>0) x.push_back(s);
        }
        for(int n=0;n<j[2];++n)
        {
            string s;
            getline(myfile, s);
            if(s.size()>0)
            {
                int ans=0;
                string tmp[j[0]],test(s);
                int p=0,q=0;
                while(p<=test.size()-1)
                {
                    if(test[p]!='(')
                    {
                        tmp[q].push_back(test[p]);
                    }
                    else
                    {
                        while(test[p]!=')')
                        {
                            ++p;
                            tmp[q].push_back(test[p]);
                        }
                    }
                    ++p;++q;
                }
                for(int r=0;r<=j[1]-1;++r)
                {
                    bool found=true;
                    for(int t=0;t<=j[0]-1;++t)
                        if(find(tmp[t].begin(),tmp[t].end(),x[r][t])==tmp[t].end()) {found=false;break;}
                    if(found) ans++;
                }
                m<<"Case #"<<n+1<<": "<<ans<<endl;
            }
        }
        m.close();
        myfile.close();

        return;
    }
    else cout << "Unable to open file";
    return;
}



int main ()
{
    ifstream myfile ("A-large.in");
    g(myfile);

    return 0;
}

