#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>

using namespace std;

const char input1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
const char input2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const char input3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char *input[]={input1,input2,input3};

const char output1[]="our language is impossible to understand";
const char output2[]="there are twenty six factorial possibilities";
const char output3[]="so it is okay if you want to just give up";
const char *output[]={output1,output2,output3};

char Map[256];
char used[256];

void init(){
    memset(used,0,sizeof(used));
    for(int i = 0 ; i < 3; ++i){
        for(int j = 0 ; j < strlen(input[i]) ; ++j){
            Map[input[i][j]] = output[i][j] ;
            used[output[i][j]] = 1;
        }
    }
    Map['q'] = 'z';
    Map['z'] = 'q';
    used['q'] = 1;
//    Map['a'] = 'y';
//    Map['o'] = 'e';
//    Map['z'] = 'q';
//    used['y'] = 1;
//    used['e']  = 1;
//    used['q']  = 1;
    for(int i = 'a' ; i!='z' + 1 ;++i  ){
        if(used[i] == 0){
            Map['q'] = i;
        }
    }
}

string translate(string & str){
    for(int i = 0; i < str.length() ; ++i){
        str[i] = Map[str[i]];
    }
    return str;
}


int main(){
    init();
    int t;
    cin>>t;
    string str;
    getline(cin,str);
    for(int i = 0 ; i < t ; ++i){
        getline(cin,str);
        cout<<"Case #"<<i+1<<": "<<translate(str)<<endl;
    }
    for(char i = 'a' ; i!='z'+1 ; ++i){
//        cout<<i<<" "<<Map[i]<<" " << used [i] <<" "<< used[Map[i]] <<endl;
    }
}
