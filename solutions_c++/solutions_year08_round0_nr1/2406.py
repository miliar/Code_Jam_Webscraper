#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

int main(){
int n;
scanf("%d\n",&n);
for(int j=0;j<n;j++){
int s,q;
scanf("%d\n",&s);
string inp;
set<string> eng,que;
for(int i=0;i<s;i++){
getline(cin,inp);
eng.insert(inp);
}

scanf("%d\n",&q);
int sw=0;
//cout<<q<<endl;

for(int i=0;i<q;i++){
getline(cin,inp);
//cout<<inp<<' '<<i<<endl;
que.insert(inp);

//cout<<que.size()<<' '<<sw<<endl;
if(que.size()==s){
sw++;
que.clear();
que.insert(inp);
}
}


cout<<"Case #"<<j+1<<": "<<sw<<endl;
}
return 0;
}
