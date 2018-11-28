#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
#include<map>
using namespace std;

int main()
{
    int t,count=0;
    ifstream fin("C-large.in");
    ofstream fout("output31.in");
    vector <int> res;
    map <int,int> nos;
    fin>>t;
    while(t--)
    {
              nos.clear();
              int n;
              int max = 0;
              fin>>n;
              int tmp;
              res.clear();
              for(int i=0;i<n;i++)
              {fin>>tmp;res.push_back(tmp);}
    
    int ans = 0;
    int flag = 0;       
    int xori = res[0];
    for(int i=1;i<res.size();i++)
    xori = xori ^ res[i];
    if(xori != 0)
    flag = 1;
    else
    {
        sort(res.begin(),res.end());
        for(int i=1;i<res.size();i++)
        ans += res[i];
    }
    count++;
    fout<<"Case #"<<count<<": ";
    if(flag == 1)
    fout<<"NO\n";
    else
    fout<<ans<<endl;
	}
	//system("pause");
	return 0;
}
