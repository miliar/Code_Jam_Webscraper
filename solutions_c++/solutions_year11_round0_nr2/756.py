/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 07 May 2011 09:14:11 PM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>

using namespace std;


static int merge_rule[100][3];
static int opps_rule[100][2];
static int seq[200];
static int merge_rule_len = 0;
static int opps_rule_len  = 0;
static int seq_len        = 0;

static void generate_merge_rule(int rule_count)
{
  merge_rule_len = rule_count;
  for (int i = 0; i < rule_count; i++) {
    char buf[100];
    scanf("%s", buf);
    fprintf(stderr,  "debug: input merge: %s\n", buf);
    merge_rule[i][0] = buf[0];
    merge_rule[i][1] = buf[1];
    merge_rule[i][2] = buf[2];
  }
}

static void generate_opps_rule(int rule_count)
{
  opps_rule_len = rule_count;
  for (int i = 0; i < rule_count; i++) {
    char buf[100];
    scanf("%s", buf);
    fprintf(stderr, "debug: input opps: %s\n", buf);
    opps_rule[i][0] = buf[0];
    opps_rule[i][1] = buf[1];
  }
}

static void generate_seq(int char_count)
{
  seq_len = char_count;
 // for (int i = 0; i < char_count; i++) {
    char buf[200];
    scanf("%s", buf);
    fprintf(stderr, "debug: input seqs: %s\n", buf);
 // }
  for (int i = 0; i < char_count; i++)
    seq[i] = buf[i];
}


static int search_merge(int x, int y)
{
  for (int i = 0 ; i < merge_rule_len; i++)
    if (x == merge_rule[i][0] && y == merge_rule[i][1] 
        || x == merge_rule[i][1] && y == merge_rule[i][0])
      return i;
  return -1;
}

static int search_opps(int x, int y)
{
  for (int i = 0 ; i < opps_rule_len; i++)
    if (x == opps_rule[i][0] && y == opps_rule[i][1] 
        || x == opps_rule[i][1] && y == opps_rule[i][0])
      return i;
  return -1;
}

static void walk_seq()
{
  bool mask[200];
  fill(mask, mask + 200, true);

  for (int i = 1; i < seq_len; i++) if (mask[i]) {
    /*
     *  First check if it can be merged
     */
    for (int j = i - 1; j >= 0; j--) if (mask[j]) {
      int merge = search_merge(seq[i], seq[j]);
      if (merge != -1) {
        seq[i]    = merge_rule[merge][2];
        mask[j]   = false;  /* remove previous one */
      }
      break;
    }

    /*
     *  Then if it could be removed for all the previous char
     */
    for (int j = i - 1; j >= 0; j--) if (mask[j]) {
      if (search_opps(seq[i], seq[j]) != -1) {
        /* clear the list or clear the segment ? */
        fill(mask, mask + i + 1, false);
        break;
      }
    }
  }

  bool flag = false; /* output format */
  for (int i = 0; i < seq_len; i++) if (mask[i]) {
    if (flag) {
      printf(", ");
    }
    printf("%c", seq[i]);
    flag = true;
  }

}


static void solve(int t)
{
  fprintf(stderr, "debug: case %d\n", t);
  int c, d, n;
  scanf("%d", &c);
  generate_merge_rule(c);
  scanf("%d", &d);
  generate_opps_rule(d);
  scanf("%d", &n);
  generate_seq(n);
  printf("[");
  walk_seq();
  printf("]");
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}





