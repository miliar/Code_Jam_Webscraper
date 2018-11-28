#include<iostream>
#include<string>
using namespace std;
//#define dump(x) cerr <<  __LINE__ << " : "<< #x << "  =  " << (x) <<endl;
int main()
{
    int L,D,N;
    char words[5000][16],t[2000],w[15][26];
    int i,j,k,kk;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    for (i=0;i<D;i++) scanf("%s",words[i]);
    //dump(words[0][L]);dump(words[i]);}
    for (i=0;i<N;i++)
    {
        scanf("%s",t);//dump(t);
        //for (j=0;j<L;j++) w[j][0]='\0';
        k=0;j=0;
        while (t[j]){
           if (t[j]!='(') {w[k][0]=t[j++];w[k++][1]='\0';}
           else {
               kk=0;
               while (t[++j]!=')') w[k][kk++]=t[j]; 
               w[k][kk]='\0';
               j++;k++;            
               }
           }//dump(k);
       /* for (j=0;j<k;j++) {
          for (kk=0;w[j][kk];kk++)
           dump(w[j][kk]);
           dump("&&&&");}*/
        int sum=0;
        bool f1,f2;
        for (j=0;j<D;j++)
        {
             f2=true;
             for (k=0;words[j][k];k++)
             {
                 f1=false;
                 for (kk=0;w[k][kk];kk++)
                    if (words[j][k]==w[k][kk]) {f1=true;break;}
                 if (!f1) {f2=false;break;}
             }
             if (f2) sum++;
        }
        cout<<"Case #"<<i+1<<": "<<sum<<endl;
    }
    //system("pause");
    return 0;
    
}
