#include<iostream>
#include<string>
using namespace std;

int main(){
    freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
    int n;
    while(cin >> n){
    for(int k=1; k<=n; ++k){
        string op,oc,str;
        int c;
        cin >> c;
        if(c==1) cin >> oc;
        int d;
        cin >> d;
        if(d==1) cin >> op;
        int w;
        cin >> w;
        cin >> str ;
        cout <<"Case #"<<k<<": ";
        if(c==0 && d==0){
            cout << "[";
            string word;
            for(int i=0; i<w; ++i){
                cout << str[i];
                if(i<w-1) cout << ", ";
            }
            cout << "]" << endl;
        }else if(c==0 && d==1){
            cout << "[";
            string word="";
            for(int i=0; i<w; ++i){
                word+=str[i];
                int flag1=0,flag2=0;
                for(int j=0; j<word.size(); ++j){
                    if(word[j]==op[0]) flag1=1;
                    if(word[j]==op[1]) flag2=1;
                }
                if(flag1 && flag2 ) {
                    word="";
                    flag1=0;
                    flag2=0;
                }
            }
            for(int j=0; j<word.size(); ++j){
                cout << word[j];
                if(j<word.size()-1) cout << ", ";
            }
            cout << "]" << endl;
        }else if(c==1 && d==0){
            cout << "[";
            string word="";
            for(int i=0; i<w;){
                if(i+1<w && ( (str[i]==oc[0] && str[i+1]==oc[1])|| (str[i]==oc[1] && str[i+1]==oc[0]))){
                    word+=oc[2];
                    i+=2;
                }else{
                    word+=str[i];
                    ++i;
                }
            }
            for(int j=0; j<word.size(); ++j){
                cout << word[j];
                if(j<word.size()-1) cout << ", ";
            }
            cout << "]" << endl;
        }else if(c==1 && d==1){
            cout << "[";
           int flag1,flag2;
           string word="";
           for(int i=0; i<w;){
               flag1=0;flag2=0;
               for(int j=0; j<word.size(); ++j){
                    if(word[j]==op[0]) flag1=1;
                    if(word[j]==op[1]) flag2=1;
                }
               if(str[i]==op[0]) flag1=1;
               if(str[i]==op[1]) flag2=1;
                if(flag1 && flag2 ){
                    word="";
//                    flag1=0;
//                    flag2=0;
                    ++i;
                    if(i>=w) break;
                }
               if(i+1<w &&( (str[i]==oc[0] && str[i+1]==oc[1])|| (str[i]==oc[1] && str[i+1]==oc[0]))){
                    word+=oc[2];
                    i+=2;
                }else{
                    word+=str[i];
                    ++i;
                }
            }
           for(int j=0; j<word.size(); ++j){
               cout << word[j];
               if(j<word.size()-1) cout << ", ";
           }
           cout << "]" << endl;
        }
    }
    }
    return 0;
}
