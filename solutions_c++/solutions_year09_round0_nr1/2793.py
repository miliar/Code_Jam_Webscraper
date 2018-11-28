#include <iostream>
#include <string>
using namespace std;

void process_str(string &out, string str){
    int j=0;
    int in=0;
    for(int i=0;i<str.length();++i){
        if(str[i]=='('){
            out += '(';
            in = 1;
        }
        else if(str[i]==')'){
            out += ')';
            in = 0;
        }
        else{
            if(in==0){
                out += '(';
                out += str[i];
                out += ')';
            }
            else
                out += str[i];
        }
    }
    out += '\0';
    return;
}

int main(void){
    int l, d, n;
    string s[5000];
    string str1;
    string s2[15];
    
    cin >> l >> d >> n;
    for(int i=0;i<d;++i)
        cin >> s[i];
    for(int i=0;i<n;++i){
        cin >> str1;
        string str;
        process_str(str, str1);
        char *pch;
        char tmp[30*15];
        strcpy(tmp, str.data());
        int j=0;
        pch = strtok(tmp, "()");
        while (pch != NULL)
        {
            s2[j++] = pch;
            pch = strtok(NULL, "()");
        }
        
        cout << "Case #"<< i+1 <<": ";
        int ans = 0;
        for(int k=0;k<d;++k){
            int t;
            for(t=0;t<l;++t){
                size_t found = s2[t].find(s[k][t]);
                if(found==string::npos)
                    break;
            }
            if(t==l)
                ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
