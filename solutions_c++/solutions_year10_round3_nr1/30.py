#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;

int main()
{
    int i,j,k;
    ifstream fin("A-large.in");
    FILE* fp=fopen("A_large.txt","w+");
    
    int T,N,A[1100],B[1100],ans;
    fin>>T;
    for(i=0;i<T;++i)
    {
        ans=0;
        fin>>N;
        for(j=0;j<N;++j)
            fin>>A[j]>>B[j];
        for(j=0;j<N;++j)
        for(k=j+1;k<N;++k)
        {
            if((A[j]-A[k])*(B[j]-B[k])<0)
                ++ans;
        }

        fprintf(fp,"Case #%d: %d\n",i+1,ans);
    }
    //system("pause");
    fclose(fp);
    return 0;
}
