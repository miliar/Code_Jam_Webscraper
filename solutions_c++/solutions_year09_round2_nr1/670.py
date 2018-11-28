#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<set>
using namespace std;
set<string> ss;
int tc,nlines,depth,ndepth[500];
double dtree[500];
string ctree[500];
char s[500][500];

double convert(string st){
double a = 0;
  for (int i = st.length()-1; i >= 0; i--){
      a = a / (double)10 + (st[i]-'0')/(double)10;
  }      
return a;
}

double trace(int place){
      if (ctree[place] == "") {return dtree[place];} 
      if (ss.find(ctree[place]) == ss.end()) {return dtree[place]*trace(place*2+1);} 
      return dtree[place] * trace(place*2);
}

int main(){
  scanf("%d\n",&tc);
  for (int ti = 1; ti <= tc; ti++){
      scanf("%d\n",&nlines);
      ss.clear();
      for (int i = 0; i < 500; i++) dtree[i] = 0;
      for (int i = 0; i < 500; i++) ctree[i] = "";
      string dt;
      depth = 0; 

      memset(ndepth,0,sizeof(ndepth));
      for (int i = 0; i < nlines; i++){
          gets(s[i]);
          int bil;bool dot;
          
          for (int j = 0; s[i][j]; j++){
              if (s[i][j] == ' '){
                     if (dot){
                             dtree[(1<<(depth-1))+ndepth[depth]-1] += convert(dt);
                             dot = false; dt = "";
                     }                          
                     continue;
              }
              
              if (s[i][j] == '('){
                  bil = 0; dot = false; 
                  depth++; dt= "";
                  if ((depth != 1) && (ndepth[depth] == 0))   ndepth[depth] = (ndepth[depth-1]-1)*2;
                  ndepth[depth]++; continue;
              }    
              if (s[i][j] == ')'){
                  if (dot){
                             dtree[(1<<(depth-1))+ndepth[depth]-1] += convert(dt);                           
                             dot = false; dt = "";
                  }                          
                  dot = false; depth--; continue;            
              }
              if (s[i][j] == '.'){
                 dot = true;            
                 continue;
              }
              if ((!dot) && (s[i][j] >= '0') && (s[i][j] <= '9')){
                         bil = bil * 10 + s[i][j]-'0';
                         dtree[(1<<(depth-1))+ndepth[depth]-1] = bil;
                         continue;
              }
              if ((dot) && (s[i][j] >= '0') && (s[i][j] <= '9')){
                        dt += s[i][j];          
              }
              if ((s[i][j] < '0') || (s[i][j] > '9')){
                     if (dot){
                             dtree[(1<<(depth-1))+ndepth[depth]-1] += convert(dt);                              
                             dot = false; dt = "";
                     }
                     ctree[(1<<(depth-1))+ndepth[depth]-1] += s[i][j];
              }
          }         
      }    

      char name[500];
      int m,n;
      printf("Case #%d:\n",ti);
      scanf("%d\n",&n);
      for (int i = 1; i <= n; i++){
          scanf("%s %d",&name,&m);
          ss.clear();
          for (int j = 1; j <= m; j++){
              scanf("%s",&s[j]);
              ss.insert((string)s[j]);    
          }
          scanf("\n");
          printf("%.7lf\n",trace(1));
      }
  }   
}
