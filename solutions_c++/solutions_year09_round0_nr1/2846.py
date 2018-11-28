#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;
int main(){
    int l,d,n;
    cin>>l>>d>>n;
    vector<string> dictionary;
    while(d){
        string tmp;
        cin>>tmp;
        dictionary.push_back(tmp);
        d--;
    }
    int map[l][26];
    for(int k=1;k<=n;k++){
        string pattern;
        int count=0;
        cin>>pattern;
        for(int i=0;i<l;i++)
            for(int j=0;j<26;j++)
                map[i][j]=0;
     /*   for(int i=0;i<l;cout<<endl, i++)
            for(int j=0;j<26;j++)
                cout<<map[i][j];*/
        int tmp=0;
        for(int i=0;i<l;i++)
        {
            if(pattern[tmp]=='('){
                while(pattern[++tmp]!=')'){
                    map[i][pattern[tmp]-'a']=1;
                }
                tmp++;
            }
            else
            {
                map[i][pattern[tmp]-'a']=1;
                tmp++;
            }
            //if(map[0]['v'-'a']==1)cout<<"BUGGY!";
        }
        //DEBUG:
       /* for(int i=0;i<l;cout<<endl, i++)
            for(int j=0;j<26;j++)
                cout<<map[i][j];
*/
        for(int i=0;i<dictionary.size();i++){
            int flag=1,j=0;
            while(flag&&j<l){
                if(!map[j][dictionary[i][j]-'a'])
                    flag=0;
                j++;
            }
            if(flag)
                count++;
        }
        cout<<"Case #"<<k<<": "<<count<<endl;
    }

    return 0;
}
