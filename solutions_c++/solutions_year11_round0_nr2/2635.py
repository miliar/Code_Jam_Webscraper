#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
using namespace std;
#define forn(i,n) for(int i = 0 ; i < (int) (n) ; i ++)
#define pb push_back
main()
{
    #ifdef ACMTUYO
        freopen("a.in","r",stdin);
    #endif
    int cc;
    cin >>cc;
    forn(kk,cc)
    {
        vector<vector<int> > op (150,*new vector<int> (150,0));
        vector<vector<int> > ch (150,*new vector<int> (150,0));
        int n;
        cin>>n;

        forn(i,n)
        {
            string a;
            cin >>a;
            ch[a[0]][a[1]] = a[2];
            ch[a[1]][a[0]] = a[2];
        }

        cin>>n;

        forn(i,n)
        {
            string a;
            cin >>a;
            op[a[0]][a[1]] = 1;
            op[a[1]][a[0]] = 1;
        }

        cin>>n;
        string ss;
        cin>>ss;
        //cerr<<ss<<endl;
        bool cambios = true;
      //  while (cambios)
        {
            cambios = false;
            forn(i,ss.size())
            {
                if (i == 0) continue;
                if ( ch[ss[i]][ss[i-1]] != 0)
                {
                    ss[i-1] = ch[ss[i-1]][ss[i]];
                    for(int j = i; j < ss.size()-1;j++)
                        ss[j] = ss[j+1];
                    cambios = true;
                    ss.resize(ss.size()-1);
                    i --;
                    continue;

                }
                 for(int j = 0; j < i;j++)
                        if (op[ss[i]][ss[j]] != 0)
                        {
                            int k= 0;
                            while(i+k+1 < ss.size())
                            {
                                ss[k] = ss[i+k+1];
                                k++;
                            }
                            cambios = true;
                            ss.resize(k);
                            i = -1;
                            break;

                        }

            }





        }
        string res = "";
        forn(i,ss.size()-1)
        {
            res = res+ss[i]+", ";

        }
        if (ss.size()!= 0)
            res+=ss[ss.size()-1];
        cout<<"Case #"<<kk+1<<": ["<<res<<"]"<<endl;


    }

}
