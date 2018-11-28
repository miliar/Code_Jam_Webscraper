#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>

#define SIZE 105

using namespace std;

int n;

string in1("zqejp mysljylc kd kxveddknmc re jsicpdrysi");
string in2("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
string in3("de kr kd eoya kw aej tysr re ujdr lkgc jv");

string out1("qzour language is impossible to understand");
string out2("there are twenty six factorial possibilities");
string out3("so it is okay if you want to just give up");

char input[SIZE];
char c[2];


int main(){
  c[1]='\0';
  scanf("%d\n",&n);
  for(int ccase = 1;ccase <= n; ccase++){
    printf("Case #%d: ",ccase);
    cin.getline(input,SIZE);
    int len = strlen(input);
    for(int index = 0; index < len; index++){
      if(input[index]=='\n'){
        continue;
      }
      c[0] = input[index];
      string cur(c);

      //Str1
      int found = in1.find(cur);
      if(found != string::npos){
        //printf("\n%d in str1\n");
        cout << out1.at(found);
        continue;
      }
      //Str2
      found = in2.find(cur);
      if(found != string::npos){
        //printf("\n%d in str2\n");
        cout << out2.at(found);
        continue;
      }
      //Str3
      found = in3.find(cur);
      if(found != string::npos){
        //printf("\n%d in str3\n");
        cout << out3.at(found);
        continue;
      }
      //printf("ERROR:%s\n",c);
    }
    //if(ccase!=n){
      printf("\n");
    //}
  }
  return 0;
}
