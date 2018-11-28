#include <cstdio>
#include <vector>
#include <map>
#include <cstring>
using namespace std;

typedef pair<char,char> cc;

int T,C,D,N;
char spels[128];
char str[16];
char last;
map<cc,char> transform;
map<char,char> opposed;
vector<char> elements;
int inlist[32];


int main(){

  scanf("%d",&T);
  for(int t=0;t<T;t++){
    transform.clear();
    opposed.clear();
    elements.clear();
    memset(inlist,0,sizeof(inlist));

    // two base combined AB->C
    scanf("%d",&C);
    for(int c=0;c<C;c++){
      scanf("%s",str);
      transform[cc(str[0],str[1])]=str[2];
      transform[cc(str[1],str[0])]=str[2];
    }

    // opposed elements A<->B
    scanf("%d",&D);
    for(int d=0;d<D;d++){
      scanf("%s",str);
      opposed[str[0]]=str[1];
      opposed[str[1]]=str[0];
    }

    scanf("%d",&N);
    scanf("%s",spels);

    for(int i=0;i<N;i++){
      if((int)elements.size()>0){
        last = elements[(int)elements.size()-1];
        if(transform.find(cc(last,spels[i]))!=transform.end()){
          elements.pop_back();
          elements.push_back(transform[cc(last,spels[i])]);
          inlist[last-'A']--;
          inlist[transform[cc(last,spels[i])]-'A']++;
        } else {
          // check if no opposed element
          if(opposed.find(spels[i])!=opposed.end() and
             inlist[opposed[spels[i]]-'A']!=0){
            elements.clear();
            memset(inlist,0,sizeof(inlist));
          } else {
            elements.push_back(spels[i]);
            inlist[spels[i]-'A']++;
          }
        }
      } else {
        elements.push_back(spels[i]);
        inlist[spels[i]-'A']++;
      }
    }

    printf("Case #%d: [",t+1);
    if((int)elements.size()>0)
      printf("%c",elements[0]);
    for(int i=1;i<(int)elements.size();i++)
      printf(", %c",elements[i]);
    printf("]\n");
  }

  return 0;
}
