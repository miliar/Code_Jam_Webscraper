#include <iostream>

using namespace std;
int main()
{
    FILE *fin;
    FILE *fout;
    fin=fopen("A-large.in","r");
    fout=fopen("A-large.out","w");
    char board[52][52],absent;
    int t,r,c,row[52],columns[52],numbers,answer;

    fscanf(fin,"%d",&t);
    //cin>>t;
    for (int i=1;i<=t;++i)
    {
        answer=0;
        numbers=0;
        for (int j=1;j<=51;++j)
        {
            row[j]=0;
            columns[j]=0;
        }
        fscanf(fin,"%d%d%c",&r,&c,&absent);
        //cin>>r>>c;
        for (int j=1;j<=r;++j)
            for (int k=1;k<=c+1;++k)
            {
                fscanf(fin,"%c",&board[j][k]);
                //cout<<board[j][k];
                if(board[j][k]=='#')
                {
                    row[j]++;
                    columns[k]++;
                    numbers++;
                }
            }   
        for(int j=1;j<=r;++j)
            if(row[j]%2==1)
                answer=1;
        for(int j=1;j<=c;++j)
            if(columns[j]%2==1)
                answer=1;
        if(numbers%4!=0)
            answer=1;
        //for(int j=1;j<=r;++j)
        //cout<<row[j];
        //system("pause");
        //for(int j=1;j<=c;++j)
        //cout<<columns[j];
        //system("pause");
        //cout<<numbers;
        if(answer==1)
        {
        fprintf(fout,"Case #%d:\nImpossible\n",i);
        continue;
        }
        for(int j=1;j<=r-1 && answer!=1;++j)
            for(int k=1;k<=c-1;++k)
                if(board[j][k]=='#')
                {
                    if(board[j][k+1]!='#' || board[j+1][k]!='#' || board[j+1][k+1]!='#')
                    {
                    answer=1;
                    break;
                    }
                    else
                    {
                        board[j][k]='/';
                        board[j][k+1]='\\';
                        board[j+1][k]='\\';
                        board[j+1][k+1]='/';
                    }
                }
        if(answer==1)
        {
        fprintf(fout,"Case #%d:\nImpossible\n",i);
        continue;
        }
        fprintf(fout,"Case #%d:\n",i);
        for (int j=1;j<=r;++j)
        {
            for (int k=1;k<=c;++k)
            {
                fprintf(fout,"%c",board[j][k]);
                cout<<board[j][k];
            }
            fprintf(fout,"\n");
            printf("\n");
        }
            
    }
    system("pause");
    
}
