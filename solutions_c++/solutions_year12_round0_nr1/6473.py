#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <sstream>
#include <fstream>

using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	string sc[3][2];
    sc[0][0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    sc[0][1]="our language is impossible to understand";
    sc[1][0]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    sc[1][1]="there are twenty six factorial possibilities";
    sc[2][0]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    sc[2][1]="so it is okay if you want to just give up";

    char tras[30][2];
    for(int i=0;i<30;i++){
        tras[i][0]='*';
        tras[i][1]='*';
    }
//0: g, 1:e
    for(int j=0;j<3;j++){
        for(int i=0;i<(sc[j][0]).size();i++)
            if(sc[j][0][i]!=' '){
                tras[ sc[j][0][i] -'a'][0]=sc[j][0][i];
                tras[ sc[j][0][i] -'a'][1]=sc[j][1][i];
            }
    }
    tras['z'-'a'][0]='z';
    tras['z'-'a'][1]='q';
    tras['q'-'a'][0]='q';
    tras['q'-'a'][1]='z';
/*    for(int i=0;i<30;i++)
        cout<<"goog: "<<tras[i][0]<<"  ,eng: "<<tras[i][1]<<endl;
*/
    int n;
    scanf("%d\n",&n);
    string s;
    int j=0;
    while(n--){
        getline(cin,s);
        int l=s.size();
        cout<<"Case #"<<++j<<": ";
        for(int i=0;i<l;i++){
            if(s[i]!=' ')   cout<<tras[ s[i] -'a'][1];
            else            cout<<s[i];
        }
        cout<<endl;
    }
	return 0;
}
