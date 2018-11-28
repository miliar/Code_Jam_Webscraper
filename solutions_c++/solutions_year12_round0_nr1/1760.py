#include<stdio.h>
#include<map>
using namespace std;
int main()
{
    freopen("F:\\A-small-attempt6.in","r",stdin);
    freopen("F:\\file.txt","w+",stdout);
    int n=0,i=0,j=0,k=0;
    char a[100],ch;
    map<char,char>v;
    v.insert(pair<char,char>('a','y'));
    v.insert(pair<char,char>('b','h'));
    v.insert(pair<char,char>('c','e'));
    v.insert(pair<char,char>('d','s'));
    v.insert(pair<char,char>('e','o'));
    v.insert(pair<char,char>('f','c'));
    v.insert(pair<char,char>('g','v'));
    v.insert(pair<char,char>('h','x'));
    v.insert(pair<char,char>('i','d'));
    v.insert(pair<char,char>('j','u'));
    v.insert(pair<char,char>('k','i'));
    v.insert(pair<char,char>('l','g'));
    v.insert(pair<char,char>('m','l'));
    v.insert(pair<char,char>('n','b'));
    v.insert(pair<char,char>('o','k'));
    v.insert(pair<char,char>('p','r'));
    v.insert(pair<char,char>('q','z'));
    v.insert(pair<char,char>('r','t'));
    v.insert(pair<char,char>('s','n'));
    v.insert(pair<char,char>('t','w'));
    v.insert(pair<char,char>('u','j'));
    v.insert(pair<char,char>('v','p'));
    v.insert(pair<char,char>('w','f'));
    v.insert(pair<char,char>('x','m'));
    v.insert(pair<char,char>('y','a'));
    v.insert(pair<char,char>('z','q'));
    scanf("%d",&n);
    scanf("%c",&ch);
    for(i=0;i<n;i++)
    {
                    j=0;
                    while(scanf("%c",&a[j]))
                    {
                                            if(a[j]=='\n'){break;}
                                            j++;
                    }
                    printf("Case #");
                    printf("%d",i+1);
                    printf(": ");
                    for(k=0;k<j;k++)
                    {
                                    if(a[k]!=' ')
                                    { 
                                               printf("%c",v[a[k]]);
                                               }
                                    else
                                    {
                                        printf(" ");
                                        }
                                    }
                    printf("\n");
                                    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
