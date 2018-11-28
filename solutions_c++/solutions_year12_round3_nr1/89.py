#include <cstdio>
#include <set>
#include <vector>

using namespace std;
int main(){
int ncas;
scanf("%d",&ncas);
for(int cc=1;cc<=ncas;cc++){

int n;
scanf("%d",&n);
vector<vector<int> > inherits;
inherits.resize(n);
int j,l;
for(int i=0;i<n;i++){ scanf("%d",&j);for(int k=0;k<j;k++){scanf("%d",&l);inherits[i].push_back(l-1);} }
bool apriori = false;
for(int i=0;i<n && !apriori ;i++){
vector<int> todo;todo.push_back(i);
set<int> inh;


while(!todo.empty() && !apriori){ 
j=todo[todo.size()-1];// printf("%d %d\n",i,j);
todo.pop_back();
for(int k=0;k<inherits[j].size();k++){ if(!inh.insert(inherits[j][k]).second){ apriori=true;/*fini*/}else todo.push_back(inherits[j][k]); }
}
}

printf("Case #%d: ",cc);
if(apriori)printf("Yes\n"); else printf("No\n");

}
return 0;

}
