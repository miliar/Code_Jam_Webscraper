#include<iostream>
#include<string>
using namespace std;
int main()
{
    int L,D,N;
    char word[5000][16],t[2000],w[15][26];
    int i,j,k,wc;
    freopen("1.in","r",stdin);
    freopen("2.out","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    for (i=0;i<D;i++) scanf("%s",word[i]);
    for (i=0;i<N;i++)
    {
        scanf("%s",t);
        k=0;j=0;
        while (t[j]){
           if (t[j]!='(') {w[k][0]=t[j++];w[k++][1]='\0';}
           else {
               wc=0;
               while (t[++j]!=')') w[k][wc++]=t[j]; 
               w[k][wc]='\0';
               j++;k++;            
               }
           }
        int sum=0;
        bool f1,f2;
        for (j=0;j<D;j++)
        {
             f2=true;
             for (k=0;word[j][k];k++)
             {
                 f1=false;
                 for (wc=0;w[k][wc];wc++)
                    if (word[j][k]==w[k][wc]) {f1=true;break;}
                 if (!f1) {f2=false;break;}
             }
             if (f2) sum++;
        }
        cout<<"Case #"<<i+1<<": "<<sum<<endl;
    }
    return 0;
}
