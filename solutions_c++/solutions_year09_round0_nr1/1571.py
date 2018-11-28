
#include <stdio.h>
#include <malloc.h>

int L,N,D;
char *letter[20];
int numchars[20];


typedef struct _t_node {
  
  int spot;
  struct _t_node * child[26];

} t_node;


t_node * newNode() {
  
  t_node * node = (t_node *) malloc(sizeof(t_node));
  
  node->spot = 0;
  for (int i = 0; i < 26; i++)
    node->child[i] = NULL;
  
}


int count(t_node * pt, int level) {
  
  int total = 0;
  if (pt == NULL) return 0;
  if (pt->spot == 1) {
    return 1;
  }
  if (level == L) return 0;
  
  for (int i =0; i < numchars[level]; i++) {
    
    char c = letter[level][i];
    int idx = (int) (c - 'a');
    if (pt->child[idx] != NULL) {
      total += count(pt->child[idx],level+1);
    }
  }
  
  
  return total;
}


main() {



  
  char c;
  char line[900];


  for (int l = 0; l < 20; l++) {
    letter[l] = (char *) malloc(30);
  }

  t_node * root = newNode();
  
  scanf("%d %d %d", &L, &D, &N);

  for (int word = 0; word < D; word++) {

    // now read the letters of the word; There are L of them;

    t_node * pt = root;
    
    scanf("%s",line);
    
    for (int l = 1; l <= L; l++) {

      c = line[l-1];
      
      int idx = (int) ( c - 'a');
      if (pt->child[idx] == NULL) 
	pt->child[idx] = newNode();
      pt = pt->child[idx];
      
    }
    pt->spot = 1;
  }
  
  for (int word = 1; word <= N; word++) {
    // These are the test cases;

    scanf("%s",line);
    int pos = 0;
    printf("Case #%d: ",word);
    
    for (int l = 0; l < L; l++) {
      
      int numread = 0;
      if (line[pos] == '(') {
	pos++;
	while (line[pos] != ')') {
	  letter[l][numread] = line[pos];
	  numread++;
	  pos++;
	}
	pos++;
      }
      else {
	letter[l][numread] = line[pos];
	numread = 1;
	pos++;
      }
      letter[l][numread] = 0;
      numchars[l] = numread;
      

    }

    // check:
    
    printf("%d\n",count(root,0));

    
  }


}


