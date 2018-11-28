#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<fstream>
using namespace std;

char Map[27]={0};

void init(){
    const char *s1[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    const char *s2[]={"our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"};
    for(int i=0;i<3;i++){
        int len = strlen(s1[i]);
        for(int j=0;j<len;j++){
            if(s1[i][j]!=' '){
                Map[s1[i][j]-'a'] =s2[i][j];
            }
        }
    }
    Map['z'-'a']='q';
    Map['q'-'a']='z';
    return;
}




int main(int argc,char *argv[]){
    init();
    int T,l;
    scanf("%d",&T);
    getchar();
    ofstream f;
    f.open("D:/out.in");
    //char str[110];
    string str;
    for(int i=1;i<=T;i++){
        getline(cin,str);
        printf("Case #%d: ",i);
        f<<"Case #"<<i<<": ";
        l = str.length();
        for(int j=0;j<l;j++){
            if(str[j]==' '){
                printf(" ");
                f<<" ";
            }

            else{
                printf("%c",Map[str[j]-'a']);
                f<<Map[str[j]-'a'];
            }

        }
        printf("\n");
        f<<endl;
    }
    f.close();

}
