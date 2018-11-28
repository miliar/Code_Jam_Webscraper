#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
map<int,char> itc;
map<char,int> cti;

int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int t;
    cin>>t;
    for(int i=0;i<26;i++)
    {
            itc[i]=i+'A';
            cti[i+'A']=i;
    }
    for(int j=1;j<=t;j++){
        int combine[26][26];
        int oppose[26][26];
        for(int p=0;p<26;p++){
        for(int q=0;q<26;q++){
                combine[p][q]=-1;
                oppose[p][q]=0;
        }
        }
        int c;
        cin>>c;
        for(int i=0;i<c;i++)
        {
                string tem;
                cin>>tem;
                combine[cti[tem[0]]][cti[tem[1]]]=cti[tem[2]];
                combine[cti[tem[1]]][cti[tem[0]]]=cti[tem[2]];
        }
        cin>>c;
        for(int i=0;i<c;i++)
        {
                string tem;
                cin>>tem;
                oppose[cti[tem[0]]][cti[tem[1]]]=1;
                oppose[cti[tem[1]]][cti[tem[0]]]=1;
        }
        char invoke[100];
        int start=0;
        int n;string s;
        cin>>n>>s;
        for(int i=0;i<n;i++)
        {
                if(start==0){invoke[start]=s[i];start++;continue;}
                if(combine[cti[invoke[start-1]]][cti[s[i]]]!=-1)
                {
                   invoke[start-1]=itc[combine[cti[invoke[start-1]]][cti[s[i]]]];
                   continue;
                }
                bool flag=false;
                for(int k=0;k<start;k++)
                {
                        if(oppose[cti[invoke[k]]][cti[s[i]]]==1)
                        {
                           start=0;
                           flag=true;
                           break;
                        }
                }
                if(flag==false){invoke[start]=s[i];start++;}
        }
        cout<<"Case #"<<j<<": [";
        if(start==0){cout<<"]"<<endl;continue;}
        for(int i=0;i<start;i++)
        {
                if(i==start-1){cout<<invoke[i]<<"]"<<endl;}
                else{cout<<invoke[i]<<", ";}
        }
    }
}
        
        
