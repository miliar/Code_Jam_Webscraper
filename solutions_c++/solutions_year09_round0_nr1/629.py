#include<cstdio>
#include<cstring>
int len,nwords,nquery;
char words[6000][50];
char query[6000];
bool hash[6000];
bool tr[6000];

int main(){
  scanf("%d %d %d\n",&len, &nwords, &nquery);
  for (int i = 0; i < nwords; i++){
      gets(words[i]);    
  }   

  for (int i = 0; i < nquery; i++){
      gets(query);
      int inhash = 0;
      int lenq = strlen(query)-1;
      long long res = 0;
      bool choice = false;
      int hurufke = 0;
      
      memset(tr,true,sizeof(tr));
      for (int j = 0;query[j]; j++){
          if (query[j] == '('){
               choice = true;
               memset(hash,0,sizeof(hash));
               continue;
          }
          else if (query[j] == ')') {
               choice = false;
               for (int k = 0; k < nwords; k++){
                   if (!hash[words[k][hurufke]-'a']) {
                                                     tr[k] = false;
                   }
               }
               //process
               hurufke++;
               continue;
          }
          if (choice) hash[query[j]-'a'] = true;
          else{
               for (int k = 0; k < nwords; k++){
                   if (words[k][hurufke]!= query[j]) {
                                           tr[k] = false;
                   }
               }
               //process
               hurufke++;
          }
      }
      for (int j = 0; j < nwords; j++){
          if (tr[j]) res++;    
      }
      printf("Case #%d: %I64d\n",i+1,res);      
  }

}
