#include<iostream>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,i,j,k,x,N,F,l;
    scanf("%d\n",&T);
    char str[30],str1[30];
    for (i=1;i<=T;i++)
    {
        gets(str);
        strcpy(str1,str);
        l=strlen(str);
        sort(str1,str1+l,greater<char>());
        printf("Case #%d: ",i);
        if (strcmp(str,str1))
        {
                            // cout<<"here\n";
           next_permutation(str,str+l);
           cout<<str;
        }
        else
        {
            sort(str1,str1+l);
            if (str1[0]=='0')
            {
               j=0;
               while (str1[j]=='0')
                     j++;
               str1[0]=str1[j];
               str1[j]='0';
            }
            cout<<str1[0]<<"0";
            for (j=1;j<l;j++)
            {
                cout<<str1[j];
            }
        }
        cout<<endl;
    }
}
