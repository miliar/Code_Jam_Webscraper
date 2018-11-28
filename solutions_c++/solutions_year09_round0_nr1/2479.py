#include <iostream>
using namespace std;

class pattern{
        public:
            char str[800];
            int len;
            char* patterns[20];
        pattern(char* s){
            strcpy(str,s);
            len=strlen(s);
            int j=0,status=0;
            for(int i=0;i<len;++i){
                if(str[i]!='('&&status==0){
                    patterns[j++]=str+i;
                    continue;
                }
                if(str[i]!='('&&status==1){
                    patterns[j++]=str+i;
                    status=2;
                    continue;
                }
                if(str[i]=='('){
                    status=1;
                    continue;
                }
                if(str[i]==')'){
                    status=0;
                }
            }
        }
        bool check(char str[]){
            int i=0;
            while(str[i]!='\0'){
                if(!checkpattern(str[i],i))return false;
                ++i;
            }
            return true;
        }
        bool checkpattern(char c,int i){
            int j=0;
            while(patterns[i][j]!=')'&&patterns[i][j]!='('){
                if(c==patterns[i][j])return true;
                ++j;
            }
            return false;
        }
};

int main(){
    int L=0,D=0,N=0;
    cin>>L>>D>>N;
    char** str;
    str=new char*[D];
    for(int i=0;i<D;++i){
        str[i]=new char[L+1];
        cin>>str[i];
    }
    for(int i=0;i<N;++i){
        int count=0;
        char pat[800];
        cin>>pat;
        pattern p(pat);
        for(int j=0;j<D;++j){
            if(p.check(str[j]))++count;
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
