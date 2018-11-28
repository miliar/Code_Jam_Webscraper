#include<iostream>
#include<algorithm>
#include<conio.h>
#include<fstream>
using namespace std;
class node
{
      public:
              long long int x,y;
      public:
             node(){}
             node(long long int a,long long int b):x(a),y(b)
             {
             }
             bool operator<(const node &n)const
             {
                  if(x!=n.x) return (x<n.x);
                  return (y<n.y);
             }
};
class tree{
          long long int x;
          long long int y;
          tree *left,*right;
          int height;
          public:
                 tree()
                 {
                       tree(0,0);
                 }
                 tree(long long int  v1,long long int v2):x(v1),y(v2),left(0),right(0),height(0)
                 {
                 }
                 int getheight()
                 {
                     return (this==0)?-1:height;
                 }
                 long long int getdata()
                 {
                      return x;
                 }
                 void updateheight()
                 {
                      height=max(left->getheight(),right->getheight())+1;
                 }
                 bool insert(long long int val1,long long int val2,tree* &tr)
                 {
                      if(tr==0){
                          tr=new tree(val1,val2);
                          return 1;
                      }
                      bool a;
                      if(x>val1){
                                   a=left->insert(val1,val2,tr->left);
                                   if(left->getheight()+2==right->getheight())
                                   {
                                      if(left->getdata()>val1)
                                                singlerotateright(tr);            
                                       else if(left->getdata()<val1)
                                                doublerotateright(tr);          
                                   }
                      }
                      else if(x<val1){
                                   a=right->insert(val1,val2,tr->right);
                                   if(right->getheight()+2==left->getheight())
                                   {
                                       if(right->getdata()<val1)
                                             singlerotateleft(tr);
                                       else if(right->getdata()<val1)
                                           doublerotateleft(tr);
                                   }
                      }
                      else if(x==val1){
                           if(y<val2){
                              a=right->insert(val1,val2,tr->right);
                              if(right->getheight()+2==left->getheight())
                                   {
                                       if(right->getdata()<val1)
                                             singlerotateleft(tr);
                                       else
                                           doublerotateleft(tr);
                                   }
                           }
                            else if(y>val2){
                              a=left->insert(val1,val2,tr->left);
                              if(left->getheight()+2==right->getheight())
                                   {
                                      if(left->getdata()>val1)
                                                singlerotateright(tr);            
                                       else 
                                                doublerotateright(tr);          
                                   }
                            }
                            else
                               return 0;    
                           
                      }
                      tr->updateheight();
                      return a;
                 }
                  friend void singlerotateright(tree *&tr)
                 {
                        tree *temp=tr->left;
                        tr->left=temp->right;
                        temp->right=tr;
                        tr->updateheight();
                        temp->updateheight();
                        tr=temp;
                 }
                 friend void doublerotateright(tree *&tr)
                 {
                        singlerotateleft(tr->left);
                        singlerotateright(tr);
                        
                 }
                 friend void singlerotateleft(tree *&tr)
                 {
                        tree *temp=tr->right;
                        tr->right=temp->left;
                        temp->left=tr;
                        tr->updateheight();
                        temp->updateheight();
                        tr=temp;
                 }
                 friend void doublerotateleft(tree *&tr)
                 {
                        singlerotateright(tr->right);
                        singlerotateleft(tr);
                 }
                 
};
bool binarysearch(long long int &x1,long long int &y1,node *a,long long int &n)
{
     int low=0,high=n-1,mid=(low+high)/2;
     while(low<=high)
     {
                     if(a[mid].x==x1)
                     {
                        if(a[mid].y>y1)
                          high=mid-1;
                        else if(a[mid].y<y1)
                          low=mid+1;
                        else                 
                             return 1;
                     }
                     if(a[mid].x<x1)
                        low=mid+1;
                     if(a[mid].x>x1)
                       high=mid-1;
       mid=(low+high)/2;
     }
     return 0;
}
int main()
{
    int nt;int g=1;
    ifstream din("A-small-attempt0.in");
    ofstream dout("out.txt");
    din>>nt;
    while(nt--)
    {
               long long int a,b,c,d,n,m,count=0,f;
               tree *tr=NULL;
               din>>n>>a>>b>>c>>d;
               long long int x[n],y[n],i,j,k;
               node arr[n];
               din>>x[0]>>y[0]>>m;
               arr[0].x=x[0];arr[0].y=y[0];
               for(i=1;i<n;i++)
               {
                               x[i]=(a*x[i-1]+b)%m;
                               y[i]=(c*y[i-1]+d)%m;
                              /* if(!tr->insert(x[i],y[i],tr))
                                  break;*/
               }
               f=i;
               for(i=0;i<f;i++)
                for(j=i+1;j<f;j++)
                 for(k=j+1;k<f;k++)
                 {            
                       if(((x[i]+x[j]+x[k])%3==0)&&((y[i]+y[j]+y[k])%3==0))
                  {           
                           ++count;
                   }           
                                   
                 }
                 
                 dout<<"Case #"<<g<<": "<<count<<endl;
                 cout<<"Case #"<<g<<": "<<count<<endl;
                 g++;
    }
    getch();
    return 0;
}
