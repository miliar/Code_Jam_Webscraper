#include<stdio.h>
#include<map>
using namespace std;

char * m[]={"  ","ay","bh","ce","ds","eo","fc","gv","hx","id","ju","ki","lg","ml","nb","ok","pr","rt","sn","tw","uj","vp","wf","xm","ya","qz","zq"};
map<char,char> Map;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cnt=0;
    char c;
    for(int i=0;i<27;i++){
        Map[m[i][0]]=m[i][1];
    }
    scanf("%d",&cases);
    getchar();
    while(cases--){
        printf("Case #%d: ",++cnt);
        while(true){
            c=getchar();
            if(c=='\n'){
                putchar(c);
                break;
            }
            putchar(Map[c]);
        }
    }
    return 0;
}
