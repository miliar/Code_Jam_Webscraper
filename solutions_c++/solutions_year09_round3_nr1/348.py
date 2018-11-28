    #include <iostream>
    #include <cstdio>
    #include <cstring>

    using namespace std;

    int id[100];
    char s[1000];
    int tot, base;

    int getx(char x)
    {
       if (x >= '0' && x <= '9') return (x - '0');
       else return (x - 'a' + 10);   
    }

    int getid(char x)
    {
       if (x >= '0' && x <= '9') return id[(x - '0')];
       else return id[(x - 'a' + 10)];
    }

    int main()
    {
       int tests;
       
       scanf("%d",&tests);
       int cases = 0;
       while (tests--){
          scanf("%s",s);
          int len = strlen(s);
          if (len == 1){
              printf("Case #%d: 1\n",++cases);
              continue;
          }
          memset(id, 0xff, sizeof(id));
          int ids = getx(s[0]);
          id[ids] = 1;
          tot = 0;
          for (int i = 1; i < len; ++i)
          {      
             int idtmp = getid(s[i]);
             //printf("!%c %d\n",s[i], idtmp);
             if (idtmp == -1)
             {
                id[getx(s[i])] = tot;
                tot++;
                if (tot == 1) tot = 2;
             }   
          }
          if (tot == 0) base = 2;
          else base = tot;
          
          long long ans = 0;
          long long e = 1;
          for (int i = len - 1; i >= 0; --i)
          {
             //printf("%c %d\n",s[i], getid(s[i]));
             ans += e * getid(s[i]);
             e *= base;
          }
          printf("Case #%d: %lld\n",++cases, ans);
       }
       return 0;
    }
