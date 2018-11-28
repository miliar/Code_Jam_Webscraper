// Author: .zGr..
#include <iostream>
#include <fstream>
using namespace std;

void find_sink(int i,int j,int H,int W,int *map,char *sink_i,char *sink_j)
{
    int check=1;
    while (check!=0)
    {
        int min=1000000000,min_ind;
        check=0;
        if (i-1>=0 && map[(i-1)*W+j]<map[i*W+j]) { min=map[(i-1)*W+j]; min_ind=i-1; check=1; }
        if (j-1>=0 && map[i*W+j-1]<map[i*W+j] && map[i*W+j-1]<min) { min=map[i*W+j-1]; min_ind=j-1; check=2; }
        if (j+1<W && map[i*W+j+1]<map[i*W+j] && map[i*W+j+1]<min) { min=map[i*W+j+1]; min_ind=j+1; check=2; }
        if (i+1<H && map[(i+1)*W+j]<map[i*W+j] && map[(i+1)*W+j]<min) { min=map[(i+1)*W+j]; min_ind=i+1; check=1; }
        if (check==1) i=min_ind;
        if (check==2) j=min_ind;
    }
    *sink_i=i;
    *sink_j=j;
}

int main()
{
    int T;
    ifstream inp;
    inp.open("B-large.in");
    ofstream op;
    op.open("B-large_op.txt");
    inp >> T;
    for (int i=0;i<T;i++)
    {
        int H,W;
        inp >> H >> W;
        int * map=new int [H*W];
        char * result=new char [H*W];
        char si,sj;
        char * sink_i=&si, * sink_j=&sj;
        for (int j=0;j<H*W;j++) result[j]=0;
        for (int j=0;j<H;j++)
        {
            for (int k=0;k<W;k++)   inp >> map[j*W+k];
        }
        char last='a';
        for (int j=0;j<H;j++)
        {
            for (int k=0;k<W;k++)
            {
                
                find_sink(j,k,H,W,map,sink_i,sink_j);
                if (result[(*sink_i)*W+(*sink_j)]>='a' && result[(*sink_i)*W+(*sink_j)]<='z') result[j*W+k]=result[(*sink_i)*W+(*sink_j)];
                else {result[j*W+k]=last; result[(*sink_i)*W+(*sink_j)]=last; last++;}
            }    
        }
        op << "Case #" << (i+1) << ":\n"; 
        for (int j=0;j<H;j++)
        {
            for (int k=0;k<W;k++)   op << result[j*W+k] << " ";
            op << endl;
        }
    }
    inp.close();
    op.close();
    return 0;
}
                
                
                
            