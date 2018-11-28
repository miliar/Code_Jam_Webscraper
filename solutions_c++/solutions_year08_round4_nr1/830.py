#include "utils.h"

int M, V;

struct node{
  int leaf;
  int val;
  int gate;
  int cable;
  int li;
  int ri;
};

vector<node> tree;

void EvalNode(int i) {
  node &n = tree[i];
  if (!n.leaf) {
    if (n.gate) // AND
      n.val = tree[n.li].val && tree[n.ri].val;
    else
      n.val = tree[n.li].val || tree[n.ri].val;
  }
}

void EvalTree() {
  for(int j = M - 1; j >= 0; j--) {
    EvalNode(j);
  }
}

int RunTCaseSub(int i, int dv) {
  int result = 0;

  //  printf("i = %d, dv = %d.\n", i, dv);

  if (tree[i].val == dv)
    return result;
  
  if (tree[i].leaf)
    if (tree[i].val == dv)
      return 0;
    else
      return -1;

  if (dv) { // want a 1
    if (tree[i].cable && tree[i].gate) {  // change and to or
      tree[i].gate = 0;
      result++;
      //      EvalNode(i);
      //      printf("debug -- changing %d from and to or.\n", i);
    }
    int ld = RunTCaseSub(2 * i, 1);
    int rd = RunTCaseSub(2 * i + 1, 1);
    if (tree[i].gate) { // AND 
      if ((ld == -1) || (rd == -1))
	return -1;
      else
	return result + ld + rd;
    } else {  // OR
      if ((ld == -1) && (rd == -1))
	return -1;
      else {
	if (ld == -1)
	  return result + rd;
	if (rd == -1)
	  return result + ld;
	return result + min(ld, rd);
      }
    }
  } else {  // want 0
    if (tree[i].cable && !tree[i].gate) {  // change or to and
      tree[i].gate = 1;
      result++;
      //      printf("debug -- changing %d from or to and.\n", i);
      //      EvalNode(i);
    }
    int ld = RunTCaseSub(2 * i, 0);
    int rd = RunTCaseSub(2 * i + 1, 0);
    if (tree[i].gate) { // AND 
      if ((ld == -1) && (rd == -1))
	return -1;
      else {
	if (ld == -1)
	  return result + rd;
	if (rd == -1)
	  return result + ld;
	return result + min(ld, rd);
      }
    } else {  // OR
      if ((ld == -1) || (rd == -1))
	return -1;
      else
	return result + ld + rd;
    }
  }
}

void PrintTree() {
  for(uint i = 1; i < tree.SZ; i++) {
    printf("tree[%d]:  val = %d, leaf = %d, li = %d, ri = %d.\n", i, tree[i].val, tree[i].leaf, tree[i].li, tree[i].ri);
  }
}

void RunTCase(int n) {
  int result = 0;

  EvalTree();
  //  PrintTree();

  result = RunTCaseSub(1, V);

  if (result >= 0)
    printf("Case #%d: %d\n", n, result); 
  else
    printf("Case #%d: IMPOSSIBLE\n", n);
}

void GetInputs() {
  fscanf(ifile, "%d", &N);
  for(int i = 0; i < N; i++) {
    fscanf(ifile, "%d %d", &M, &V);
    tree = vector<node>(1);
    for(int j = 1; j <= (M - 1) / 2; j++) {
      node n;
      n.leaf = 0;
      fscanf(ifile, "%d %d", &n.gate, &n.cable);
      n.li = 2 * j;
      n.ri = 2 * j + 1;
      tree.PB(n);
    }

    for(int j = 1; j <= (M + 1) / 2; j++) {
      node n;
      n.leaf = 1;
      fscanf(ifile, "%d", &n.val);
      tree.PB(n);
    }

    RunTCase(i + 1);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();

  fclose(ifile);
}
