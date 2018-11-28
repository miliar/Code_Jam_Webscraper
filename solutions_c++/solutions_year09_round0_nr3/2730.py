#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int subscount(string s,string a,int i,int j,int l)
{
    int count=0;
    if(j==18)
    {
        while(i<l)
        {
            if(s[i]==a[j])
            {
                count++;
            }    
            i++;
        }    
        return count;
    }
    while(i<l)
    {    
        while(s[i]!=a[j]&&i<l)
            i++;
        if(i==l)
            return count;
        i++;
        count+=subscount(s,a,i,j+1,l);
    }
    return count;    
}

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.in");
	int t,n;
	fin>>t;
    string s;
    string a="welcome to code jam";
	getline(fin,s);
    for(int i=0;i<t;i++)
	{
	    getline(fin,s);
	    fout<<"Case #"<<i+1<<": ";
        n=subscount(s,a,0,0,strlen( s.c_str()));
        n%=10000;
        fout<<n/1000;
        n%=1000;
        fout<<n/100;
        n%=100;
        fout<<n/10;
        n%=10;
        fout<<n;
        if(i<t-1)
        fout<<endl;
	} 
	
	fin.close();
	fout.close();
	
	return 0;
}

