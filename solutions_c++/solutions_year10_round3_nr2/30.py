#include<iostream>
#include<cstdio>
#include<fstream>
#include<cmath>

using namespace std;

int main()
{
    int i,j,k;
    ifstream fin("B-large.in");
    FILE* fp=fopen("B_large.txt","w+");
    
    int T,L,P,C,ans;
    double temp_double;
    fin>>T;
    
    for(i=0;i<T;++i)
    {
        fin>>L>>P>>C;
        ans=0;
        temp_double=log(((double)P)/((double)L))/log(C);
        ans=ceil(log(temp_double)/log(2));
        fprintf(fp,"Case #%d: %d\n",i+1,(ans>0)?ans:0);
        
        //system("pause");
    }
    //system("pause");
    fclose(fp);
    return 0;
}
