#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

int main()
{
    ifstream fin("alienlang.in");
    ofstream fout("alienlang.out");
    
    int i,j,n,k,l,d,zag=0,poz=0,br=0,brojac=0;
    string a[5001];
    //scanf("%d%d%d",&l,&d,&n);
    fin>>l>>d>>n;
    for (i=0;i<d;i++) fin>>a[i];
    
    for (i=0;i<n;i++)
    {
        brojac++;
        zag=0;
        poz=0;
        br=0;
        char b[5010];
        int t[5010]={0};
        //scanf("%s",b);
        fin>>b;
        for (j=0;j<strlen(b);j++)
        {
            if (b[j]=='(') zag=1;
               else if (b[j]==')') zag=0;
            for (k=0;k<d;k++)
            if (a[k][poz]==b[j]) t[k]++;
            if (zag==0) poz++;
        }
        for (j=0;j<d;j++)
        if (t[j]==l) br++;
        //printf("Case #%d: %d\n",brojac,br);
        fout<<"Case #"<<brojac<<": "<<br<<endl;
    }
    return 0;
}
