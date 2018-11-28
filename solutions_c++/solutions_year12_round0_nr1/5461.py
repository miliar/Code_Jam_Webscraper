#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int n;
    scanf("%d",&n);
    char buf[1000];
    char buf2[1000];
    gets(buf);
    char dict[1000] = "zqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    char ans[1000] =  "qzour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    for (int i = 0 ; i < n ; i++) {
        gets(buf);
        cout <<"Case #"<<i+1<<": ";
        for (int k = 0 ;;k++){
            if (buf[k]=='\0') {buf2[k] ='\0'; break;}
            for (int j = 0 ;; j++){
                if (dict[j]==buf[k])
                    buf2[k]=ans[j];
                if (ans[j]=='\0') break;
            }
        }
        cout << buf2<<endl;

    }
}
