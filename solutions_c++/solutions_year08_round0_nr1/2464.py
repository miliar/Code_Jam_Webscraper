#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;
fstream in("input.in",ios::in);
fstream out("output1.txt",ios::out);
#define cin in 
#define cout out
int main()
{
    
    int testcases;
    cin>>testcases;
    for(int c=0;c<testcases;c++)
    {
            map <string,int> m;
            int searchengine,query;
            cin>>searchengine;
            string s;
            getline(cin,s);
            for(int i=0;i<searchengine;i++)
            {
                    getline(cin,s);                //care of space has not been taken
                    m[s]=i;
            }
            cin>>query;
            vector<string> q;
            getline(cin,s);
            for(int i=0;i<query;i++)
            {
                  
                    getline(cin,s);
                    q.push_back(s);
            }
            int ans=0;
            vector <int> flag(searchengine);
            int count=0;
            for(int i=0;i<query;i++)
            {
                    if(m.find(q[i])!=m.end())
                    {
                                             if(flag[m[q[i]]]==0)
                                             {
                                                                 if(count==searchengine-1)
                                                                 {
                                                                  count=0;
                                                                  ans++;
                                                                  for(int j=0;j<searchengine;j++)
                                                                          flag[j]=0;
                                                                  }
                                                                  
                                                                 count++;
                                                                 flag[m[q[i]]]++;
                                             }
                                             else
                                                 flag[m[q[i]]]++;
                    
                    }
            }
            cout<<"Case #"<<c+1<<": "<<ans<<endl;
            m.clear();
    }
  //  system("pause");
    return 0;
}
