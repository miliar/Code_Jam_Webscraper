#include <iostream>
#include <hash_map.h>
#include <queue>

using namespace::std;


int heappoz[1003];
deque<int> lists[101];
struct eqstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) == 0;
  }
};

struct Engine {
  int val;
  int type;  
}heap[1003];

void heapify(int i,int n) {
  int l,r,largest,poz;
  struct Engine tmp;
  l=2*i+1;
  r=2*i+2;

  if((l<n) && (heap[l].val>heap[i].val))
    largest = l;
  else
    largest = i;
  
  if((r<n) && (heap[r].val>heap[largest].val))
    largest = r;

  if(largest !=i) {
    tmp = heap[i];
    
    heap[i] = heap[largest];
    heappoz[heap[largest].type] = i;
    heap[largest] = tmp;
    heappoz[tmp.type] = largest;
    heapify(largest,n);
  }      
}

void build_heap(int n) {
  int i,j;
  for(j=n/2; j>=0;j--)
    heapify(j,n);
}


void heap_increase_key(int type)
{
  int key,i,poz;
  struct Engine e;
  key = lists[type].front();
  lists[type].pop_front();
  
  i = heappoz[type];
  heap[i].val=key;
  while( (i> 0) && (heap[i/2].val<heap[i].val)) {
    e = heap[i];
    heap[i] = heap[i/2];
    heappoz[heap[i/2].type]=i;
    heap[i/2] = e;
    heappoz[e.type]=i/2;
    i = i/2;
  }
}


struct Engine heap_max(int n) {
  struct Engine tmp;
  tmp = heap[0];
  heap[0] = heap[n-1];
  heappoz[heap[n-1].type] = 0;
  heappoz[tmp.type] = n-1;
  heap[n-1] = tmp;
  heapify(0,n-1);
  return tmp;
}

int znajdz(char tab[][102],char *w, int n) {
  int i;
  for(i=0; (i<n)&&strcmp(tab[i], w);i++);
  return i;
}
int main()
{
  hash_map<const char*, int, hash<const char*>, eqstr> engines;
  char wyrazy[102][102];
  struct Engine tmp, my;
  char word[103];
  int n, s, q, i, j, t, l, result;
  int queries[1003];
  scanf("%d",&n);
  for (t = 0; t < n; t++) {
  
    result = 0;
  //  engines.clear();
    scanf("%d\n",&s);
    
    for(l = 0; l < s; l++) {
      fgets(word, 101, stdin);
      strcpy(wyrazy[l],word);
     // engines[word] = l;
    //  printf("%s %d\n",word,engines[word]);
      lists[l].clear();
    }
    
    scanf("%d\n",&q);
    for(l = 0; l < q; l++) {
      fgets(word, 101, stdin);
      j = znajdz(wyrazy,word, s);//engines[word];
      queries[l]=j;
  //    printf("%d\n",j);
      lists[j].push_back(l);
    }
    
    for(l = 0; l < s; l++) {
      lists[l].push_back(100023); //+oo 
      lists[l].push_back(100023);
      tmp.type = l;
      tmp.val = lists[l].front();
      heap[l]=tmp;
      heappoz[l]=l;
      lists[l].pop_front();
    }
    build_heap(s);
/*    printf("kopiec  ");
        for(j=0;j<s;j++)
          printf(" %d ",heap[j].val);
        printf("\n");
        for(j=0;j<s;j++)
          printf("%d ",heappoz[j]);
        printf("\n"); */
    my = heap_max(s);
    heap_increase_key(queries[0]);
//    printf("pocz %d %d\n",my.type,my.val);
    for(i = 1; i < q;i++) {
      if (my.type == queries[i]) {
        result++;
/*        printf("zmiana %d rowne %d kiedy %d\n",result, my.type,my.val);
        printf("kopiec  ");
        for(j=0;j<s;j++)
          printf(" %d  ",heap[j].val);
        printf("\n");
        for(j=0;j<s;j++)
          printf("%d ",heappoz[j]);
        printf("\n"); */
        my = heap_max(s);
      
      }
      heap_increase_key(queries[i]);
    }  
    
    printf("Case #%d: %d\n",t+1,result);
  }
                                     
   return 0;
}
