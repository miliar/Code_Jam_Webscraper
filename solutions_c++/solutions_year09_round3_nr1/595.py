# include <iostream>
# include <cstdio>
# include <sstream>
# include <vector>
# include <algorithm>
# include <queue>
# include <map>
# include <cstring>
# include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("out.txt");

long long pow(long long n, long long p)
{
    long long ret = 1;
    for(int i = 0;i<p;i++)
        ret*=n;
        
        return ret;
}

long long solve(string n)
{
    int used[256]={0},b=0;
    int map[256]={0};
    long long ret = 0;
    int m = 0;

    for(int i = 0;i<256;i++)	map[i]=-1;
    
    for(int i = 0;i<n.size();i++)
    {
        used[n[i]]=1;    
     }  

    for(int i = 0;i<256;i++)    b+=used[i];

	if(b == 1)	b = 2;
    map[n[0]]=1;
    
    ret += (map[n[0]]*pow(b,n.size()-1));
    
    for(int i = 1;i<n.size();i++)
    {

        if(map[n[i]]!= -1){
            ret+=(map[n[i]] * pow((long long)b,(long long)n.size()-1-i));
        }
        else{
         map[n[i]]=m++;
            if(m == 1)  m++;
               ret+=(map[n[i]] * pow((long long)b,(long long)n.size()-1-i));
        }

    }    
    
    return ret;
}

int main()
{
    int cas = 0;
    int T;
    in>>T;
    
    while(T--)
    {
        string num;
        in>>num;
               
     out<<"Case #"<<++cas<<": "<<solve(num)<<endl;   
    }    
 
 return 0;   
}
