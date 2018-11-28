#include <iostream>
using namespace std;

char interpret(char* interpreter, char c);
bool genInterpreter(char* interpreter);

int main(){
        int numCases;
        char c, line[101];
        char interpreter[26];
        genInterpreter(interpreter);

        cin>>numCases;
        cin.getline(line, 101);
        for(int i=0; i<numCases; i++){
                cout<<"Case #"<<i+1<<": ";
                cin.getline(line, 101);
                int k=0;
                while (k<100){
                        c=line[k++];
                        if(c=='\n'|| c=='\0')
                                break;
                        if(c==' ')
                                cout<<c;
                        else
                                cout<< interpret(interpreter, c);
                }
                cout<<endl;
        }
}

bool genInterpreter(char* interpreter){
        for(int i=0; i<26; i++){
                interpreter[i]='A';
        }

        const char* code[3];
        code[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
        code[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
        code[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
        const char* text[3];
        text[0]="our language is impossible to understand";
        text[1]="there are twenty six factorial possibilities";
        text[2]="so it is okay if you want to just give up";

        for(int i=0; i<3; i++){
                int k=0;
                while(code[i][k]!='\0'){
                        interpreter[code[i][k]-'a']=text[i][k];
                        k++;
                }
        }
        interpreter['y'-'a']='a';
        interpreter['e'-'a']='o';
        interpreter['q'-'a']='z';

        int unmatched=0, unmatchIdx=-1;
        int mappedChar[26];
        for(int i=0; i<26; i++){
                if(interpreter[i]=='A'){
                        unmatched++;
                        unmatchIdx=i;
                }else{
                        mappedChar[interpreter[i]-'a']=1;
                }
        }
        if(unmatched>1){
                return false;
        }
        for( int i=0; i< 26; i++){
                if(mappedChar[i]!=1)
                        interpreter[unmatchIdx]='a'+i;
        }
        return true;
}

char interpret(char* interpreter, char c){
        return interpreter[c-'a'];
}
