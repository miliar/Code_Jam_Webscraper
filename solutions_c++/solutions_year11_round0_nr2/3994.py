#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

int main() {


   ifstream cin("B-large.in");
   ofstream cout("output.out");

    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        map<pair<char,char>, char> comb;
        map<pair<char,char>, bool> opp;
        
        int c;
        cin >> c;

        while(c--)
        {
            string s1;
            cin >> s1;

            comb[make_pair(s1[0],s1[1])] = s1[2];
        }

        cin >> c;
        while(c--)
        {
            string s2;
            cin >> s2;

            opp[make_pair(s2[0],s2[1])] = true;
        }

        cin >> c;

        
        string s3;
        cin >> s3;

        string res = "";
        int cur = -1;
        
        for(int j=0;j<s3.size();j++)
        {

           

           if(res=="")
           {
               res=res+s3[j];
           }
           else if((comb[make_pair(s3[j],res[cur])] >= 'A' && comb[make_pair(s3[j],res[cur])] <= 'Z') ||
                   (comb[make_pair(s3[j],res[cur])] >= 'a' && comb[make_pair(s3[j],res[cur])] <= 'z') ||
                   (comb[make_pair(res[cur],s3[j])] >= 'A' && comb[make_pair(res[cur],s3[j])] <= 'Z') ||
                   (comb[make_pair(res[cur],s3[j])] >= 'a' && comb[make_pair(res[cur],s3[j])] <= 'z'))
           {

               
               res[cur] = max(comb[make_pair(s3[j],res[cur])], comb[make_pair(res[cur],s3[j])]);
               cur --;
           }
           else
           {
               bool isop = false;
               
               for(int k=0;k< res.size();k++)
               {
                   if(opp[make_pair(s3[j],res[k])] || opp[make_pair(res[k],s3[j])])
                   {
                       isop = true;
                       res ="";
                       cur = -2;
                       break;
                   }

               }

               if(!isop)
               {
                   res=res+s3[j];
               }
           }

           cur ++;
        }

        cout << "Case #" << i+1 << ": [";

        for(int z = 0; z<res.size();z++)
        {
            cout << res[z];
            if(z!=res.size()-1)
                cout << ", " ;
        }

        cout << "]" << endl;


    }

    return 0;
}

