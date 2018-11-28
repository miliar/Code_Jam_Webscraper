
#include <string>
#include <fstream>
#include <vector>
using namespace std;
int n,m,j;

long long int count(string d,string* dir)
{
    if(d.size()==0)
    return 0;
    for(int i=0;i<n;i++)
    {
        if(d==dir[i])
        {
            return 0;
        }
    }
    int j;
    for(j=d.size()-1;j>=0;j--)
    {
        if(d[j]=='/')
        {
            break;
        }
    }
    string temp=d.substr(0,j);
    long long int ans=count(temp,dir);
    dir[n]=d;
    n++;
    return (1+ans);
}
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int t;
    fin>>t;


    long long int ans;
    string dir[10000],newd[100];
    for(int i=0;i<t;i++)
    {
        fin>>n>>m;

        for(j=0;j<n;j++)
        {

            fin>>dir[j];
            }
        for(j=0;j<m;j++)
        {
            fin>>newd[j];
         }
        ans=0;
        for(j=0;j<m;j++)
        {
            ans+=count(newd[j],dir);
        }
        fout<<"Case #"<<i+1<<": "<<ans<<endl;

    }
}
