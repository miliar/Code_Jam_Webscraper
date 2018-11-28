#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;
char array_result[100][100]={0};
int array_input[100][100]={0};
char c_num='a';
int h=0,w=0;
int add_x[]={0,-1,1,0,0};
int add_y[]={-1,0,0,1,0};

stack<int> stack_x;
stack<int> stack_y;
bool mycheck(int x,int y)
{
return x>=0&&x<w&&y>=0&&y<h;
    }

int mycheckFlow(int x,int y)
{
 int n_low=array_input[y][x];
 int n_num=-1;
    for(int i=0;i<4;i++)
       {
           int x_temp=x+add_x[i];
           int y_temp=y+add_y[i];
            if(mycheck(x_temp,y_temp))
            {
              if(n_low>array_input[y_temp][x_temp])
                    {n_low=array_input[y_temp][x_temp];n_num=i;}
                }
        }
    return n_num;
}
int mydo(int x, int y)
{
int x_deal=x,y_deal=y;
int n_orient=4;
do{
    x_deal+=add_x[n_orient];
    y_deal+=add_y[n_orient];
    stack_x.push(x_deal);
    stack_y.push(y_deal);
    array_result[y_deal][x_deal]=c_num;
    n_orient=mycheckFlow(x_deal,y_deal);
    }
while(n_orient!=-1);

while(!stack_x.empty())
{
    x_deal=stack_x.top();
    y_deal=stack_y.top();

    stack_x.pop();
    stack_y.pop();

    for(int i=0;i<4;i++)
    {
    int x_temp=x_deal-add_x[i];
    int y_temp=y_deal-add_y[i];
    if(mycheck(x_temp,y_temp)&&array_result[y_temp][x_temp]==0)
        {
        int n_temp=mycheckFlow(x_temp,y_temp);
        if(i==n_temp)
            {stack_x.push(x_temp);
            stack_y.push(y_temp);
            array_result[y_temp][x_temp]=c_num;
                }
        }
    }
}


c_num++;
return 0;
    }

int main()
{
    ifstream in("a.in");
    ofstream out("a.out");
int t=0;
in>>t;
    for(int num=1;num<=t;num++)
    {
        memset(array_result,0,sizeof(array_result));
        memset(array_input,0,sizeof(array_result));
        c_num='a';

        in>>h>>w;
        for(int y=0;y<h;y++)
        {
            for(int x=0;x<w;x++)
                in>>array_input[y][x];
            }


        for(int y=0;y<h;y++)
        {
            for(int x=0;x<w;x++)
                if(array_result[y][x]==0)
               { mydo(x,y);}
            }

        out<<"Case #"<<num<<":"<<endl;
        for(int y=0;y<h;y++)
        {
            for(int x=0;x<w-1;x++)
                out<<array_result[y][x]<<" ";
            out<<array_result[y][w-1]<<endl;
            }
    }
    return 0;
}
