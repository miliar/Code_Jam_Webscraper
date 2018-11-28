#include <iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<bitset>
using namespace std;

void split(char *str, int l ,char * out1,char *out2)
{
    int i,j=0,k=0;
    for(i=0;i<l;i++)
    {
        out1[j++] = str[i];
    }
    out1[j] = '\0';
    for(;i<strlen(str);i++)
    {
        out2[k++] = str[i];
    }
    out2[k] = '\0';
}
int main()
{
    int i,t,j,k=0,n1,n2,l,tmp,cnt;
    char str[105],a1[50],a2[50];
    bitset<2000001> st1;
    bitset<2000001> st2;
    freopen ("out.txt","w",stdout);
    freopen("in.txt","r",stdin);

    scanf("%d",&t);
    k=1;
    while(t--)
    {
        st1.reset();
        st2.reset();
        cnt=0;
        scanf("%d",&n1);
        scanf("%d",&n2);
        cout<<"Case #"<<k<<": ";

        for(i=n1;i<=n2;i++)
        {
           // if(st[i])
                //continue;
            itoa(i,str,10);
            l= strlen(str);

            for(j=1;j<l;j++)
            {
                split(str,j,a1,a2);

                if(a2[0] == '0')
                {
                    continue;
                }

                strcat(a2,a1);

                tmp =  atoi(a2);

                if(!(st1[tmp] && st2[i]))
                {
                    if(tmp == i)
                    {
                       //cout<<i<<" "<<tmp<<"\n";
                        //st.set(i,true);
                        //cnt++;
                        continue;

                    }


                    if(tmp<=n2 && tmp >= n1)
                    {
                        //cout<<<<" "<<tmp<<"\n";
                        st2.set(tmp,true);
                        st1.set(i,true);

                        cnt++;
                    }
                }
            }


        }


        cout<<cnt;
        cout<<"\n";

        k++;
    }

    return 0;

}
