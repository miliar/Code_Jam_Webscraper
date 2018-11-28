// GCJ.cpp : Defines the entry point for the console application.
//



#include <stdio.h>
#include <string.h>

void Welcome()
{
  int N;
  char pat[] = "welcome to code jam";
  int p_len = 19;


  scanf("%d", &N);
  int i, k;
  char s[502];
  long long cnt[19][502];

  char ch;
  scanf( "%c", &ch); // \n
  for(i = 0; i < N; i++){
    int s_len = 0;
	gets(s);
    s_len = strlen(s);

    for(k = 0; k < 19; k++){
      for(int j = 0; j < 502; j++){
        cnt[k][j] = 0;
      }
    } 

    int h = 0, len = 1;
    if(s[0] == 'w')
      cnt[0][0] = 1;
    for(h = 1; h < s_len; h++){
      if(s[h] == 'w')
        cnt[0][h] = cnt[0][h-1] + 1;
      else
        cnt[0][h] = cnt[0][h-1];
    }

    for(len = 2; len <= p_len; len++){
      for(h = len-1; h <= s_len-1; h++){
        if(s[h] == pat[len-1])
          cnt[len-1][h] = (cnt[len-2][h-1] + cnt[len-1][h-1])%10000;
        else
          cnt[len-1][h] = cnt[len-1][h-1];
      }
    }

    long long sum = cnt[18][s_len-1]%10000;

    printf("Case #%d: ",i+1);
    printf("%0.4lld\n", sum);
  }
}

int main()
{
  Welcome();
  return 0;
}

