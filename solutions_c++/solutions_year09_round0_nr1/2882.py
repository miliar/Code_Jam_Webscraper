#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int main(){
    int l,d,n;
    char str[1000];
    vector<string> words;
    string s;
    scanf("%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++){
        scanf(" %s",str);
        s=str;
        words.push_back(s);
    }


    for(int i=0;i<n;i++){
        vector< string > posChars;
        scanf(" %s",str);
        s = str;
        int len = s.length();
        for(int j=0;j<len;){
            string temp = "";
            if(s[j] =='('){
                j++;
                while(s[j]!=')'){
                    temp = temp + s[j];
                    j++;
                }
                j++;
                posChars.push_back(temp);
            }
            else {
                temp = temp + s[j];
                j++;
                posChars.push_back(temp);
            }
        }

        int ans = 0;
        for(int j=0;j<d;j++){
            bool flag = true;
            for(int k=0;k<l;k++){
                char ch = words[j][k];
                string::size_type loc = posChars[k].find(ch, 0);
                if(loc == string::npos){
                    flag = false;
                    break;
                }
            }
            if(flag)ans++;
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
