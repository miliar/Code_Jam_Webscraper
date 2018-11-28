#include<fstream>
#include<iostream>
#include<cstring>
using namespace std;

string s_avail[200];
int n;

void sort()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(s_avail[j].compare(s_avail[j+1])>0)
            {
                s_avail[j].swap(s_avail[j+1]);
            }
        }
    }
}

int search(string s)
{
    int a=0,b=n,mid;
    string sub="";
    int comp,i=0,count=0;
    bool flag=false;
    while(s[i]!=0)
    {
        sub+=s[i];
        i++;
        
        while(s[i]!='/'&&s[i]!=0)
        {
            sub+=s[i];
            i++;
        }
        if(flag)
        {
            count++;
            s_avail[n]=sub;
            n++;
            b=n;
            continue;
        }
        b=n;
        while(a<=b && n>0)
        {
            mid=(a+b)/2;
            if((comp=sub.compare(s_avail[mid]))==0)
            {
                break;                
            }
            else if(comp<0)
            {
                b=mid-1; 
            }
            else a=mid+1;
        }
        if(a>b || n==0)
        {
            flag=true;
            count++;
            s_avail[n]=sub;
            n++;
            b=n;
        }
    }
    if(flag)
        sort();
    return count;
}

int main()
{
    ifstream fin("A.in");
    ofstream fout("A.out");
    
    int t,m,j,count;
    string s_req;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        fin>>n>>m;
        for(j=0;j<n;j++)
            fin>>s_avail[j];
        
        sort();
        count=0;
        for(j=0;j<m;j++)
        {
            fin>>s_req;
            count+=search(s_req);
        }
        fout<<"Case #"<<i<<": "<<count<<endl;
    }
}
