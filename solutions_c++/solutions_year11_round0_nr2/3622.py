#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef map<set<char>, char> MAP;

string solve(MAP &comap, MAP &opmap, string &seq)
{
   vector<char> res;
   res.push_back(seq[0]);
   for(int i = 1; i < seq.size(); i++)
   {
       bool app = true;
       set<char> s;
       s.insert(seq[i]);
       s.insert(res.back());
       if(comap.count(s) > 0)
       {
            res.pop_back();
            res.push_back(comap[s]);
            app = false;
       }
       else
       {
           for(int j = 0; j < res.size(); j++)
           {
                set<char> ss;
                ss.insert(seq[i]);
                ss.insert(res[j]);
                if(opmap.count(ss) > 0)
                {
                    res.clear();
                    app = false;
                    break;
                }
           }
       }
       if(app) res.push_back(seq[i]);
   }
   string s = "[";
   for(int i = 0; i < res.size(); i++)
   {
       s += res[i];
       if(i != res.size() - 1)
           s+= ", ";
   }
   s += "]";
   return s;
}

int main(int argc, char ** argv)
{
    ifstream in(argv[1]);
    ofstream out("output.txt");
    int n;
    in >> n;
    cout<<n<<endl;
    for(int i = 1; i <= n; i++)
    {
        int total;
        string item;
        MAP comap;
        MAP opmap;
        in >> total;
        for(int j = 0; j < total; j++)
        {
            in >> item;
            set<char> s;
            s.insert(item[0]);
            s.insert(item[1]);
            comap[s] = item[2];
        }
        in >> total;
        for(int j = 0; j < total; j++)
        {
            in >> item;
            set<char> s;
            s.insert(item[0]);
            s.insert(item[1]);
            opmap[s] = '0';
        }
        in >> total;
        string seq;
        in >> seq;
        string ans = solve(comap, opmap, seq);
        cout<<ans<<endl;
        out<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
