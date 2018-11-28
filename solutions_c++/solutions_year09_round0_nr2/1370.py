#include<iostream>
#include<stdio.h>
#include<fstream>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>

#define MAX 100

using namespace std;

int a[MAX][MAX],d[MAX][MAX];
char s[MAX][MAX];
int H,W,T;

int findpath(int i, int j);
int main(int argc, char* argv[])
{
    int i,j,k;
    char b;
    cin>>T;
    for(i=0;i<T;i++)
    {
            cin>>H>>W;
            for(j=0;j<H;j++) {
                             for(k=0;k<W;k++) {
                                            cin>>a[j][k];
                                            d[j][k]=-1;
                                            s[j][k]=(char)0;
                             }
            }
            //cout<<"done";
            b='a';
            for(j=0;j<H;j++)
                             for(k=0;k<W;k++)
                                             findpath(j,k);
            j=0;
            while(j<(H*W))
            {
                          if(s[(j/W)][(j%W)]!=0) {
                                         j++;
                                         continue;
                          }
                          else {
                               s[(j/W)][(j%W)] = b;
                               k=j+1;
                               while(k<(H*W))
                               {
                                             if(d[(j/W)][(j%W)]==d[(k/W)][(k%W)]) {
                                                                              s[(k/W)][(k%W)]=b; 
                                             }
                                             k++; 
                                             
                               }
                               b++;
                          }
                          j++;
            }
            cout<<"Case #"<<i+1<<":"<<endl;
            for(j=0;j<H;j++) {
                             for(k=0;k<W;k++)
                                             cout<<s[j][k]<<" ";
                             cout<<endl;
            }
            
    }
    //system("PAUSE");
    return 1;
}

int findpath(int i, int j)
{
    int val,pos=-1;
    //cout<<"here"<<i<<j<<d[i][j];
    if(d[i][j]!=-1)
                   return d[i][j];
    //cout<<"whre";
    val = a[i][j];
    if(i>0 && a[i-1][j]<val) {
           pos=((i-1)*W) +j;
           val = a[i-1][j];
    }
    if(j>0 && a[i][j-1]<val) {
           pos=(i*W) + (j-1);
           val = a[i][j-1];
    }
    if(j<W-1 && a[i][j+1]<val) {
             pos = (i*W) + (j+1);
             val = a[i][j+1];
    }
    if(i<H-1 && a[i+1][j] < val) {
             pos = ((i+1)*W) +j;
             val = a[i+1][j];
    }
    //cout<<"i="<<i<<"j="<<j<<"newi="<<(pos/W)<<"newj="<<(pos%W)<<endl;
    if(pos==-1)
           d[i][j] = i*W +j;
    else
        d[i][j] = findpath((pos/W),(pos%W));
    //cout<<d[i][j];
    return d[i][j];
}
