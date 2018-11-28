#include<iostream>
#include<cstdio>
#include<fstream>
#include<map>

using namespace std;

int board[550][550];
int T,M,N;

bool search(int sm,int sn,int size)
{
    int i,j;
    
    for(i=sm+1;i<sm+size;++i)
    {
        for(j=sn+1;j<sn+size;++j)
        {
            if(board[i][j]*board[i-1][j]!=-1 || board[i][j]*board[i][j-1]!=-1)
            {
                return 0;
            }
        }
    }
    if(board[sm][sn]*board[sm+1][sn]!=-1 || board[sm][sn]*board[sm][sn+1]!=-1)
        return 0;
    else
        return 1;
};

void erase(int sm,int sn,int size)
{
    int i,j;
    for(i=sm;i<sm+size;++i)
    for(j=sn;j<sn+size;++j)
        board[i][j]=0;
    return;
}

int main()
{
    int i,j,k,l;
    ifstream fin("C-large.in");
    FILE* fp=fopen("C_large.txt","w+");
    
    map<char,int> word_2_int;
    char word[16]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    for(i=0;i<16;++i)
        word_2_int.insert(make_pair(word[i],i));
    int two[4]={8,4,2,1};
    
    int num[530],num_size,one;
    int temp_int,max_sq;
    char temp_char;
    fin>>T;
    for(i=0;i<T;++i)
    {
        memset(num,0,sizeof(int)*530);
        num_size=1;
        
        fin>>M>>N;
        one=M*N;
        for(j=0;j<M;++j)
        {
            for(k=0;k<N/4;++k)
            {
                fin>>temp_char;
                temp_int=word_2_int[temp_char];
                for(l=0;l<4;++l)
                {
                    if(temp_int>=two[l])
                    {
                        board[j][4*k+l]=1;
                        temp_int-=two[l];
                    }
                    else
                    {
                        board[j][4*k+l]=-1;
                    }      
                }
            }
        }
        
        max_sq=(M>N)?N:M;
        for(j=max_sq;j>1;--j)
        {
            for(k=0;k<=M-j;++k)
            for(l=0;l<=N-j;++l)
            {
                if(search(k,l,j))
                {
                    erase(k,l,j);
                    if(num[j]==0)
                        ++num_size;
                    ++num[j];
                    one-=j*j;
                }
            }
        }
        
        if(one==0)
            --num_size;
        fprintf(fp,"Case #%d: %d\n",i+1,num_size);
        for(j=529;j>1;--j)
        {
            if(num[j]>0)
                fprintf(fp,"%d %d\n",j,num[j]);
        }
        if(one>0)
            fprintf(fp,"1 %d\n",one);
        printf("%d\n",i+1);
    }
    fclose(fp);
    return 0;
}
