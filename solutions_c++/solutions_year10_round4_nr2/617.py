#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int T,P,temp;
int two[12]={1,2,4,8,16,32,64,128,256,512,1024,2048};

int main()
{
    int i,j,k,l;
    ifstream fin("B-small-attempt0.in");
    FILE* fp=fopen("B_small.txt","w+");
    
    int need[1050];
    bool done,nonzero;
    int layer,ans;

    fin>>T;
    for(i=0;i<T;++i)
    {
        fin>>P;
        for(j=0;j<two[P];++j)
        {
            fin>>temp;
            need[j]=P-temp;
            
            cout<<need[j]<<" ";
        }
        cout<<endl;
        for(j=0;j<P;++j)
        for(k=0;k<two[j];++k)
            fin>>temp;
        
        done=0;
        ans=0;
        layer=P;
        while(!done)
        {
            for(j=0;j<two[P];j+=two[layer])
            {
                nonzero=0;
                for(k=j;k<j+two[layer];++k)
                    nonzero|=(need[k]>0);
                if(nonzero)
                {
                    ++ans;
                    for(k=j;k<j+two[layer];++k)
                        need[k]=(need[k]>0)?need[k]-1:0;
                }
            }
            nonzero=0;
            for(j=0;j<two[P];++j)
                nonzero|=(need[j]>0);
            if(nonzero)
                --layer;
            else
                break;
        }
        
        fprintf(fp,"Case #%d: %d\n",i+1,ans);
    }
    return 0;
    
}
