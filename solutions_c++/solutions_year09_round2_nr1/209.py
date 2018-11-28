#include <stdio.h>
#include <string.h>

#define NN 110
int read_until(char c){
  while (getc(stdin)!=c);
  return 0;
}

char next_char(){
  char c;
  while (true){
    c = getc(stdin);
    if (c!=' ' && c!='\n')break;
  }
  return c;
}

char gfeature[NN][100];
int nn; 


struct Node{
  Node *left, *right;
  char feature[100];
  double p;

  Node(){
    left=right=NULL;
  }

  double cal(double init){
    if (left==NULL){
      //leaf node
      return init*p;
    }
    bool has_feature=false;
    for (int i=0;i<nn && !has_feature;i++){
      if (strcmp(gfeature[i],feature)==0)has_feature=true;
    }
    if (has_feature){
      return left->cal(init*p);
    }else{
      return right->cal(init*p);
    }
  }

  int read(){
    read_until('(');
    scanf("%lf",&p);
    char c = next_char();
    if (c==')'){
      //leaf node
    }else{
      ungetc(c,stdin); scanf("%s",feature);
      left = new Node();
      left->read();
      right = new Node();
      right->read();
      read_until(')');
    }
  }

};

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int L;
    scanf("%d",&L);
    char s[100];
    int state = 0;
    Node *root = new Node();
    root->read();

    printf("Case #%d:\n",ti);
    int A;
    scanf("%d",&A);
    for (int i=0;i<A;i++){
      char name[100];
      scanf("%s%d",name,&nn);
      for (int j=0;j<nn;j++){
        scanf("%s",gfeature[j]);
      }
      double p = root->cal(1);
      printf("%.7lf\n",p);
    }
  }
  return 0;
}
