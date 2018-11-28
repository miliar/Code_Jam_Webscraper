#include<iostream>
using namespace std;

int map[102][102];
int nbour[100][100];        //1-n,2-w,3-e,4-s
int label[100][100];
int read[100][100];
int count,h,w;
char alpha[26],labelo[100][100];
void init()
{
    cin>>h>>w;
    ::count=0;
    for(int i=0;i<26;i++)
    {
        alpha[i]='A';
    }
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<w;j++)
        {
            cin>>map[i+1][j+1];
            nbour[i][j]=label[i][j]=read[i][j]=0;
        }
    }
    for(int i=0;i<=h+1;i++)
    {
        map[i][0]=1000000;
        map[i][w+1]=100000;
    }
    for(int i=0;i<=w+1;i++)
    {
        map[0][i]=1000000;
        map[h+1][i]=100000;
    }
}
    
void nbour_asign()
{
    for(int i=1;i<=h;i++)
    {
        int m=i-1;
        for(int j=1;j<=w;j++)
        {
            int n=j-1,tmp=map[i][j];
            if(map[i-1][j]<tmp)
            {
                nbour[m][n]=1;
                tmp=map[i-1][j];
            }
            if(map[i][j-1]<tmp)
            {
                nbour[m][n]=2;
                tmp=map[i][j-1];
            }
            if(map[i][j+1]<tmp)
            {
                nbour[m][n]=3;
                tmp=map[i][j+1];
            }
            if(map[i+1][j]<tmp)
            {
                nbour[m][n]=4;
                tmp=map[i+1][j];
            }
            if(tmp==map[i][j])
            {
                label[m][n]= ::count++;
                read[m][n]=1;
            }
        }
    }
}

int traverse(int m,int n)
{
    if(read[m][n]==1)
        return label[m][n];
    switch(nbour[m][n])
    {
        case 1:
            label[m][n]=traverse(m-1,n);
            break;
        case 2:
            label[m][n]=traverse(m,n-1);
            break;
        case 3:
            label[m][n]=traverse(m,n+1);
            break;
        case 4:
            label[m][n]=traverse(m+1,n);
            break;
    }
    read[m][n]=1;
    return label[m][n];
}
void labeling()
{
    ::count=0;
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<w;j++)
        {
            if(alpha[label[i][j]]=='A')
            {
                 alpha[label[i][j]]= 'a' + ::count++;
            }
            labelo[i][j]=alpha[label[i][j]];
        }
    }
}            
        
int main()
{
    int t,ct=1;
    cin>>t;
    while(t--)
    {
        init();
        nbour_asign();  
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
                traverse(i,j);
        }
        labeling();
        cout<<"Case #"<<ct++<<":\n";
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
                cout<<labelo[i][j]<<' ';
            cout<<endl;
        }
    }
    
    return 0;
}
