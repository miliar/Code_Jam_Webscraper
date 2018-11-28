#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

bool letter[15][26];
char dict[5000][16];
int l,d,pos[15];

void sim(char *str)
{
    char group[15][30];
    int len[15];
    for(int i=0,j=0;i<l;++i,++j)
    {
        if(str[j]=='(')
        {
            int k=0;
            do group[i][k++]=str[++j]; while(str[j]!=')');
            len[i]=k-1;
        }
        else
        {
            group[i][0]=str[j];
            len[i]=1;
        }
    }
    pos[0]=0;
    for(int i=1;i<l;++i)
    {
        int j;
        for(j=i;j>0 && len[pos[j-1]]>len[i];--j) pos[j]=pos[j-1];
        pos[j]=i;
    }
    for(int i=0;i<l;++i)
    {
        for(int j=0;j<26;++j) letter[i][j]=false;
        for(int j=0;j<len[pos[i]];++j) letter[i][group[pos[i]][j]-'a']=true;
    }
}

int check()
{
    int s=0;
    for(int i=0;i<d;++i)
    {
        int j=0;
        while(j<l && letter[j][dict[i][pos[j]]-'a']) ++j;
        if(j==l) ++s;
    }
    return s;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    int n;
    fin>>l>>d>>n;
    for(int i=0;i<d;++i) fin>>dict[i];
    for(int i=0;i<n;++i)
    {
        char temp[500];
        fin>>temp;
        sim(temp);
        fout<<"Case #"<<i+1<<": "<<check()<<endl;
    }
    return 0;
}
