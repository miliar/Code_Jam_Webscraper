#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<map>
using namespace std;
int check(int i,int j,vector< vector<int> > &a,vector< vector<int> > &v,int m ,int n);
int main()
{
 	 ifstream fin1("B-large.in");
 	 ofstream fout1("B-large.out");
 	 int t;
 	 fin1>>t;
 	 for(int p=0;p<t;p++)
 	 {
	     vector< vector<int> > v;
	     vector<int> temp;
		 int m,n;
		 fin1>>m>>n;
		 for(int i=0;i<m;i++)
		 {
		  		 vector<int> temp;
		  		 for(int j=0;j<n;j++)
		  		 {
				  		 int n1;
				  		 fin1>>n1;
				  		 temp.push_back(n1);
		         }
		         v.push_back(temp);
		 }
		 vector<int> temp2(n,-1);
		 vector< vector<int> > a(m,temp2);
		 vector<char> temp1(n,'a');
		 vector< vector<char> > ans(m,temp1);
		 map<int,char> alpha;
		 int n_alpha=(int)'a';
		 for(int i=0;i<m;i++)
		 for(int j=0;j<n;j++)
		 {
		   int temp=check(i,j,a,v,m,n);
		   if(!alpha[temp])
		     alpha[temp]=(char)n_alpha++;
	       ans[i][j]=alpha[temp];
         }
         fout1<<"Case #"<<p+1<<":"<<endl;
         for(int i=0;i<m;i++)
         {
		  for(int j=0;j<n;j++)
          fout1<<ans[i][j]<<" ";
          if(p==t-1 && i==m-1)fout1<<"";else fout1<<endl;
	     }
         
    }				 
    return 0;
    
}

int check(int i,int j,vector< vector<int> > &a,vector< vector<int> > &v,int m ,int n)
{
  if(a[i][j]!=-1)return a[i][j];
  bool flag=false;
  vector< pair<int,int> > p;
  if(i>0)p.push_back(make_pair(i-1,j) );  
  if(j>0)p.push_back(make_pair(i,j-1));
  if(j<n-1)p.push_back(make_pair(i,j+1));
  if(i<m-1)p.push_back(make_pair(i+1,j));
  int minx=i,miny=j;
  int min=v[i][j];
  for(int r=0;r<p.size();r++)
  {
     if(v[ p[r].first ][p[r].second ] < min )
	 {min=v[ p[r].first ][p[r].second];minx=p[r].first;miny=p[r].second;} 
  }
  if(min!=v[i][j])
  {				  
   if(a[minx][miny]!=-1)a[i][j]=a[minx][miny];
   else
   {
   	  a[i][j]=check(minx,miny,a,v,m,n);
   }
   return a[i][j]; 		  
  }
  else
  {
   	  a[i][j]=i*n+j; 
      return (a[i][j]);		 
  }		 	 
}
