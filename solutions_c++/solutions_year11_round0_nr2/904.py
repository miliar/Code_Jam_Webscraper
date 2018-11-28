#include <iostream>
#include <cstdio>
#include <string>
#include <set>
#include <map>
using namespace std;
int combine[26][26];
bool check(set<char>&oppose,map<char,int>&input,char a){
    set<char>::iterator it=oppose.begin();
    while(it!=oppose.end()){
        if(input[*it]!=0)
            return true;
        ++it;
    }
    return false;
}
int main()
{
    //cout<<"here\n";
    freopen("B-large.in","r",stdin);
    freopen("Blarge.txt","w",stdout);
    int t;

    int kase=0;
    cin>>t;
    while(t--){
        //cout<<kase<<endl;
        for(int i=0;i<26;++i)
            for(int j=0;j<26;++j){
                combine[i][j]=-1;
                //oppose[i][j]=0;
            }
        int c,d,n;
        string a;
        set<char>oppose[26];
        map<char,int>input;
        cin>>c;
        for(int i=0;i<c;++i){
            cin>>a;
            combine[a[0]-'A'][a[1]-'A']=a[2]-'A';
            combine[a[1]-'A'][a[0]-'A']=a[2]-'A';
        }
        cin>>d;
        for(int i=0;i<d;++i){
            cin>>a;
            oppose[a[0]-'A'].insert(a[1]);
            oppose[a[1]-'A'].insert(a[0]);
        }
        cin>>n;
        cin>>a;
        char st[1000];
        int top=0;
        //st[top++]=a[0];
        for(int i=0;i<n;++i){
            //printf("%c\n",a[i]);
            if(top==0){
                st[top++]=a[i];
                input[a[i]]++;
                continue;
            }
            if(combine[st[top-1]-'A'][a[i]-'A']!=-1){
                input[st[top-1]]--;
                st[top-1]=combine[st[top-1]-'A'][a[i]-'A']+'A';
                input[st[top-1]]++;

            }
            else if(check(oppose[a[i]-'A'],input,a[i])){
                input.clear();
                top=0;

            }
            else{
                st[top++]=a[i];
                input[a[i]]++;
            }
        }
        ++kase;
        printf("Case #%d: [",kase);
        for(int k=0;k<top;++k){
            printf("%c",st[k]);
            if(k!=top-1)  printf(", ");
        }
        printf("]\n");

    }

return 0;
}
