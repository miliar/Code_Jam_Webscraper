#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <vector>
#include <sstream>
#include <string.h>
#include <unistd.h>
#include <map>

using namespace std;

int main(int argc, char *argv[]){


    freopen("A-small-attempt5.in","r",stdin);
    FILE *in=fopen("input.txt","r");
    freopen("output5.txt","w",stdout);
    //freopen("out.txt","r",stdin);
    //freopen("input.txt","w",stdout);
    map<char,char>trans;
    map<char,char>::iterator it;

    char s,d;
    while(s!='z'){
        fscanf(in,"%c %c\n",&s,&d);
        trans[s]=d;
    }
    trans['z']='q';

    /*
    int i,k,m;
    for(i=0;i<3;i++){
        string s1;
        string s2;
        getline(cin,s1);
        getline(cin,s2);
        for(k=0;k<s1.length();k++){
            if(s1[k]==' ')
                continue;
            trans[s1[k]]=s2[k];
        }

    }

    for(it=trans.begin();it!=trans.end();it++){
        if(islower(it->first))
            cout<<it->first<<" "<<it->second<<endl;
    }
    */
    int num;
    while(cin>>num){
        cin.ignore('\n',10);
        int i,k,m;
        char c;
        for(i=0;i<num;i++){
            printf("Case #%d: ",i+1);
            c=getchar();
            while(c!='\n'){
                if(islower(c))
                    cout<<trans[c];
                else if(c==' ')
                    cout<<' ';
                c=getchar();
            }
            cout<<endl;
            //string s2;
            //getline(cin,s2);
            /*
            for(k=0;k<s1.length();k++){
                trans[s1[k]]=s2[k];
            }
            */
        }
    }
    fclose(in);
    /*
    trans['z']='q';
    for(it=trans.begin();it!=trans.end();it++){
        if(islower(it->first))
            cout<<it->first<<" "<<it->second<<endl;
    }
    */



    return 0;
}

