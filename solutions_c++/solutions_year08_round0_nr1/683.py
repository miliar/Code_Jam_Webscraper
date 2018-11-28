#include<iostream>
#include<map>
#include<string>
using namespace std;
map <string,int> m;
int S,Q;
char name[1000];
string ename;
int ecount;
bool engine[120];
int switches;
int main()
{
  int t,n;
  scanf("%d",&t);
  for(int i =1;i<=t;i++){
//  printf("\n\nCase %d\n",i);
    ecount =switches=0;
    scanf("%d\n",&S);//fflush(stdin);
    m.clear();
    for(int j=0;j<S;j++){
      getline(cin,ename);
//      ename = name;
      m[ename]=ecount++;
  //    printf("Engine %d : %s\n",m[ename],name);
    }
  //  printf("Accepted Engines...\n");
    scanf("%d\n",&Q);//fflush(stdin);
    memset(engine,0,sizeof(engine));
    for(int j=0;j<Q;j++){
      getline(cin,ename);
//      ename=name;  
      engine[m[ename]]=1;
      bool allseen=1;
      for(int k=0;k<S;k++)
            if(!engine[k]){
              allseen=0;
    //          printf("%s ... Engine number %d not seen\n",name,k);
              break;
            }
      if(allseen){
      //  printf("%s all seen\n",name);
     // printf("%s ... all engines seen\n",name);
        switches++;
        memset(engine,0,sizeof(engine));
        engine[m[ename]]=1;
      }       
    }
    printf("Case #%d: %d\n",i,switches);
  }
}

