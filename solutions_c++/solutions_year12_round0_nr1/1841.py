#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

int cnt,T;
string sp[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string an[3]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
string in,out;
int map[26];

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    memset(map,0,sizeof(map));
    map['y'-'a']='a';map['e'-'a']='o';map['q'-'a']='z';cnt=3;
    for (int i=0;i<3;i++) 
        for (int j=0;j<sp[i].length();j++) 
            if ((sp[i][j]!=' ')&&(map[sp[i][j]-'a']==0)) {
               cnt++;
               map[sp[i][j]-'a']=an[i][j];
            }
    int temp=('a'+'z')*13,pos;
    for (int i=0;i<26;i++) if (map[i]==0) pos=i; else temp-=map[i];
    map[pos]=temp;
    scanf("%d\n",&T);cnt=0;
    while (T--) {
          in.clear();out.clear();cnt++;
          getline(cin,in);
          for (int i=0;i<in.length();i++) if (in[i]==' ') out+=' ';else out+=char(map[in[i]-'a']);
          cout<<"Case #"<<cnt<<": "<<out<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
