#include<cstdio>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;

int mcase;
char conv[256];

int main(){
    scanf("%d\n",&mcase);
    char* mstr= "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv zq";
    char* tstr= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up qz";
    for(int i=0;mstr[i] != '\0';i++){
        conv[mstr[i]]=tstr[i];
    }
    //vector<pair<char,char> > v;
    //for(char c='a';c<='z';c++){
    //    v.push_back( make_pair(conv[c],c) );
    //    //printf("%c->%c\n",c,conv[c]);
    //}
    //sort(v.begin(),v.end());
    //for(int i=0;i<v.size();i++){
    //    printf("%c->%c\n",v[i].second,v[i].first);
    //}

    for(int ncase=0;ncase<mcase;ncase++){
        char str[256];
        gets(str);
        printf("Case #%d: ",ncase+1);
        char *pt = str;
        while(*pt != '\0'){
            putchar(conv[*pt]);
            pt++;
        }
        puts("");
    }
}
