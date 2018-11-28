#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<algorithm>
#include <sstream>
using namespace std;
int N,T,NA,NB;
vector <int> a1,b1,a2,b2,A,B;
int a2i(string s)
{
    int t;
    istringstream totalSString( s );
    totalSString >>t;
    return t;
}
void sortinga()
{
  int key,key2,i,j;
  for(j=1;j<a1.size();j++)
  {
     key=a1[j];
     key2=a2[j];
     i=j-1;
     while(a1[i]>key && i>=0)
     {
         a1[i+1]=a1[i];
         a2[i+1]=a2[i];
         i--;
     }
     a1[i+1]=key;
     a2[i+1]=key2;
  }
}
void sortingb()
{
  int key,key2,i,j;
  for(j=1;j<b1.size();j++)
  {
     key=b1[j];
     key2=b2[j];
     i=j-1;
     while(b1[i]>key && i>=0)
     {
         b1[i+1]=b1[i];
         b2[i+1]=b2[i];
         i--;
     }
     b1[i+1]=key;
     b2[i+1]=key2;
  }
}
int main()
{
    int i,j,k,ca,cb,ai,bi,flag;
    string temp1,temp2;
    cin>>N;
    for(i=0;i<N;i++)
    {
         cin>>T;
         cin>>NA>>NB;
         a1.clear();
         A.clear();
         B.clear();
         b1.clear();
         a2.clear();
         b2.clear();
         for(j=0;j<NA;j++)
         {
                          cin>>temp1>>temp2;
                          a1.push_back(((a2i(temp1.substr(0,2))*60)+a2i(temp1.substr(3,2))));
                          a2.push_back(((a2i(temp2.substr(0,2))*60)+a2i(temp2.substr(3,2))));
                          A.push_back(0);
                          //cout<<"**"<<a1[j]<<a2[j];
         }
         for(j=0;j<NB;j++)
         {
                          cin>>temp1>>temp2;
                          b1.push_back(((a2i(temp1.substr(0,2))*60)+a2i(temp1.substr(3,2))));
                          b2.push_back(((a2i(temp2.substr(0,2))*60)+a2i(temp2.substr(3,2))));
                          B.push_back(0);
         }
         sortinga();
         sortingb();
         /*for(j=0;j<NA;j++)
         {
                          cout<<a1[j]<<a2[j];                
         }
         */
         ai=bi=0;
         ca=cb=0;
         while(ai<NA&&bi<NB)
         {
              if(a1[ai]<=b1[bi])
              {
                 flag=0;
                 for(j=0;b1[j]<a1[ai]&&j<NB;j++)
                 {
                         if(B[j]==0&&((b2[j]+T)<=a1[ai]))
                         {
                               B[j]=1;
                               flag=1;
                               break;
                         }
                 }
                 if(flag==0)
                            ca++;
                 ai++;                 
              }
              else
              {
                 flag=0;
                 for(j=0;a1[j]<b1[bi]&&j<NA;j++)
                 {
                         if(A[j]==0&&((a2[j]+T)<=b1[bi]))
                         {
                               A[j]=1;
                               flag=1;
                               break;
                         }
                 }
                 if(flag==0)
                            cb++;
                 bi++; 
              }
         }
         while(ai<NA)
         {
                 flag=0;
                 for(j=0;b1[j]<a1[ai]&&j<NB;j++)
                 {
                         if(B[j]==0&&((b2[j]+T)<=a1[ai]))
                         {
                               B[j]=1;
                               flag=1;
                               break;
                         }
                 }
                 if(flag==0)
                            ca++;
                 ai++;                 
         }
         while(bi<NB)
         {
                 flag=0;
                 for(j=0;a1[j]<b1[bi]&&j<NA;j++)
                 {
                         if(A[j]==0&&((a2[j]+T)<=b1[bi]))
                         {
                               A[j]=1;
                               flag=1;
                               break;
                         }
                 }
                 if(flag==0)
                            cb++;
                 bi++; 
         }
    cout<<"Case #"<<i+1<<": "<<ca<<" "<<cb<<"\n";
    }
    //system("PAUSE");
    return 1;
}
