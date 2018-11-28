#include<string>
#include<algorithm>
using namespace std;
int N;
string s;
char in[30];
int main()
{
    scanf("%d", &N);
    int c =1;
    while(N--)
    {
        scanf("%s", in);
        s = (string)in;
       bool ok =  next_permutation(s.begin(), s.end());
       if(ok)
        printf("Case #%d: %s\n", c++, s.c_str());
       if(!ok)
       {
          s = '0'+s;
          sort(s.begin(), s.end());
          while(s[0]=='0')
           next_permutation(s.begin(), s.end());
           printf("Case #%d: %s\n", c++, s.c_str());
       }
    }
}
