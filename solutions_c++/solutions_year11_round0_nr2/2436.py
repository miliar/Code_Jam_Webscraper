#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<map>
#include<string>
#include<iostream>
#include<vector>
using namespace std;

int opp[100][100];
char com[100][100];
char op[100],co[100];
string line="",out="";
int main(){
        int t,c,d,n,cnt=1;
        scanf("%d", &t);
        while(t--){
                out = "";
                line= "";
                memset(opp,0,sizeof(opp));
                memset(com,0,sizeof(com));
                scanf("%d", &c);
                while(c--){
                        scanf("%s", co);
                        com[co[0]-'A'][co[1]-'A'] = com[co[1]-'A'][co[0]-'A'] = co[2];
                }
                scanf("%d", &d);
                while(d--){
                        scanf("%s", op);
                        opp[op[1]-'A'][op[0]-'A'] = opp[op[0]-'A'][op[1]-'A'] = 1;
                }
                scanf("%d", &n);
                cin >> line;
                out+= line[0];
                for(int i=1; i<n;i++){
                        int l = out.length();
                        if(com[line[i]-'A'][out[l-1]-'A']!=0){
                                out[l-1]= com[line[i]-'A'][out[l-1]-'A'];
                                continue;
                        }
                        int s = 0;
                        for(int j=0; j<out.length(); j++)
                                if(opp[out[j]-'A'][line[i]-'A']) {s=1; break;}

                        if(s)out="";
                        else {out+= line[i];}
                }
                printf("Case #%d: ",cnt++);
                cout << '[' << out[0];
                for(int i=1; i<out.length();i++){
                        cout<<", " <<out[i];
                }
                cout<<']'<<endl;
        }
        return 0;
}
