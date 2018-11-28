#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
int main()
{
    int t,i,j,c,d,cn;
    freopen("input.txt","r",stdin);
    freopen("outputB.txt","w",stdout);
	cin>>t;

	FOR1(cn,t)
	{
        char combine[100][100];
        bool opposed[100][100];
        cin>>c;
        memset(combine,' ',sizeof(combine));
        memset(opposed,0,sizeof(opposed));
        string str;
        FOR(i,c)
        {
            cin>>str;
            combine[str[0]-'A'][str[1]-'A']=str[2];
            combine[str[1]-'A'][str[0]-'A']=str[2];
        }
        cin>>d;
        FOR(i,d)
        {
            cin>>str;
            opposed[str[0]-'A'][str[1]-'A']=1;
            opposed[str[1]-'A'][str[0]-'A']=1;
        }
        int n;
        cin>>n;
        cin>>str;
        deque<char>v;
        for(i=0;i<n;i++)
        {
            //cout<<v.size()<<endl;
                /*cout<<"[";
            FOR(j,v.size())
            {
                if(j)cout<<", ";
                cout<<v[j];
            }
            cout<<"]"<<endl;;*/
            if(v.size()==0)v.push_back(str[i]);
            else
            {
                if(combine[str[i]-'A'][v[v.size()-1]-'A']!=' ')
                {
                     //cout<<"combine "<<endl;
                    char ch= combine[str[i]-'A'][v[v.size()-1]-'A'];
                    v.pop_back();
                    v.push_back(ch);
                }
                else
                {
                    int f=0;
                    FOR(j,v.size())
                    {
                        if(opposed[str[i]-'A'][v[j]-'A']==1)
                        {
                       //     cout<<"opposed "<<endl;
                            v.clear();
                            f=1;
                            break;
                        }
                    }
                    if(f==0)v.push_back(str[i]);
                }

            }
        }
        cout<<"Case #"<<cn<<": ";
        cout<<"[";
        FOR(i,v.size())
        {
            if(i)cout<<", ";
            cout<<v[i];
        }
        cout<<"]"<<endl;;
	}
	return 0;
}
