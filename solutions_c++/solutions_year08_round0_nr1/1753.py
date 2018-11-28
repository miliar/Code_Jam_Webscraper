#include<iostream>
#include<fstream>
#include<map>
#include<vector>
#include<string>
using namespace std;

map<string,int> name;
int n;

int id(string s)
{
    if(name.find(s)!=name.end())return name[s];
    name[s]=n++;
    return n-1;
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("c:\\data\\A-large.in");
    fout.open("c:\\data\\as.txt");
    int t;
    fin>>t;
    bool yes[1005];
    int a[1005];
    int m;
    string temp;
    char tem[1000];
    int k;
    for(int cas=1;cas <=t ; ++cas)
    {
        n=0;
        name.clear();
        fin>>m;
        char ch;
        for(int i=0;i<m;++i)
        {
            fin>>ch;
            fin.getline(tem,1000);
            temp=ch;
            temp+=tem;
            id(temp);
        }
        fin>>k;
        int ret=0;
        memset(yes,false,sizeof(yes));
        int used=0;
        for(int i=0;i<k;++i)
        {
            fin>>ch;
            fin.getline(tem,1000);
            temp=ch;
            temp+=tem;
            a[i]=name[temp];
            if(!yes[a[i]])
            {
             used++;
             if(used==m)
             {
                used=1;
                memset(yes,false,sizeof(yes));
                ret++;
             }
             yes[a[i]]=true;                    
            }
        }
        fout<<"Case #"<<cas<<": "<<ret<<endl;
    }
    fin.close();
    fout.close();
    return 0;    
}
