#include<iostream>
#include<conio.h>
#include<fstream>

using namespace std;
int x,y,k,o,b,oo[100],bb[100],ans[20],ooo[10],bbb[10];
char r;

void check();

void push(char rr,int xx)
{
     if(rr=='b' || rr=='B')
     {
                /*if(bb[xx-1]==0)
                              bb[xx-1]++;
                else
                              check();*/
     }
     else
     {
                /*if(oo[xx-1]==0)
                              oo[xx-1]++;
                else
                              check();*/
     }
}

void backward(char rr)
{
     if(rr=='b' || rr=='B')
     b--;
     else
     o--;
     
}
void forward(char rr)
{
     if(rr=='b' || rr=='B')
     b++;
     else
     o++;
     
}

void check()
{
     k++;
     if(b==x)
     {
             if(o==y)
             {
                     if(r=='b' || r=='B')
                               push('b',x);
                     else
                               push('o',y);
             }
             else if(o>y)
             {
                        if(r=='b' || r=='B')
                        {
                                  push('b',x);
                                  backward('o');
                                  //check();
                        }
                        else
                        {backward('o');check();}
             }
             else if(o<y)
             {
                        if(r=='b' || r=='B')
                        {
                                  push('b',x);
                                  forward('o');
                                  //check();
                        }
                        else
                        {forward('o');check();}
             }
     }
     else if(b>x)
     {
                if(o==y)
                {
                        if(r=='b' || r=='B')
                        {backward('b');check();}
                        else
                        {
                                  push('o',y);
                                  backward('b');
                                  //check();
                        }
                }
                else if(o>y)
                {
                           backward('b');
                           backward('o');
                           check();
                }
                else if(o<y)
                {
                           backward('b');
                           forward('o');
                           check();
                }
     }
     else if(b<x)
     {
                if(o==y)
                {
                           if(r=='b' || r=='B')
                           {forward('b');check();}
                           else
                           {
                                      push('o',y);
                                      forward('b');
                                      //check();
                           }
                }
                else if(o>y)
                {
                           forward('b');
                           backward('o');
                           check();
                }
                else if(o<y)
                {
                           forward('b');
                           forward('o');
                           check();
                }
     }

}



int main()
{
    //ifstream myReadFile;
    //myReadFile.open("text.txt");
    ifstream fin("text.txt");

    int t,i,n,j,a[10];
    char c[10];
    fin>>t;
    for(i=0;i<t;i++)
    {
                 fin>>n;
                 for(j=0;j<n;j++)
                 {
                                       fin>>c[j];
                                       fin>>a[j];
                 }
                 o=1;b=1;k=0;x=1;y=1;
                 int l=0,m=0;
                 //for(j=0;j<100;j++)
                                   //oo[j]=bb[j]=0;
                 for(j=0;j<10;j++)
                                   ooo[j]=bbb[j]=0;
                 for(j=0;j<n;j++)
                 {
                                 r=c[j];
                                 if(r=='b' || r=='B')
                                           {
                                                     bbb[l]=a[j];
                                                     l++;
                                           }
                                 else
                                           {
                                                     ooo[m]=a[j];
                                                     m++;
                                           }
                 }
                 l=m=0;
                 if(bbb[l]!=0)
                      x=bbb[l];
                 if(ooo[m]!=0)
                      y=ooo[m];
                 for(j=0;j<n;j++)
                 {
                                 r=c[j];
                                 
                                 check();
                                 if(r=='b' || r=='B')
                                 {
                                              l++;
                                              if(bbb[l]!=0)
                                              x=bbb[l];
                                 }
                                 else
                                 {
                                              m++;
                                              if(ooo[m]!=0)
                                              y=ooo[m];
                                 }
                 }
                 ans[i]=k;
    }
    fin.close();
    ofstream fout("text1.txt");
    for(i=0;i<t;i++)
    {
                    fout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
    }
    fout.close();
    getch();
    return 0;
}
