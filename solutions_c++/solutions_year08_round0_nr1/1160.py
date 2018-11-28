#include <iostream>
#include <string>

using namespace std;

#define MAX_ENGINES 100

int main()
{
    int n, s, q, i ,j, k, no_eng, no_switches, l;
    string engines[MAX_ENGINES];
    int appeared[MAX_ENGINES];
    string str;
    
    cin>>n;
    
    for (i = 0; i < n; i++)
    {
        no_switches = 0;
        no_eng = 0;
        
        cin>>s;
        getline(cin, str);
        for (j = 0; j < s; j++)
        {
          getline(cin, engines[j]);
          appeared[j] = 0;
          //cout<<engines[j]<<endl;
        }
        
        cin>>q;
        getline(cin, str);
        for (j = 0; j < q; j++)
        {
          getline(cin, str); 
          k = -1;
          for (l = 0; l < s; l++)
            if (engines[l] == str) {k = l; break;}
          
          if (k != -1)
          {
             if (appeared[k] == 0)
             {
                appeared[k] = 1;
                no_eng++;
                if (no_eng == s)
                {
                  no_switches++;
                  for (l = 0; l < s; l++)
                    appeared[l] = 0;
                  no_eng = 1;
                  appeared[k] = 1;
                }
             }
          }
        }
        cout<<"Case #"<<i+1<<": "<<no_switches<<endl;
        
    }
    
    
    return 0;
}
