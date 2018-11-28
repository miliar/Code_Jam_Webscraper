#include<stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
#include<ctype.h>


using namespace std;
struct point{
       int i,j;
};

int count,H,W;
vector<int> a[105];
char ans[105][105],curr_char;

point find_lowest_neighbour(point P)
{
      point temp,p[4];
      for(int k=0;k<=3;k++)
      {p[k].i=-1;p[k].j=-1;}
      
      int min;
      char ch;
      temp.i=-1;temp.j=-1;
      if(P.i>0)
      {p[0].i=P.i-1;p[0].j=P.j;}
      
      if(P.j>0)
      {p[1].j=P.j-1;p[1].i=P.i;}
      
      if(P.j<W-1)
      {p[2].j=P.j+1;p[2].i=P.i;}
      
      if(P.i<H-1)
      {p[3].i=P.i+1;p[3].j=P.j;}
      
      min=15000;
      for(int k=0;k<=3;k++)
      if(p[k].i!=-1 && p[k].j!=-1)
      if(a[p[k].i][p[k].j]<min && a[p[k].i][p[k].j]<a[P.i][P.j])
      {
                               temp=p[k];
                               min=a[p[k].i][p[k].j];
      }
      return temp;
      
}

void crawl_from_sink(point s)
{
     char ch;
     point temp,ltemp;
     if(s.i>0)
     {
              temp.i=s.i-1;temp.j=s.j;
              if(find_lowest_neighbour(temp).i!=-1 && find_lowest_neighbour(temp).j!=-1)
              if(ans[temp.i][temp.j]==' ' && find_lowest_neighbour(temp).i==s.i && find_lowest_neighbour(temp).j==s.j && a[s.i][s.j]<a[temp.i][temp.j])
              {
                                        ans[temp.i][temp.j]=curr_char;
                                        crawl_from_sink(temp);
              }
     }
     if(s.j>0)
     {
              temp.j=s.j-1;temp.i=s.i;
              if(find_lowest_neighbour(temp).i!=-1 && find_lowest_neighbour(temp).j!=-1)
              if(ans[temp.i][temp.j]==' ' && find_lowest_neighbour(temp).i==s.i && find_lowest_neighbour(temp).j==s.j && a[s.i][s.j]<a[temp.i][temp.j])
              {
                                        ans[temp.i][temp.j]=curr_char;
                                        crawl_from_sink(temp);
              }
     }
     if(s.j<W-1)
     {
                //cin>>ch;
                //cout<<'r';
              temp.j=s.j+1;temp.i=s.i;
              if(find_lowest_neighbour(temp).i!=-1 && find_lowest_neighbour(temp).j!=-1)
              if(ans[temp.i][temp.j]==' ' && find_lowest_neighbour(temp).i==s.i && find_lowest_neighbour(temp).j==s.j && a[s.i][s.j]<a[temp.i][temp.j])
              {
                                        //cout<<'r';
                                        ans[temp.i][temp.j]=curr_char;
                                        crawl_from_sink(temp);
              }
              
     }
      
     if(s.i<H-1)
     {
              temp.i=s.i+1;temp.j=s.j;
              if(find_lowest_neighbour(temp).i!=-1 && find_lowest_neighbour(temp).j!=-1)
              if(ans[temp.i][temp.j]==' ' && find_lowest_neighbour(temp).i==s.i && find_lowest_neighbour(temp).j==s.j && a[s.i][s.j]<a[temp.i][temp.j])
              {
                                        ans[temp.i][temp.j]=curr_char;
                                        crawl_from_sink(temp);
              }
     }
     //cout<<"\nreturn";
     return; 
}


point goto_sink(point Pi)
{
     char ch; 
     //ans[Pi.i][Pi.j]=::curr_char;
     point Pf=find_lowest_neighbour(Pi);
     //cout<<Pf.i<<' '<<Pf.j<<endl;
     //cin>>ch;
     if(Pf.i==-1 || Pf.j==-1)
     return Pi;
     else
     return goto_sink(Pf);
}

int main()
{
    char ch,str[10];
    int i,j,k,t,altitude,T,h,w;
    
        
    FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
    fscanf(fin,"%d",&T);
    ch=fgetc(fin);
    
    
    for(t=1;t<=T;t++)
    {
                     for(i=0;i<=104;i++)
                     for(j=0;j<=104;j++)
                     ans[i][j]='\0';
                     ::curr_char='a';
                     fscanf(fin,"%d %d",&H,&W);
                     for(i=0;i<=104;i++)
                     a[i].erase(a[i].begin(),a[i].end());
                     for(h=0;h<=H-1;h++)
                     {
                                      ch=fgetc(fin);
                                      for(w=0;w<=W-1;w++)
                                      {
                                             fscanf(fin,"%d",&altitude);    
                                             a[h].push_back(altitude);   
                                             ans[h][w]=' ';   
                                      }
                     }
                     
                     for(h=0;h<=H-1;h++)
                     {
                                      for(w=0;w<=W-1;w++)
                                      {
                                             point p;p.i=h;p.j=w;
                                             if(ans[h][w]==' ')
                                             {
                                                             //cout<<"\n For point: "<<h<<w;
                                                             point s=goto_sink(p);
                                                             ans[s.i][s.j]=curr_char;
                                                             crawl_from_sink(s);
                                                             //cout<<"Sink: "<<s.i<<' '<<s.j<<endl;
                                                             
                                                                                
                                                                                
                                                             //cin>>ch;
                                                             curr_char++;
                                             }
                                                   
                                      }
                     }
                     fprintf(fout,"Case #%d:\n",t);
                     for(i=0;i<=H-1;i++)
                     {
                                        for(j=0;j<=W-1;j++)
                                        {
                                                           fprintf(fout,"%c ",ans[i][j]);
                                        }
                                        fprintf(fout,"\n");
                     }
                     //cin>>ch;
                     
                     
                     
                     
    }
    /*
    a a a b b b 
a a a b b b 
a a a b b b 
a a a a b b 
a a a a a b 

    */
    
    fclose(fin);
    fclose(fout);
    //fclose(fout);
    
    return 0;
}
