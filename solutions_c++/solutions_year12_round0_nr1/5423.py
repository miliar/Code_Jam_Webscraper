#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    long i,j,len,test,order;
    char gs[205];//,vstd[300]={0};
    string str[3][2];
    char ch[305];
    ch['q']='z';
    ch['z']='q';
    str[0][0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    str[0][1]="our language is impossible to understand";
    str[1][0]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    str[1][1]="there are twenty six factorial possibilities";
    str[2][0]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str[2][1]="so it is okay if you want to just give up";
    for(i=0;i<3;i++){
        len=str[i][0].size();
        for(j=0;j<len;j++){ 
            ch[str[i][0][j]]=str[i][1][j];
        }
    }
    cin>>test;
    getchar();
    for(order=1;order<=test;order++){
        //printf("order %ld\n",order);
        cout<<"Case #"<<order<<": ";
        gets(gs);
        len=strlen(gs);
        for(i=0;i<len;i++)
            cout<<ch[gs[i]];
        cout<<endl;
    }
    return 0;
}
