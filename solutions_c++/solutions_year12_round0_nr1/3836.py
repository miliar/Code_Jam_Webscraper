#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

string A="abcdefghijklmnopqrstuvwxyz";
string T="ynficwlbkuomxsevzpdrjgthaq";

int main()
{
    freopen("A-small-attempt5.in","r",stdin);
    freopen("A-small-attempt5.out","w",stdout);
    for (int i=0;i<26;i++) for (int j=i;j<26;j++)
    if (T[i]>T[j])
    {
        char tmp=A[i];A[i]=A[j];A[j]=tmp;
        tmp=T[i];T[i]=T[j];T[j]=tmp;
    }
    
    int c,num=0;
    scanf("%d\n",&c);
    while (c)
    {
        c--;num++;
        char ch;
        printf("Case #%d: ",num);
        while (1)
        {
            scanf("%c",&ch);
            if (ch=='\n') 
            {
                printf("\n");break;
            }
            if (ch==' ') printf(" ");
            else printf("%c",A[ch-'a']);
        }
    }
}
            
        
