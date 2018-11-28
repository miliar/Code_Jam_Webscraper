#include <cstdio>
#include <cstring>
#include <map>

using std::map;

namespace {
  struct CmpStr {
    bool operator() (const char* a, const char* b) const {
      return strcmp(a, b) < 0;
    }
  };

  char host[100][120];
  char query[1000][120];
  char host_taken[100];
  map<const char*, int, CmpStr> dict;
  int host_num;
  int query_num;

  void ReadName() {
    char waste[200];
    scanf("%d", &host_num);
    gets(waste);
    for (int i = 0; i < host_num; i++) {
      gets(host[i]);
    }
    scanf("%d", &query_num);
    gets(waste);
    for (int i = 0; i < query_num; i++) {
      gets(query[i]);
    }

    dict.clear();
    for (int i = 0; i < host_num; i++)
      dict[host[i]] = i;
  }

  int GetMinSwitch() {
    //     printf("%d\n", host_num);
    //     for (int i = 0; i < host_num; i++) {
    //       printf("%s\n", host[i]);
    //     }
    //     printf("\n\n=====\n\n");
    //     printf("%d\n", query_num);
    //     for (int i = 0; i < query_num; i++) {
    //       printf("%s\n", query[i]);
    //     }
    //     printf("\n\n=====\n\n");
    memset(host_taken, 0, sizeof(host_taken));
    int count = 0;
    int host_left = host_num;
    for (int i = 0; i < query_num; ) {
      int host_id = dict[query[i]];
      if (!host_taken[host_id])
        host_left--;
      host_taken[host_id] = true;

      if (host_left == 0) { // Flush anything before this query.
        count++;
        host_left = host_num;
        memset(host_taken, 0, sizeof(host_taken));

      } else { // Add this query to current batch.
        i++;
      }
    }
    return count;
  }

  void ProcessCase(int case_id) {
    ReadName();
    printf("Case #%d: %d\n", case_id, GetMinSwitch());
  }
}

int main() {
  int case_num;
  scanf("%d", &case_num);

  for (int i = 1; i <= case_num; i++) {
    ProcessCase(i);
  }

  return 0;
}
