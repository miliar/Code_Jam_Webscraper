#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<string>
#include<set>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    for(int cs=0;cs<t;cs++){
        int k;
        char s[1000];
        string str="";
        scanf("%d",&k);
        scanf(" %s",s);
        str=s;
        vector<int> perm;
        for(int i=0;i<k;i++)
            perm.push_back(i);
        int min=1000000;
        do{
            int cnt=1;
            string news="";
            for(int i=0;i<str.length();i+=k){
                string temp="";
                string ntemp="";
                for(int j=i;j<i+k;j++)
                    temp=temp+str[j];
                for(int j=0;j<k;j++)
                    ntemp=ntemp+temp[perm[j]];
                news=news+ntemp;
            }
            for(int i=1;i<news.length();i++)
                if(news[i]!=news[i-1])cnt++;
            if(min>cnt)min=cnt;
        }while(next_permutation(perm.begin(),perm.end()));
        printf("Case #%d: %d\n",cs+1,min);
    }
    return 0;
}
